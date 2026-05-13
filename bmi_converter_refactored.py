import json
from pathlib import Path

ADULTS_BMI_FILEPATH = "adults_bmi_classification.txt"
TEENS_BMI_FILEPATH = "teens_or_child_bmi_classification.txt"


def compute_bmi(weight: float, height: float) -> float:
    """
    Take weight and height as parameters.
    Compute the bmi using the formula weight / height**2.
    Return the computed value.
    """
    return weight / height**2


def user_is_an_adult() -> bool:
    """
    Prompt a question to the user asking if the user is an adult.
    Return boolean values True or False.
    """
    answer = ""
    valid_answers = ["y", "yes", "n", "no"]

    while answer not in valid_answers:
        answer = input("\nAre you an adult? (y or n) ").strip().lower()

    if answer in valid_answers[:2]:
        return True

    return False


def ask_weight_and_height() -> tuple[float, float]:
    """
    Ask the user his weight and height.
    Return the two values provided.
    """
    invalid_number = True

    while invalid_number:
        weight = input("\nEnter your weight in kilograms: ")
        height = input("\nEnter your height in cm: ")

        try:
            weight = float(weight)
            height = float(height)
            invalid_number = False

        except ValueError:
            print("Your weight and height should be valid numbers.")

    return weight, height


def safely_load_file(filepath: str) -> dict | None:
    """
    Load a file using the filepath provided
    Return a dictionary if successfull
    Return a msg otherwise
    """
    try:
        path = Path(filepath)
        data = path.read_text()
        contents = json.loads(data)
        return contents
    except FileNotFoundError:
        print("\nThe path provided is not correct.")


def match_adult_bmi_classification(filename: str, bmi: float) -> tuple[str, str]:
    """Return a string of the matching bmi classification."""
    data = safely_load_file(filename)
    pairs = []
    if data is not None:
        for k, v in data.items():
            pairs.append((k, v))

        if bmi < 16:
            return pairs[0][0], pairs[0][1]
        elif bmi < 17:
            return pairs[1][0], pairs[1][1]
        elif bmi < 18.5:
            return pairs[2][0], pairs[2][1]
        elif bmi < 25:
            return pairs[3][0], pairs[3][1]
        elif bmi < 30:
            return pairs[4][0], pairs[4][1]
        elif bmi < 35:
            return pairs[5][0], pairs[5][1]
        elif bmi < 40:
            return pairs[6][0], pairs[6][1]
        else:
            return pairs[7][0], pairs[7][1]

    else:
        return "", ""


def match_teens_bmi_classification(filename: str, bmi: float) -> tuple[str, str]:
    """Return a string of the matching bmi classification."""
    data = safely_load_file(filename)
    pairs = []
    if data is not None:
        for k, v in data.items():
            pairs.append((k, v))

        if bmi < 5:
            return pairs[0][0], pairs[0][1]
        elif bmi < 85:
            return pairs[1][0], pairs[1][1]
        elif bmi < 95:
            return pairs[2][0], pairs[2][1]
        else:
            return pairs[3][0], pairs[3][1]
    else:
        return "", ""


def get_bmi_classification() -> None:
    """Get the BMI classification of the user."""
    weight, height = ask_weight_and_height()
    bmi = compute_bmi(weight, height)

    if user_is_an_adult():
        (classif, bmi_range) = match_adult_bmi_classification(ADULTS_BMI_FILEPATH, bmi)
    else:
        (classif, bmi_range) = match_teens_bmi_classification(TEENS_BMI_FILEPATH, bmi)

    show_bmi_infos(classif, bmi)


def show_bmi_infos(classif: str, bmi: float) -> None:
    """Print a sentence about the BMI of the user."""
    print(f"\nYour bmi is {bmi:.2f}, you have {classif}.")


get_bmi_classification()
