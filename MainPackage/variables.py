
# Binary questions
If_Patient_Has_Anemia = "Does the Patient have Anemia (Yes or no): "
If_Patient_Has_Diabetes = "Does the Patient have Diabates (Yes or no): "
If_Patient_Has_HBP = "Does the Patient have High Blood Pressure (Yes or no): "
If_Patient_Is_Male_Or_Female = "is the Patient male or female: "
If_Patient_Is_Smoking = "Is the Patient smoking (Yes or no): "

# Integer questions
Patient_Age_Question = "What is the Patient's age: "
Patient_Creatinine_Phospho_Question = "What is the Patient's creatinine phosphokine: "
Patient_Ejection_Fraction_Question = "What is the Patient's Ejection Fraction: "
Patient_Serum_Sodium_Question = "What is the Patient's Serum Sodium: "
Patient_Time = "WHat is the Patient's time: "

# Continuous questions
Patient_Platelets_Amount = "What is the amount of platelets the Patient has: "
Patient_Serum_Creatinine = "What is the amount of the Serum Creatinine of the Patient: "

# Binary variables
PatientAnemia = ""
PatientDiabetes = ""
PatientHBP = ""
PatientSex = ""
PatientSmoking = ""

# Integer questions
PatientAge = 0
PatientCreatininePhospo = 0
PatientEjectionFrac = 0
PatientSerumSodium = 0
PatientTime = 0

# Continuous variables
PatientPlatelets = 0
PatientSerumCreatinine = 0

# For interacting with the model
SeriesToFeed = None
DictionaryToConvert = {}
DataframeToFeed = None
DecisionTreeClassifierModel = None

# For dictionary order
ArrayToCompare = ["Age_Variable", "Anemia_Variable", "Creatinine_Phospho_Variable", 
                  "Diabetes_Variable", "Ejection_Fraction_Variable", "HBP_Variable", 
                  "Platelets_Variable", "Serum_Creatinine_Variable", "Serum_Sodium_Variable", 
                  "Gender_Variable", "Smoking_Variable", "Time_Variable"]

ArrayOfColumnsForDF = ["age", "anaemia", "creatinine_phosphokinase", 
                       "diabetes", "ejection_fraction", "high_blood_pressure", 
                       "platelets", "serum_creatinine", "serum_sodium", 
                       "sex", "smoking", "time"]

# age, anemia, 
