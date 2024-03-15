import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class Main:

        class LoadModel:
                
                def __init__ (self):
                        self.Interaction_Class_Access = Main.Interaction()

                def Load (self):
                        with open("/home/ai/Desktop/Machine Learning/Legit ML Projects/Heart Failure/Model/DTC_Model.pkl", "rb") as FileRead:
                                self.Interaction_Class_Access.DTC_Model = pickle.load(FileRead)
                                print("[+] Successfully loaded model")

        class Interaction:
                
                def __init__(self):
                        self.DTC_Model = None
                        self.Error_Dictionary = {
                                "IDT_NOT_DESIRED_TYPE_ERROR": "[-] Error: One of the values is not the desired data type",
                                "VE_INSUFFICIENT_INPUT_ERROR": "[-] Error: Insufficient input"
                        }

                def ValidateInputs (self):
                        
                        for MainKey, MainValue in MainDictionary2.items():
                                try:
                                        if MainValue is None:
                                                raise TypeError(self.Error_Dictionary.get("VE_INSUFFICIENT_INPUT_ERROR"))
                                        else:
                                                if isinstance(MainValue, bool) or isinstance(MainValue, int) or isinstance(MainValue, float):
                                                        continue
                                                else:
                                                        raise TypeError(self.Error_Dictionary.get("IDT_NOT_DESIRED_TYPE_ERROR"))
                                except TypeError as NULL_OR_IDT_ERROR:
                                        print(NULL_OR_IDT_ERROR)
                                        main()

                def InteractModel (self):
                        pass

def main ():

        global MainDictionary2
        MainDictionary2 = {
                # Binary 1 and 0 questions
                "Patient_Has_Anemia": None,
                "Patient_Has_Diabetes": None,
                "Patient_Has_HBP": None,
                "Patient_Sex": None,
                "Patient_Is_Smoking": None,
                # Integer questions
                "Patient_Age": None,
                "Patient_CP": None,
                "Patient_EF": None,
                "Patient_SS": None,
                "Patient_Age": None,
                # Continuous questions
                "Patient_Platelets": None,
                "Patient_SC": None
        }
