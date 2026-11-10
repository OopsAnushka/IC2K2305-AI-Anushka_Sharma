
"""
Experiment 2: Production Rule System
Author: Anushka Sharma
Roll No: IC-2K23-12
"""


def production_system():
    # Working memory: initial facts
    facts = {
        "temperature": 32,
        "person_present": True,
        "fan_on": False,
        "window_open": False
    }

    # Production rules
    rules = [
        (
            "Turn ON fan",
            lambda f: (
                f["temperature"] > 28
                and f["person_present"]
                and not f["fan_on"]
            ),
            lambda f: f.update({"fan_on": True})
        ),
        (
            "Open window",
            lambda f: (
                f["temperature"] > 30
                and not f["window_open"]
            ),
            lambda f: f.update({"window_open": True})
        )
    ]

    print("PRODUCTION RULE SYSTEM")
    print("-" * 35)

    print("Initial Facts:", facts)

    # Apply rules until no more rules can execute
    while True:
        rule_fired = False

        for rule_name, condition, action in rules:

            if condition(facts):
                print("\nRule Applied:", rule_name)

                action(facts)

                rule_fired = True
                break

        if not rule_fired:
            break

    print("\nFinal Facts:", facts)


if __name__ == "__main__":
    production_system()
