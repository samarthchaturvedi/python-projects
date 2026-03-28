# K-Map Solver (2–4 Variables)
# Author: Samarth Chaturvedi
# Description:
# This program simplifies Boolean expressions using logic minimization.
# It uses SymPy library to simulate Karnaugh Map simplification.

from sympy import symbols, simplify_logic
from sympy.logic.boolalg import SOPform

def get_variables(n):
    """Generate variable symbols based on number of variables"""
    if n == 2:
        return symbols('A B')
    elif n == 3:
        return symbols('A B C')
    elif n == 4:
        return symbols('A B C D')
    else:
        print("Only 2–4 variables supported.")
        return None

def main():
    print("\n🔷 K-Map Solver (2–4 Variables)\n")

    n = int(input("Enter number of variables (2–4): "))
    variables = get_variables(n)

    if variables is None:
        return

    print("\nEnter minterms (space-separated, e.g., 1 3 5):")
    minterms = list(map(int, input("Minterms: ").split()))

    print("\nEnter don't care terms (optional, press enter to skip):")
    dc_input = input("Don't cares: ")

    dont_cares = list(map(int, dc_input.split())) if dc_input else []

    # Simplify using SOP form (Sum of Products)
    simplified_expr = SOPform(variables, minterms, dont_cares)

    print("\n✅ Simplified Expression:")
    print(simplified_expr)


if __name__ == "__main__":
    main()