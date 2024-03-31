import pickle
import pandas as pd
from MainPackage import variables as var

class Main:

        class LoadModel:

                def __init__(self):
                        self.Interaction_Class_Access = Main.InteractModel()
                
                def Load (self):
                        with open ("/home/mikkel-ai/Desktop/Machine Learning/Heart Failure Classifier/Project-HeartFailureClassifier/Model/DTC_Model.pkl", "rb") as DTC_Model_Dump:
                                var.DecisionTreeClassifierModel = pickle.load(DTC_Model_Dump)
                        print("\n\n[+] Successfully loaded DecisionTreeClassifier model\n\n")

        class InteractModel:

                def __init__(self):
                        self.DTC_Model = None
                        self.VE_NOT_DESIRED_INPUT_ONE = "[-] Error: One of the input is not one of the following: Yes, No, Male, Female"
                        self.VE_NOT_DESIRED_INPUT_TWO = "[-] Error: One of the inputs is neither int or float"
                        
                def Validate_Inputs (self):

                        for Binary_CLK, Binary_CLV in DictionaryVariables["Binary_Variables"].items():
                                StringVersion = str(Binary_CLV)
                                try:
                                        if StringVersion.lower() == "yes" or StringVersion.lower() == "male":
                                                DictionaryVariables["Binary_Variables"].update({Binary_CLK: 1})
                                        elif StringVersion.lower() == "no" or StringVersion.lower() == "female":
                                                DictionaryVariables["Binary_Variables"].update({Binary_CLK: 0})
                                        else:
                                                raise ValueError(self.VE_NOT_DESIRED_INPUT_ONE)
                                except ValueError as VAL_ERROR:
                                        print("\n\n{} \n[-] Error: Key - {} | Value - {}\n\n".format(VAL_ERROR, Binary_CLK, Binary_CLV))

                        for Number_CLK, Number_CLV in DictionaryVariables["Integer_Continuous_Variables"].items():
                                try:
                                        if int(Number_CLV) or float(Number_CLV):
                                                continue
                                        else:
                                                raise ValueError(self.VE_NOT_DESIRED_INPUT_TWO)
                                except ValueError as VAL_ERROR:
                                        print("\n\n{} \n[-] Error: Key - {} | Value - {}\n\n".format(VAL_ERROR, Number_CLK, Number_CLV))
                        
                        print("\n\n[+] All inputs are correct, proceeding with sorting inputs")
                        self.Sort_Dictionary_And_Convert()

                def Sort_Dictionary_And_Convert (self):
                        
                        for Element in var.ArrayToCompare:
                                for Outer_DK, Outer_DV in DictionaryVariables["Binary_Variables"].items():
                                        for Inner_DK, Inner_DV in DictionaryVariables["Integer_Continuous_Variables"].items():
                                                if Outer_DK == Element:
                                                        var.DictionaryToConvert.update({Outer_DK: Outer_DV})
                                                elif Inner_DK == Element:
                                                        var.DictionaryToConvert.update({Inner_DK: Inner_DV})
                                                else:
                                                        continue

                        for Final_DK, Final_DV in var.DictionaryToConvert.items():
                                print("Key: {} | Value: {}".format(Final_DK, Final_DV))

                        var.DataframeToFeed = pd.DataFrame(data=var.DictionaryToConvert, columns=var.ArrayOfColumnsForDF)
                        print("\n\n[+] Dictionary successfully converted to Pandas Dataframe, proceeding with making predictions...")
                        self.Interact_With_Model()

                def Interact_With_Model (self):
                        
                        ModelPrediction = var.DecisionTreeClassifierModel.predict(var.DataframeToFeed)

                        if ModelPrediction == 0:
                                print("\n\n---------- RESULT ----------")
                                print("[+] Patient is not going to have a heart attack")
                        else:
                                print("\n\n---------- RESULT ----------")
                                print("Patient in more likely to have a heart attack")

def main ():
        
        Nested_Load_Model = Main.LoadModel()
        Nested_Interact_Model = Main.InteractModel()

        Nested_Load_Model.Load()

        global DictionaryQuestions
        global DictionaryVariables

        DictionaryQuestions = {
                "Binary_Question": {
                        "Anemia_Question": var.If_Patient_Has_Anemia,
                        "Diabetes_Question": var.If_Patient_Has_Diabetes,
                        "HBP_Question": var.If_Patient_Has_HBP,
                        "Gender_Question": var.If_Patient_Is_Male_Or_Female,
                        "Smoking_Question": var.If_Patient_Is_Smoking
                },
                "Integer_Continuous_Question": {
                        "Age_Question": var.Patient_Age_Question,
                        "Creatinine_Phospho_Question": var.Patient_Creatinine_Phospho_Question,
                        "Ejection_Fraction_Question": var.Patient_Ejection_Fraction_Question,
                        "Serum_Sodium_Question": var.Patient_Serum_Sodium_Question,
                        "Time_Question": var.Patient_Time,
                        "Platelets_Question": var.Patient_Platelets_Amount,
                        "Serum_Creatinine_Question": var.Patient_Serum_Creatinine
                }
        }

        DictionaryVariables = {
                "Binary_Variables": {
                        "Anemia_Variable": var.PatientAnemia,
                        "Diabetes_Variable": var.PatientDiabetes,
                        "HBP_Variable": var.PatientHBP,
                        "Gender_Variable": var.PatientSex,
                        "Smoking_Variable": var.PatientSmoking
                },
                "Integer_Continuous_Variables": {
                        "Age_Variable": var.PatientAge,
                        "Creatinine_Phospho_Variable": var.PatientCreatininePhospo,
                        "Ejection_Fraction_Variable": var.PatientEjectionFrac,
                        "Serum_Sodium_Variable": var.PatientSerumSodium,
                        "Time_Variable": var.PatientTime,
                        "Platelets_Variable": var.PatientPlatelets,
                        "Serum_Creatinine_Variable": var.PatientSerumCreatinine
                }
        }

        """
        Both loops do the same thing but in different nested dictionaries.
        The for loop will loop through DictionaryQuestion values and DictionaryVariables keys using zip function.
        Next, it will capture user input then update the key value in the currently looped nested dictionary with the user input

        Believe me, there is no other way to make this. Atleast in my level :D
        """

        for (PatientQuestion, CurrentlyLoopedKey) in zip(DictionaryQuestions["Binary_Question"].values(), DictionaryVariables["Binary_Variables"].keys()):
                UserAnswer = input(PatientQuestion)
                DictionaryVariables["Binary_Variables"].update({CurrentlyLoopedKey: UserAnswer})

        for (PatientQuestion, CurrentlyLoopedKey) in zip(DictionaryQuestions["Integer_Continuous_Question"].values(), DictionaryVariables["Integer_Continuous_Variables"].keys()):
                UserAnswer = input(PatientQuestion)
                DictionaryVariables["Integer_Continuous_Variables"].update({CurrentlyLoopedKey: UserAnswer})

        Nested_Interact_Model.Validate_Inputs()

main()
