import pickle
import pandas as pd
from MainPackage import variables

class Main:

        class LoadModel:

                def __init__ (self):
                        self.Interaction_Class_Access = Main.ModelInteraction()

                def Load (self):
                        with open("/home/ai/Desktop/Machine Learning/Legit ML Projects/Heart Failure/Model/DTC_Model.pkl", "wb") as ML_Model_Dump:
                                self.Interaction_Class_Access.DTC_Model = pickle.load(ML_Model_Dump)
                                print("[+] Successfully loaded model")

        class ModelInteraction:

                def __init__ (self, MainVariableArray):
                        self.DTC_Model = None
                        self.Error_Dictionary = {
                                "IDT_NOT_DESIRED_TYPE_ERROR": "[-] Error: One of the values isn't: bool, int, float or instead NULL",
                                "VE_UNEXPECTED_INPUT_ERROR": "[-] Error: Yes or no value expected, instead got anything other than a yes or no"
                        }
                        self.Dictionary_Of_Inputs = {
                                "Binary_Questions": {
                                        "Patient_Anemia": MainVariableArray[0][0],
                                        "Patient_Diabetes": MainVariableArray[0][1],
                                        "Patient_HBP": MainVariableArray[0][2],
                                        "Patient_Sex": MainVariableArray[0][3],
                                        "Patient_Smoking": MainVariableArray[0][4]
                                },
                                "Integer_Questions": {
                                        "Patient_Age": MainVariableArray[1][0],
                                        "Patient_Creatinine_Phospo": MainVariableArray[1][1],
                                        "Patient_Ejection_Fraction": MainVariableArray[1][2],
                                        "Patient_Serum_Sodium": MainVariableArray[1][3],
                                        "Patient_Time": MainVariableArray[1][4]
                                },
                                "Continuous_Questions": {
                                        "Patient_Platelets": MainVariableArray[2][0],
                                        "Patient_Serum_Creatinine": MainVariableArray[2][1]
                                }
                        }

                def Validate_Inputs (self):
                        
                        # For Loop for binary questions
                        for BinaryValue in self.Dictionary_Of_Inputs["Binary_Questions"].values():
                                BinaryStringFormat = str(BinaryValue)
                                try:
                                        if BinaryValue is None or BinaryStringFormat == "":
                                                raise TypeError(self.Error_Dictionary.get("IDT_NOT_DESIRED_TYPE_ERROR"))
                                        if BinaryStringFormat.lower() == "yes" or BinaryStringFormat.lower() == "male":
                                                BinaryValue = 1
                                        elif BinaryStringFormat.lower() == "no" or BinaryStringFormat.lower() == "female":
                                                BinaryValue = 0
                                        else:
                                                raise ValueError(self.Error_Dictionary.get("VE_UNEXPECTED_INPUT_ERROR"))
                                except ValueError as VALUE_ERROR:
                                        print(VALUE_ERROR)
                                except TypeError as TYPE_ERROR:
                                        print(TYPE_ERROR)

                        # For Loop for integer questions
                        for IntegerValue in self.Dictionary_Of_Inputs["Integer_Questions"].values():
                                try:
                                        if IntegerValue is None:
                                                raise ValueError(self.Error_Dictionary.get("VE_NULL_VALUE_DETECTED_ERROR"))
                                        if not int(IntegerValue):
                                                raise TypeError(self.Error_Dictionary.get("IDT_NOT_DESIRED_TYPE_ERROR"))
                                except ValueError as NULL_VALUE_ERROR:
                                        print(NULL_VALUE_ERROR)
                                except TypeError as IDT_ERROR:
                                        print(IDT_ERROR)
                        
                        # For Loop for continuous questions
                        for ContinuousValue in self.Dictionary_Of_Inputs["Continuous_Questions"].values():
                                try:
                                        if ContinuousValue is None:
                                                raise ValueError(self.Error_Dictionary.get("VE_NULL_VALUE_DETECTED_ERROR"))
                                        if not float(ContinuousValue):
                                                raise TypeError(self.Error_Dictionary.get("IDT_NOT_DESIRED_TYPE_ERROR"))
                                except ValueError as NULL_VALUE_ERROR:
                                        print(NULL_VALUE_ERROR)
                                except TypeError as IDT_ERROR:
                                        print(IDT_ERROR)

                def Interact (self):
                        pass

def main ():

        MainClass = Main()

        global DictionaryHousingQuestions
        global DictionaryHousingVariables

        DictionaryHousingQuestions = {
                "Binary_Questions": {
                        "If_Patient_Has_Anemia": variables.If_Patient_Has_Anemia,
                        "If_Patient_Has_Diabetes": variables.If_Patient_Has_Diabetes,
                        "If_Patient_Has_HBP": variables.If_Patient_Has_HBP,
                        "If_Male_Or_Female": variables.If_Patient_Is_Male_Or_Female,
                        "If_Patient_Is_Smoking": variables.If_Patient_Is_Smoking
                },
                "Integer_Continuous_Questions": {
                        "Age_Question": variables.Patient_Age_Question,
                        "Creatinine_Phospo_Question": variables.Patient_Creatinine_Phospho_Question,
                        "Ejection_Fraction_Question": variables.Patient_Ejection_Fraction_Question,
                        "Serum_Sodium_Question": variables.Patient_Serum_Sodium_Question,
                        "Time_Question": variables.Patient_Time,
                        "Platelets_Amount_Question": variables.Patient_Platelets_Amount,
                        "Serum_Creatinine_Question": variables.Patient_Serum_Sodium_Question
                }
        }

        DictionaryHousingVariables = {
                "Binary_Variables": {
                        "Anemia_Input": variables.PatientAnemia,
                        "Diabetes_Input": variables.PatientDiabetes,
                        "HBP_Input": variables.PatientHBP,
                        "Gender_Input": variables.PatientSex,
                        "Smoking_Input": variables.PatientSmoking
                },
                "Integer_Continuous_Variables": {
                        "Age_Input": variables.PatientAge,
                        "Creatinine_Phospo_Input": variables.PatientCreatininePhospo,
                        "Ejection_Fraction_Input": variables.PatientEjectionFrac,
                        "Serum_Sodium_Input": variables.PatientSerumSodium,
                        "Time_Input": variables.PatientTime,
                        "Platelets_Input": variables.PatientPlatelets,
                        "Serum_Creatinine_Input": variables.PatientSerumCreatinine
                }
        }

main()
