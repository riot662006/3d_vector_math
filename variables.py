from typing import *
from vector import Vector

variables: dict[str, Vector] = {}

# constants that should not have variables
constants: dict[str, Vector] = {
    # important unit vectors
    "i": Vector(1, 0, 0),
    "j": Vector(0, 1, 0),
    "k": Vector(0, 0, 1),

    # temp vector
    "_": Vector(0, 0, 0)
}

def invalid_variable_name_throws(var_name: str) -> str:
    """
    Checks if the given variable name is valid. Returns the same variable name if it is valid,
    otherwise raises an error with a message.

    Parameters:
    - var_name (str): The name of the variable to check.

    Returns:
    - str: The same variable name if it is valid.

    Raises:
    - ValueError: If the variable name is invalid.
    """
    if var_name in constants:
        raise ValueError(f"Invalid variable name: '{var_name}' is a constant. Cannot set it.")

    # should not have any invalid characters (arithmetic characters)
    invalid_characters = set("+-*/%&|^!~<>=()[]{}")
    if any(c in invalid_characters for c in var_name):
        raise ValueError(f"Invalid variable name: '{var_name}' contains invalid characters.")
    
    return var_name

def load_vars():
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

                set_var(var_name, Vector(*var_args[1:]))
    except FileNotFoundError:
        # creates variable.text
        with open("variables.txt", "x") as file:
            pass

def store_vars():
    with open("variables.txt", "w") as file:
        for var_name, vector in variables.items():
            file.write(f"{var_name} {vector.to_storable()}\n")

def get_var(var_name: str) -> Vector:
    """
    Get the vector with variable name `var_name`

    Parameters:
    - var_name (str): Variable name  
    """
    if var_name in constants:
        return constants[var_name]

    if var_name in variables:
        return variables[var_name]
    
    raise KeyError(f"Variable '{var_name}' does not exist")

def set_var(var_name: str, vector: Vector) -> None:
    """
    Sets the vector into variable name `var_name` if it is valid

    Parameters:
    - var_name (str): Variable name
    - vector (Vector): vector to be stored
    """

    var_name = invalid_variable_name_throws(var_name)

    variables[var_name] = vector