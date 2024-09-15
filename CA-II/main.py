
import sympy as sp

def parse_equation(equation_str):
    """
    Parse a given mathematical equation string into a symbolic equation.
    """
    equation = sp.sympify(equation_str)
    return equation



def ask_for_inputs(variables):
    """
    Ask the user for input values for each variable in the equation.
    """
    inputs = {}
    for var in variables:
        value = float(input(f"Enter the value for {var}: "))
        inputs[var] = value
    return inputs


def solve_equation(equation, inputs):
    """
    Substitute the inputs into the equation and solve it.
    
    """
    result = equation.subs(inputs)
    return result

def main():
    equation_str = input("Enter the mathematical equation (e.g., 2*x + 3*y - z): ")
    equation = parse_equation(equation_str)

    variables = equation.free_symbols
    inputs = ask_for_inputs(variables)

    result = solve_equation(equation, inputs)
    print(f"The result of the equation is: {result}")
    

if __name__ == "__main__":
    main()
