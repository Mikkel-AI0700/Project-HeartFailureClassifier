import pickle
import pandas as pd

class Main:

        class LoadModel:

                def __init__ (self):
                        self.Interaction_Class_Access = Main.ModelInteraction()

                def Load (self):
                        with open("/home/ai/Desktop/Machine Learning/Legit ML Projects/Heart Failure/Model/DTC_Model.pkl", "wb") as ML_Model_Dump:
                                self.Interaction_Class_Access.DTC_Model = pickle.load(ML_Model_Dump)
                                print("[+] Successfully loaded model")

        class ModelInteraction:

                def __init__ (self, BinaryQuestionsList, IntegerQuestionsList, ContinuousQuestionsList):
                        self.DTC_Model = None
                        self.Error_Dictionary = {
                                "IDT_NOT_DESIRED_TYPE_ERROR": "[-] Error: One of the values isn't: bool, int, float",
                                "VE_NULL_VALUE_DETECTED_ERROR": "[-] Error: Null value detected, please input the required amount of inputs"
                        }
                        self.Dictionary_Of_Inputs = {
                                "Binary_Questions": {
                                        "Patient_Anemia": BinaryQuestionsList[0],
                                        "Patient_Diabetes": BinaryQuestionsList[1],
                                        "Patient_HBP": BinaryQuestionsList[2],
                                        "Patient_Sex": BinaryQuestionsList[3],
                                        "Patient_Smoking": BinaryQuestionsList[4]
                                },
                                "Integer_Questions": {
                                        "Patient_Age": IntegerQuestionsList[0],
                                        "Patient_Creatinine_Phospo": IntegerQuestionsList[1],
                                        "Patient_Ejection_Fraction": IntegerQuestionsList[2],
                                        "Patient_Serum_Sodium": IntegerQuestionsList[3],
                                        "Patient_Time": IntegerQuestionsList[4]
                                },
                                "Continuous_Questions": {
                                        "Patient_Platelets": ContinuousQuestionsList[0],
                                        "Patient_Serum_Creatinine": ContinuousQuestionsList[1]
                                }
                        }

                def Validate_Inputs (self):
                        
                        # For Loop for binary questions
                        for BinaryValue in self.Dictionary_Of_Inputs["Binary_Questions"].values():
                                BinaryStringFormat = str(BinaryValue)
                                try:
                                        if BinaryValue is None or BinaryValue == "":
                                                raise ValueError(self.Error_Dictionary.get("VE_NULL_VALUE_DETECTED_ERROR"))
                                        if BinaryStringFormat.lower() == "yes":
                                                BinaryValue = 1
                                        elif BinaryStringFormat.lower() == "no":
                                                BinaryValue = 0
                                        else:
                                                raise TypeError(self.Error_Dictionary.get("IDT_NOT_DESIRED_TYPE_ERROR"))
                                except ValueError as NULL_VALUE_ERROR:
                                        print(NULL_VALUE_ERROR)
                                except TypeError as IDT_ERROR:
                                        print(IDT_ERROR)

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

        # Class initialization
        MainClass = Main()
        
        # Binary questions
        PatientAnemia, PatientDiabetes, PatientHBP, PatientSex, PatientSmoking = None, None, None, None, None
        BinaryQuestionsArray = [PatientAnemia, PatientDiabetes, 
                                PatientHBP, PatientSex, PatientSmoking]

        # Integer questions
        PatientAge, PatientCreatininePhospo, PatientEjectionFrac, PatientSerumSodium, PatientTime = None, None, None, None, None
        IntegerQuestionsArray = [PatientAge, PatientCreatininePhospo, 
                                 PatientEjectionFrac, PatientSerumSodium, PatientTime]

        # Continuous questions
        PatientPlatelets, PatientSerumCreatinine = None, None
        ContinuousQuestionsArray = [PatientPlatelets, PatientSerumCreatinine]

        print("HEART FAILURE CLASSIFIER \nInput the required details")

        BinaryQuestionsArray[0] = input("Does the patient have Anemia (Yes or no): ")
        BinaryQuestionsArray[1] = input("Does the patient have diabetes (Yes or no): ")
        BinaryQuestionsArray[2] = input("Does the patient have High blood pressure (Yes or no): ")
        BinaryQuestionsArray[3] = input("What is the gender of the patient (Male or female): ")        
        BinaryQuestionsArray[4] = input("Is the patient smoking (Yes or no): ")

main()
