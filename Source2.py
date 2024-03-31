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
                        self.VE_NOT_DESIRED_INPUT = "[-] Error: One of the input is not one of the following: Yes, No, Male, Female"
                        self.Error_Dictionary = {
                                "IDT_NOT_DESIRED_DATATYPE_ERROR": "[-] Error: One of the values is not a number or float",
                                "VE_NOT_DESIRED_INPUT": "[-] Error: One of the input is not one of the following: Yes, No, Male, Female"
                        }

                def Validate_Inputs (self):

                        for CurrentlyLoopedKey, CurrentlyLoopedValue in DictionaryVariables["Binary_Variables"].items():
                                StringVersion = str(CurrentlyLoopedValue)
                                try:
                                        if StringVersion.lower() == "yes" or StringVersion.lower() == "male":
                                                DictionaryVariables["Binary_Variables"].update({CurrentlyLoopedKey: 1})
                                        elif StringVersion.lower() == "no" or StringVersion.lower() == "female":
                                                DictionaryVariables["Binary_Variables"].update({CurrentlyLoopedKey: 0})
                                        else:
                                                #raise ValueError(self.Error_Dictionary.get("VE_NOT_DESIRED_INPUT"))
                                                pass
                                except ValueError:
                                        print("[-] Error - Key: {}, Value: {}".format(CurrentlyLoopedKey, CurrentlyLoopedValue))

                        for NumberValue in zip(DictionaryVariables["Integer_Continuous_Variables"].values()):
                                try:
                                        if isinstance(NumberValue, int) or isinstance(NumberValue, float):
                                                continue
                                        else:
                                                raise TypeError(self.Error_Dictionary.get("VE_NOT_DESIRED_INPUT"))
                                except TypeError as IDT_ERROR:
                                        print(IDT_ERROR)
                                        main()
                        
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
