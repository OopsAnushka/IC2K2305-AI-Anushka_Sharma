
"""
Experiment 1: AI Environment Setup
Author: Anushka Sharma
Roll No: IC-2K23-12
"""

import sys
import platform
import importlib.util


def check_python():
    """Display Python and operating system information."""
    print("AI DEVELOPMENT ENVIRONMENT")
    print("-" * 40)

    print("Python Version:", sys.version.split()[0])
    print("Operating System:", platform.system())
    print("System Architecture:", platform.machine())


def check_libraries():
    """Check availability of common AI libraries."""

    libraries = [
        "numpy",
        "pandas",
        "matplotlib",
        "sklearn",
        "jupyter",
        "torch"
    ]

    print("\nLIBRARY STATUS")
    print("-" * 40)

    for library in libraries:
        if importlib.util.find_spec(library):
            print(library, ": Installed")
        else:
            print(library, ": Not Installed")


def main():
    check_python()
    check_libraries()

    print("\nEnvironment verification completed.")


if __name__ == "__main__":
    main()
