
"""
Experiment 5: Rule-Based Decision Making
AI Lab - IC-709D

Student Decision Support System using IF-THEN rules.
"""


def get_numeric_input(message, minimum, maximum):
    """Accept and validate numeric input."""

    while True:
        try:
            value = float(input(message))

            if minimum <= value <= maximum:
                return value

            print(
                f"Please enter a value between "
                f"{minimum} and {maximum}."
            )

        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def get_preparation_level():
    """Accept and validate preparation level."""

    while True:
        level = input(
            "Enter preparation level (Low/Medium/High): "
        ).strip().capitalize()

        if level in ("Low", "Medium", "High"):
            return level

        print("Invalid input! Enter Low, Medium, or High.")


def rule_based_decision(marks, attendance, preparation):
    """Apply predefined rules to generate recommendations."""

    facts = {
        "marks": marks,
        "attendance": attendance,
        "preparation": preparation
    }

    # Knowledge Base: Collection of IF-THEN rules
    rules = [
        {
            "name": "R1 - Attendance Rule",
            "condition": facts["attendance"] < 75,
            "recommendation": "Improve attendance to at least 75%."
        },
        {
            "name": "R2 - Low Marks Rule",
            "condition": facts["marks"] < 40,
            "recommendation": "Focus on basic concepts and extra study."
        },
        {
            "name": "R3 - Average Marks Rule",
            "condition": 40 <= facts["marks"] < 70,
            "recommendation": "Practice more questions to improve marks."
        },
        {
            "name": "R4 - Revision Rule",
            "condition": (
                facts["marks"] >= 70
                and facts["preparation"] == "Low"
            ),
            "recommendation": "Revise regularly to strengthen preparation."
        },
        {
            "name": "R5 - Medium Preparation Rule",
            "condition": facts["preparation"] == "Medium",
            "recommendation": "Improve preparation through regular revision."
        },
        {
            "name": "R6 - High Performance Rule",
            "condition": (
                facts["marks"] >= 70
                and facts["preparation"] == "High"
            ),
            "recommendation": "Maintain your performance and continue practicing."
        }
    ]

    matched_rules = []

    print("\nEvaluating Production Rules...")
    print("-" * 50)

    # Inference Engine
    for rule in rules:
        if rule["condition"]:
            matched_rules.append(rule)

            print(f"\nRule Matched: {rule['name']}")
            print(f"THEN: {rule['recommendation']}")

    return matched_rules


def main():
    """Main function."""

    print("=" * 55)
    print("       STUDENT RULE-BASED DECISION SYSTEM")
    print("=" * 55)

    marks = get_numeric_input(
        "Enter student marks (0-100): ", 0, 100
    )

    attendance = get_numeric_input(
        "Enter attendance percentage (0-100): ", 0, 100
    )

    preparation = get_preparation_level()

    print("\nStudent Information:")
    print(f"Marks: {marks}%")
    print(f"Attendance: {attendance}%")
    print(f"Preparation Level: {preparation}")

    recommendations = rule_based_decision(
        marks,
        attendance,
        preparation
    )

    print("\n" + "=" * 55)
    print("              FINAL DECISION")
    print("=" * 55)

    if recommendations:
        print(f"Total Rules Matched: {len(recommendations)}")

        for index, rule in enumerate(recommendations, start=1):
            print(f"{index}. {rule['recommendation']}")

    else:
        print("No specific recommendation required.")

    print("\nDecision Process Completed.")


if __name__ == "__main__":
    main()
