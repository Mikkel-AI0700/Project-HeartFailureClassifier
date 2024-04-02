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

                        """
                        First it will loop through the key-value pair of the Dictionary to convert then it does the same for the two nested dictionaries.
                        Next, it will compare if the key is the in the dictionary to convert is the same as the one in the nested dictionaries.
                        If it is, then it will append the value of that nested dictionary value to DTC_CLV array, if not then it will skip to the next iteration
                        """

                        """
                        Due to the code logic of the first group of nested loops, a second group nested loop must be used.
                        It then again loops through the dictionary to convert values, then looped again with an index.
                        While the length of the array in the dictionary value is unequal to 1, it will continuously remove elements.
                        """
                        
                        for DTC_CLK, DTC_CLV in var.DictionaryToConvert.items():
                                for Binary_CLK, Binary_CLV in DictionaryVariables["Binary_Variables"].items():
                                        for Number_CLK, Number_CLV in DictionaryVariables["Integer_Continuous_Variables"].items():
                                                if DTC_CLK == Binary_CLK:
                                                        DTC_CLV.append(Binary_CLV)
                                                elif DTC_CLK == Number_CLK:
                                                        DTC_CLV.append(Number_CLV)
                                                else:
                                                        continue
                        
                        for DTC_Value in var.DictionaryToConvert.values():
                                for Index, ArrayElement in enumerate(DTC_Value):
                                        while len(DTC_Value) != 1:
                                                DTC_Value.pop(Index)

                        print("[+] All inputs sorted, proceeding with interacting with DecisionTreeClassifier model")
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
