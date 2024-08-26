import numpy as np

class Mato:
    """MATOOOO"""
    def __init__(self, file: str):
        """
        Initialize the Mato

        Parameters
        ----------
        file : str
            File to set
        """
        self.file = file
    def print(self):
        """
        Print the Mato file

        """
        print(self.file)
    def add1(self, num):
        """

        Add 1 to the num

        Parameters
        ----------
        num : int
            Number to add
        """
        return num + 1
