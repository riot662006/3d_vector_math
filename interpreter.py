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

def run():
    # loads the variables
    load_variables()

    while (True):
        # nothing right now
        break

    # stores variables for next run
    store_variables()