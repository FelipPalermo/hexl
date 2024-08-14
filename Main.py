from typing import Type, overload, List, Union
from random import randint 

class hex_functions : 

    """
    A class for working with hexadecimal numbers
    There is no need to create instances off this class 

    Attributes : 
        This class dont have attributes 

    Functions : 
        hex_sum(value : int, hex_len : int)  : 
            The value will be used in the equation with the hex_len to return the result 
            returns : One int value result of the equatiion
        
        alpha_to_hex(values : str) : 
            convert alphabetical characters (A...F) in hexadecimal values 
            returns : a list with the corresponding values of the characters in int 
        
        generate_hex_ID() : 
            generate 8 digits random hexadecimal ID 
            returns : 8 digts hexadecimal string | example : "A12FFBD0" 

        hex_to_dec(values : str) : 
            use the values variable to convert and sum hexadecimal values 
            retunrs : hexadecimal converted decimal system 
    """



    @staticmethod 
    def hex_sum(value : int, hex_len : int) -> int: 
        """
        Uses value (0 - 9) digits an hex_len to convert to decimal 
        using | value * 16 ^ hex_len | notation 

        Args : 
            Value (int) : Principal value that will be used in the equation
            hex_len (int) : value that will be used to determine the power in equation

        Returns : 
            Real decimal value of the number 
        """
        result = value * 16  ** hex_len 

        return result 


    @staticmethod
    def alpha_to_hex(values : str) -> List[int] : 
        """
        Convert alphabetic type to int type 

        Args : 
            values (str) : string, can contain numbers and letters, only letters will be converted
        
        Returns :  
            List[int] with the new values   
        """
        inverse_hex_map = {
           "F": "15",
           "E": "14",
           "D": "13",
           "C": "12",
           "B": "11",
           "A": "10" 
    }

        HEX_LIST : List[str] = []

        for i in values.upper() : 
            HEX_LIST.append(i)

        HEX_LIST = [inverse_hex_map.get(var,var) for var in HEX_LIST]


        HEX_LIST = [int(var) for var in HEX_LIST]

        return HEX_LIST



    @staticmethod    
    def generate_hex_ID() : 
        """
        Generate random HEX number in a range with 8 positions 

        Args : 
            do not use args in this function

        Returns : 
            8 digit hexadecimal string 
        """
        ID : List[str] = [str(randint(1,15)) for _ in range(0, 8) ] 

        hex_map = {
            "15": "F",
            "14": "E",
            "13": "D",
            "12": "C",
            "11": "B",
            "10": "A"
        } 

        ID = [
            hex_map.get(var, var) for var in ID 
        ]

        return ''.join(ID) 


    @staticmethod
    def hex_to_dec(values : str) -> int : 
        """
        Return the real sum of entire Hexadecimal string 

        Args : 
            Values (str) : recive a str that contains the hexadecimal ID

        Returns : 
            The sum of values (Hexadecimal) casted as int 
        """
        hex_id = []
        hex_id_len = len(values)

        for i in values :  
            hex_id_len -= 1 
            if i.isalpha() and i in ["A", "B", "C", "D", "E", "F"]: 
                holder = hex_functions.alpha_to_hex(i)
                hex_id.append(hex_functions.hex_sum(int(holder[0]), hex_id_len))


            elif i.isdigit() : 
                hex_id.append(hex_functions.hex_sum(int(i), hex_id_len))

            else : 
                raise TypeError(f"Invalid value : {i}")
            
        return sum(hex_id)


class ID : 

    """ 
    ID contains a Unique hexadecimal ID that can be iterated, compared and summed 
    
    Attributes : 
        HEX_ID (str) = None, this value can be None for a new random ID, or 8 digit string

    Functions : 
        __init__(self, HEX_ID : str) : 
            create a instance of the class with ID and hexadecimal maps 
        
        exoteric_ID_sum(self, HEX_ID (str)) : 
            Esoteric function that sum 2 hexadecimal ID's 
    """

    def __init__(self, HEX_ID : str = None ) : 

        """
        Create a instance of ID, if no arguments it will create a random 8 digit ID
        and then load the hexadecimal maps 

        Args : 
            HEX_ID (str) = None, this value can be None for a new random ID, or 8 digit string 
        
        Returns : 
            Nothing
        """

        if HEX_ID is None : 
            self.ID = hex_functions.generate_hex_ID() 

        elif len(HEX_ID) == 8 and isinstance(HEX_ID, str) : 
            self.ID = HEX_ID
        
        else : 
            raise AttributeError("Incorrect format, please use 8 digit hexadecimal notation")

        self.inverse_hex_map = {
        "F": "15",
        "E": "14",
        "D": "13",
        "C": "12",
        "B": "11",
        "A": "10" 
    } 
        self.hex_map = {
        "15": "F",
        "14": "E",
        "13": "D",
        "12": "C",
        "11": "B",
        "10": "A"
    }
    
    def esoteric_ID_sum(self, HEX_ID) : 

        """ 
        Esoteric function for summing two IDs. 
        This function is considered esoteric because the sum does not yield real values; 
        it is merely a representation of a function that is under construction.

        Args : 
            HEX_ID, hexadecimal ID that will be used to sum with the original class ID 

        Returns : 
            Sum of the two hexadecimal id's 
        """

        # HEX TO BASE 10
        self.ID = [ self.inverse_hex_map.get(hmap, hmap) for hmap in self.ID ] 
        # STR TO INT 
        self.ID = [int(var) for var in self.ID] 

        # Hex to base 10 
        HEX_ID = [ self.inverse_hex_map.get(var, var) for var in HEX_ID ]
        # STR to int  
        HEX_ID = [ int(var) for var in HEX_ID ]

        # zip 2 lists
        self.ID = [a + b for a,b in zip(self.ID, HEX_ID)]
        
        # BACK TO STR 
        self.ID = [ str(var) for var in self.ID ]
        # BACK TO HEX 
        self.ID = [ self.hex_map.get(var, var) for var in self.ID ]

        return self.ID 

    def __str__(self) : 
        return ''.join(self.ID)

    def __int__(self) : 
        return hex_functions.hex_to_dec(self.ID)

    def __len__(self) -> int : 
        return len(self.ID)

    def __iter__(self) : 
        return iter(self.ID)  


id_number = hex_functions.generate_hex_ID()
ID1 = ID(id_number)
print(int(ID1))

z = ID1.esoteric_ID_sum(hex_functions.generate_hex_ID())
print(z)