import json
from pathlib import Path

adults_bmi_classification = [
    "severe thinness",
    "moderate thinness",
    "mild thinness",
    "normal",
    "overweight",
    "obese class I",
    "obese class II",
    "obese class III",
]  # BMI classification for adults

adults_bmi_range = [
    "< 16",
    "16 - 17",
    "17 - 18.5",
    "18.5 - 25",
    "25 - 30",
    "30 - 35",
    "35 - 40",
    "> 40",
]  # BMI range for adults in kg/m^2

teens_and_children_bmi_classification = [
    "underweight",
    "healthy weight",
    "at risk of overweight",
    "overweight",
]  # BMI classification for teens and children

teens_and_children_bmi_percentile_range = [
    "< 5%",
    "5% - 85%",
    "85% - 95%",
    "> 95%",
]  # BMI percentile range for teens and children


adult_data = {}
teen_and_child_data = {}

for key, value in zip(adults_bmi_classification, adults_bmi_range):
    adult_data[key] = value

for key, value in zip(
    teens_and_children_bmi_classification, teens_and_children_bmi_percentile_range
):
    teen_and_child_data[key] = value

print(adult_data)
print(teen_and_child_data)

paths = ["adults_bmi_classification.txt", "teens_or_child_bmi_classification.txt"]

for filename in paths:
    path = Path(filename)
    if filename == paths[0]:
        contents = json.dumps(adult_data)
    else:
        contents = json.dumps(teen_and_child_data)

    path.write_text(contents)
