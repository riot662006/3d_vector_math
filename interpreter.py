from typing import *
from decimal import Decimal # for precise calculations

variables = {}

def load_variables():
    global variables
    variables = {}

    with open("variables.txt", "r") as file:
        # reads the variable text file line by line
        for _var_args in file:
            var_args = _var_args.split()

            if len(var_args) != 4:
                raise MemoryError(f"Error in variable.txt: should have 4 arguments in line '{_var_args}'")

            # the first argument is the variable name and the remaining are the i, j, k components
            var_name = var_args[0]
            components = [Decimal(comp) for comp in var_args[1:]]

            variables[var_name] = components

def store_variables():
    with open("variables.txt", "w") as file:
        for var_name, components in variables.items():
            var_args = var_name + " " + " ".join([str(comp) for comp in components]) + "\n"
            file.write(var_args)

def not_in_range_throws(arguments: Iterable, left_bound: int, right_bound: int) -> Iterable:
    """
    Checks if the length of an array is in the provided bounds. Raises an exception if the range is invalid.

    Parameters:
    - arguments (Iteratable): Array to check
    - left_bound (int): The lower boundary of the range.
    - right_bound (int): The upper boundary of the range (not inclusive).

    Returns:
    - None: This function does not return a value.

    Raises:
    - ValueError: If the left_bound is greater than or equal to right_bound.
    """
    if len(arguments) < left_bound or len(arguments) >= right_bound:
        raise ValueError(f"Invalid arguments. Expected to be in range ({left_bound}, {right_bound}). got {len(arguments)}")

    return arguments

def get_variable(var_name: str, component: str = 'ijk') -> None:
    """
    Gets the components of variable `var_name`.

    Parameters:
    - var_name (str): The name of the variable.
    - component (str): Specific components to get.

    Returns:
    - None: This function does not return a value.
    """
    var_components = variables[var_name]
    to_print = []

    for c in component:
        to_print.append("")

        if c not in 'ijkxyz':
            raise SyntaxError(f"At argument, no component named '{c}'")
        
        if c in 'ix':
            to_print[-1] += str(var_components[0])
        
        if c in 'jy':
            to_print[-1] += str(var_components[1])

        if c in 'kz':
            to_print[-1] += str(var_components[2])

    print(f"<{", ".join(to_print)}>")


def interprete(keyword: str, *args: list[str]) -> None:
    """
    Interprets the given keyword and arguments.

    Parameters:
    - keyword (str): The keyword to interpret.
    - args (list[str]): A list of arguments associated with the keyword.

    Returns:
    - None: This function does not return a value.
    """
    match(keyword):
        case "get":
            get_variable(*not_in_range_throws(args, 1, 3))
        case _:
            raise SyntaxError(f"Invalid keyword: '{keyword}'")



def run():
    """
    Runs an interpreter instance
    """
    # loads the variables
    load_variables()

    while (True):
        # nothing right now
        input_line = input("> ")
        interprete(*input_line.split())
        break

    # stores variables for next run
    store_variables()