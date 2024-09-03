from typing import *
from vector import Vector

variables: dict[str, Vector] = {}

def load_variables():
    global variables
    variables = {}

    try:
        with open("variables.txt", "r") as file:
            # reads the variable text file line by line
            for _var_args in file:
                var_args = _var_args.split()

                if len(var_args) != 4:
                    raise MemoryError(f"Error in variable.txt: should have 4 arguments in line '{_var_args}'")

                # the first argument is the variable name and the remaining are the i, j, k components
                var_name = var_args[0]

                variables[var_name] = Vector(*var_args[1:])
    except FileNotFoundError:
        # creates variable.text
        with open("variables.txt", "x") as file:
            pass

def store_variables():
    with open("variables.txt", "w") as file:
        for var_name, vector in variables.items():
            file.write(f"{var_name} {vector.to_storable()}\n")

def not_in_range_throws(arguments: Iterable[Any], left_bound: int, right_bound: int | float) -> Iterable:
    """
    Checks if the length of an array is in the provided bounds. Raises an exception if the range is invalid.

    Parameters:
    - arguments (Iteratable): Array to check
    - left_bound (int): The lower boundary of the range.
    - right_bound (int | float): The upper boundary of the range (not inclusive).

    Returns:
    - Iterable: This function return the inputed argument

    Raises:
    - ValueError: If argument not in range.
    """
    if len(arguments) < left_bound or len(arguments) >= right_bound:
        raise ValueError(f"Invalid arguments. Expected to be in range ({left_bound}, {right_bound}). got {len(arguments)}")

    return arguments

def not_exact_length_throws(arguments: Iterable[Any], valid_lengths: Union[int, List[int]]) -> Iterable:
    """
    Checks if the length of arguments is exactly one of the valid lengths.

    Parameters:
    - arguments (Iterable[Any]): The collection of arguments to check.
    - valid_lengths (Union[int, List[int]]): The valid lengths. Can be a single integer or a list of integers.

    Returns:
    - Iterable: This function return the inputed argument

    Raises:
    - ValueError: If the length of arguments is not one of the valid lengths.
    """
    if isinstance(valid_lengths, int):
        valid_lengths = [valid_lengths]

    if len(arguments) not in valid_lengths:
        raise ValueError(f"Invalid arguments. Expected length to be in {valid_lengths}. got {len(arguments)}")
    
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
    vector = variables[var_name]
    to_print = []

    for c in component:
        to_print.append(str(vector[c]))

    print(f"<{", ".join(to_print)}>")

def set_variable(var_name: str, i: str = "0.0", j: str = "0.0", k: str = "0.0") -> None:
    """
    Sets the variable with the given name to the specified string values.

    Parameters:
    - var_name (str): The name of the variable to set.
    - i (str): The x-component value to set as a string.
    - j (str): The y-component value to set as a string.
    - k (str): The z-component value to set as a string.

    Returns:
    - None: This function does not return a value.
    """
    vector = Vector(i, j, k)
    variables[var_name] = vector
    print(f"{var_name} => <{vector.to_storable()}>")

def add_variables(*var_names: str) -> None:
    """
    Adds the specified variables.

    Parameters:
    - var_names (str): Variable names to be added. Multiple variable names can be provided.

    Returns:
    - None: This function does not return a value.
    """
    resultant = Vector(0, 0, 0)

    for var_name in var_names:
        resultant += variables[var_name]

    print(f"Resultant => <{resultant.to_storable()}>")

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
            get_variable(*not_exact_length_throws(args, [1, 2]))
        case "set":
            set_variable(*not_exact_length_throws(args, [1, 3, 4]))
        case "add":
            add_variables(*not_in_range_throws(args, 2, float('inf')))
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