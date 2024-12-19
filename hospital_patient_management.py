class Patient:
    def _init_(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
def search_patients_by_disease(patients, disease):
    return [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease = input("Enter disease to search for: ")
result = search_patients_by_disease(patients, search_disease)
if result:
    print(f"Patients with {search_disease}: {result}")
else:
    print(f"No patients found with disease: {search_disease}")