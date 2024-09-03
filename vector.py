from decimal import Decimal # for precise calculations
from typing import Union
from math import sqrt

class Vector:
    def __init__(self, i: Union[int, float, str, Decimal], j: Union[int, float, str, Decimal], k: Union[int, float, str, Decimal]) -> None:
        """
        Initializes a 3D vector with the given components.

        Parameters:
        - i (Union[int, float, str, Decimal]): The x-component of the vector.
        - j (Union[int, float, str, Decimal]): The y-component of the vector.
        - k (Union[int, float, str, Decimal]): The z-component of the vector.
        """
        self.i = Decimal(str(i))
        self.j = Decimal(str(j))
        self.k = Decimal(str(k))

    def __repr__(self) -> str:
        return f"Vector({self.i}, {self.j}, {self.k})"
    
    def to_storable(self) -> str:
        """Gets the storable version of the vector"""
        return f"{str(self.i)} {str(self.j)} {str(self.k)} "

    def __add__(self, other: 'Vector') -> 'Vector':
        """Adds two vectors."""
        return Vector(str(self.i + other.i), str(self.j + other.j), str(self.k + other.k))

    def __sub__(self, other: 'Vector') -> 'Vector':
        """Subtracts two vectors."""
        return Vector(self.i - other.i, self.j - other.j, self.k - other.k)

    def dot(self, other: 'Vector') -> Decimal:
        """Computes the dot product of two vectors."""
        return self.i * other.i + self.j * other.j + self.k * other.k

    def magnitude(self) -> Decimal:
        """Computes the magnitude of the vector."""
        return sqrt(self.i**2 + self.j**2 + self.k**2)

    def __eq__(self, other: 'Vector') -> bool:
        """Checks if two vectors are equal."""
        return (self.i == other.i) and (self.j == other.j) and (self.k == other.k)
    
    def __getitem__(self, key: int | str) -> Decimal:
        """
        Allows indexing into the vector to get components.

        Parameters:
        - key (int | str): The index of the component to retrieve (0, 'i', or 'x' for i; 1, 'j' or 'y' for j; 2, 'k' or 'z' for k).

        Returns:
        - Decimal: The component at the specified index.

        Raises:
        - IndexError: If the index is out of range.
        """
        key = str(key)

        if key in '0ix':
            return self.i
        elif key in '1jy':
            return self.j
        elif key in '2kz':
            return self.k
        else:
            raise KeyError(f"Invalid key. No component for '{key}'")

    def __setitem__(self, key: int | str, value: Union[int, float, str, Decimal]) -> None:
        """
        Allows indexing into the vector to set components.

        Parameters:
        - index (int | str): The index of the component to set (0 for i, 1 for j, 2 for k).
        - value (Union[int, float, str, Decimal]): The new value to set the component to.

        Returns:
        - None: This function does not return a value.

        Raises:
        - IndexError: If the index is out of range.
        """
        key = str(key)
        decimal_value = Decimal(str(value))

        if key in '0ix':
            self.i = decimal_value
        elif key in '1jy':
            self.j = decimal_value
        elif key in '2kz':
            self.k = decimal_value
        else:
            raise KeyError(f"Invalid key. No component for '{key}'")
