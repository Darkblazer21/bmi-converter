is_adult = True
is_teen_or_child = False

weight = 88  # Weight in kilograms
height = 1.85  # Height in meters

adult_bmi = weight / height**2  # BMI formula is weight divided by height squared
teen_or_child_bmi_percentile = 0

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

table_header = "|    Classification    |    BMI Range    |"
header_one = table_header[:23]  # Stores header one before pipe character
header_two = table_header[24:]

print("-" * 42)
print(table_header)
print("-" * 42)

# The loop below prints the array of bmi classification and range for adults
for i in range(len(adults_bmi_classification)):
    word_length_h1 = len(adults_bmi_classification[i])
    spaces_to_add_before_middle_pipe = len(header_one) - word_length_h1 - 1

    word_length_h2 = len(adults_bmi_range[i])
    spaces_to_add_before_last_pipe = len(header_two) - word_length_h2 - 5
    print(
        f"|{adults_bmi_classification[i]}"
        + " "
        * spaces_to_add_before_middle_pipe  # Add one or multiple spaces before pipe
        + f"|    {adults_bmi_range[i]}"
        + " " * spaces_to_add_before_last_pipe
        + "|"
    )

    print("-" * 42)


# Print the bmi classification of the individual
classification = adults_bmi_classification[
    0
]  # The index in the adult_bmi_classification list

if adult_bmi < 16:
    classification = adults_bmi_classification[0]
elif adult_bmi < 17:
    classification = adults_bmi_classification[1]
elif adult_bmi < 18.5:
    classification = adults_bmi_classification[2]
elif adult_bmi < 25:
    classification = adults_bmi_classification[3]
elif adult_bmi < 30:
    classification = adults_bmi_classification[4]
elif adult_bmi < 35:
    classification = adults_bmi_classification[5]
elif adult_bmi < 40:
    classification = adults_bmi_classification[6]
else:
    classification = adults_bmi_classification[7]


message = f"\nYour bmi is {adult_bmi:.2f}, you have {classification}."
print(message)
