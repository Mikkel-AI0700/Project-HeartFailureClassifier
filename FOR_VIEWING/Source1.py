import pickle
import pandas as pd
from MainPackage import variables as var

class Main:

        class LoadModel:

                def __init__(self):
                        self.Interaction_Class_Access = Main.InteractModel()
                
                def Load (self):
                        with open ("/home/mikkel-ai/Desktop/Machine Learning/Heart Failure Classifier/Project-HeartFailureClassifier/Model/DTC_Model.pkl", "rb") as DTC_Model_Dump:
                                self.Interaction_Class_Access.DTC_Model = pickle.load(DTC_Model_Dump)
                        print("[+] Successfully loaded DecisionTreeClassifier model")

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
                                        print(VAL_ERROR)
                                        print("[-] Error - Key: {}, Value: {}".format(Binary_CLK, Binary_CLV))

                        for Number_CLK, Number_CLV in DictionaryVariables["Integer_Continuous_Variables"].items():
                                try:
                                        if int(Number_CLV) or float(Number_CLV):
                                                continue
                                        else:
                                                raise ValueError(self.VE_NOT_DESIRED_INPUT_TWO)
                                except ValueError as VAL_ERROR:
                                        print(VAL_ERROR)
                                        print("[-] Error - Key: {}, Value: {}".format(Number_CLK, Number_CLV))
                        
                        print("[+] All inputs are correct, proceeding with using the Machine Learning model")
                        self.Interact()

                def Interact (self):
                        
                        for (DicKey1, DicValue1), (DicKey2, DicValue2) in zip(DictionaryVariables["Binary_Variables"].items(), DictionaryVariables["Integer_Continuous_Variables"].items()):
                                pass

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

        for (PatientQuestion, CurrentlyLoopedKey) in zip(DictionaryQuestions["Binary_Question"].values(), DictionaryVariables["Binary_Variables"].keys()):
                UserAnswer = input(PatientQuestion)
                DictionaryVariables["Binary_Variables"].update({CurrentlyLoopedKey: UserAnswer})

        for (PatientQuestion, CurrentlyLoopedKey) in zip(DictionaryQuestions["Integer_Continuous_Question"].values(), DictionaryVariables["Integer_Continuous_Variables"].keys()):
                UserAnswer = input(PatientQuestion)
                DictionaryVariables["Integer_Continuous_Variables"].update({CurrentlyLoopedKey: UserAnswer})

        Nested_Interact_Model.Validate_Inputs()

main()
