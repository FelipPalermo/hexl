from typing import List, Union
from random import randint 
from math import floor

class hfunc : 

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

        to_dec(values : str) : 
            use the values variable to convert and sum hexadecimal values 
            retunrs : hexadecimal converted decimal system 
    """



    @staticmethod 
    def hex_sum(value : int, hex_len : int) -> int: 
        """
        Uses value (0 - 9) digits an hex_len to convert to decimal 
        using | value *  ^ hex_len | notation 

        Args : 
            Value (int) : Principal value that will be used in the equation
            hex_len (int) : value that will be used to determine the power in equation

        Returns : 
            Real decimal value of the number 
        """
        result = value * 16 ** hex_len 

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

        HEX_LIST: List[str] = []

        for i in values.upper() : 
            HEX_LIST.append(i)

        HEX_LIST = [inverse_hex_map.get(var,var) for var in HEX_LIST]


        HEX_LIST = [int(var) for var in HEX_LIST]

        return HEX_LIST


    @staticmethod    
    def generate_hex() -> "ihex" : 
        """
        Generate random ihex number in a range with 8 positions 

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

        return ihex(''.join(ID))


    @staticmethod
    def to_dec(values : str) -> int : 
        """
        Return the real sum of entire Hexadecimal string 

        Args : 
            Values (str) : recive a str that contains the hexadecimal

        Returns : 
            The sum of values (Hexadecimal) casted as int 
        """

        if isinstance(values, int) : 
            pass 

        hex_id = []
        hex_id_len = len(values)

        for i in values :  
            hex_id_len -= 1 
            if i.isalpha() and i in ["A", "B", "C", "D", "E", "F"]: 

                holder = hfunc.alpha_to_hex(i)
                hex_id.append(hfunc.hex_sum(int(holder[0]), hex_id_len))


            elif i.isdigit() : 
                hex_id.append(hfunc.hex_sum(int(i), hex_id_len))

            else : 
                raise TypeError(f"Invalid value : {i}")
            
        return sum(hex_id)

    @staticmethod
    def dec_hex_equation(values: Union[str, int]) -> List[int]:
        """ 
            Use the standard decimal to hex equation to  

            args : 
                value (str, int), variable that will be used in the equation

            returns :  
                A list of integers that represent HEX
        """
        leftover = []

        if isinstance(values, str):
            try:
                values = int(values)
            except ValueError:
                raise ValueError(f"Invalid hexadecimal value: {values}")

        while values > 0:
            mod = values % 16 
            leftover.append(floor(mod))
            values //= 16  

        leftover.reverse()
        return leftover

    @staticmethod
    def dec_to_hex(values : List[int])  -> List[str] :  
        """
            Use list of int to a hexadecimal string 

            args : 
                values (List[int]) used to iterate over it and cast 10 - 15 into A - F values

            returns : 
                str : A string representating the hexadecimal equivalent of the provided int 
        
        """
        
        hex_map = {
            "15": "F",
            "14": "E",
            "13": "D",
            "12": "C",
            "11": "B",
            "10": "A"
        }

        values = [
            str(var) for var in values
        ]

        values = [
            hex_map.get(var, var) for var in values
        ]

        return ''.join(values)
        
    @staticmethod
    def to_hex(values : Union[str, int]) -> str : 
        """
            Decimal to hexadecimal. This function merge dex_hex_equation and dec_to_hex, to create
                                    a simplified and secure version
            
            args : 
                values : str, or int, will be used to cast to hexadecimal 

            returns : 
                str : String representation of previous number
        
        """
    
        try :  
            return ihex(hfunc.dec_to_hex(hfunc.dec_hex_equation(values)))

        except Exception as err : 

            if isinstance(values, str) :

                values = hfunc.to_dec(values)
                return ihex(hfunc.dec_to_hex(hfunc.dec_hex_equation(values)))

            else : 
                raise AttributeError(f"Type erro : {err} ")


class ihex : 

    """ 
    ID contains a Unique hexadecimal ID that can be iterated, compared and summed 
    
    Attributes : 
        ihex_ID (str) = None, this value can be None for a new random ID, or 8 digit string

    Functions : 
        __init__(self, ihex_ID : str) : 
            create a instance of the class with ID and hexadecimal maps 
        
    """

    @staticmethod
    def _convert_to_hex(values : Union[str, int]) -> str : 
        """
        This function follows a convention to avoid infinite recursion 
        and should not be used
        """
        try :  
            return hfunc.dec_to_hex(hfunc.dec_hex_equation(values))

        except Exception as err : 

            if isinstance(values, str) :

                values = hfunc.to_dec(values)
                return hfunc.dec_to_hex(hfunc.dec_hex_equation(values))

            else : 
                raise AttributeError(f"Type erro : {err} ")

    def __init__(self, hex = None ) : 

        """
        Create a instance of ID, if no arguments it will create a random 8 digit ID
        and then load the hexadecimal maps 

        Args : 
            ihex_ID = None, this value can be None for a new random ID, or 8 digit string 
            also, the value can be int or string
        
        Returns : 

            ihex instance 

        """

        if  isinstance(hex, str) or isinstance(hex, int): 
            self.ID = ihex._convert_to_hex(hex) 

        else : 
            self.ID = hfunc.generate_hex() 

# /// -----         ----- ///
# /// ----- Dunders ----- ///
# /// -----         ----- ///

    def __iter__(self) : 
        return iter(self.ID)  

    def __repr__(self) -> str:
        return f"ID ( HEX Value : {self.ID}, DECIMAL Value : \n type : {type(self.ID)}\n len : {len(self.ID)} )"

    def __str__(self) -> str : 
        return ''.join(self.ID)

    def __int__(self) -> int : 
        return hfunc.to_dec(self.ID)

    def __len__(self) -> int : 
        return len(self.ID)

    def __eq__(self, hex : str) -> bool: 
        return str(self.ID) == hex 
    
    def __add__(self, value : Union[int, str]) -> "ihex" : 

        new_ihex = hfunc.to_dec(str(self.ID)) + value
        return hfunc.to_hex(new_ihex)

    def __sub__(self, value : Union[int, str]) -> "ihex" : 

        new_ihex = int(hfunc.to_dec(str(self.ID))) - value
        return hfunc.to_hex(new_ihex)

    def __mul__(self, value : int) -> "ihex" : 

        new_ihex = hfunc.to_dec(self.ID) * value
        return ihex(hfunc.to_hex(new_ihex))

    def __pow__(self, value : int) -> "ihex" : 

        new_ihex = hfunc.to_dec(self.ID) ** value 
        return ihex(hfunc.to_hex(new_ihex))


    def __floordiv__(self, value : int) -> "ihex" : 

        new_ihex = hfunc.to_dec(self.ID) / value 
        return ihex(hfunc.to_hex(new_ihex))

    def __truediv__(self, value : int) -> "ihex" : 

        new_ihex = hfunc.to_dec(self.ID) / value 
        return hfunc.to_hex(new_ihex)

    def  __le__(self, other) -> bool : 
        if isinstance(other, int) : 
            return hfunc.to_dec(self.ID) <= int(other)

        elif isinstance(other, ihex):
            return hfunc.to_dec(self.ID) <= hfunc.to_dec(other) 

    def  __lt__(self, other) -> bool : 
        if isinstance(other, int) : 
            return hfunc.to_dec(self.ID) < int(other)

        elif isinstance(other, ihex):
            return hfunc.to_dec(self.ID) < hfunc.to_dec(other) 

    def  __ge__(self, other) -> bool : 
        if isinstance(other, int) : 
            return hfunc.to_dec(self.ID) >= int(other)

        elif isinstance(other, ihex):
            return hfunc.to_dec(self.ID) >= hfunc.to_dec(other) 

    def  __gt__(self, other) -> bool : 
        if isinstance(other, int) : 
            return hfunc.to_dec(self.ID) > int(other)

        elif isinstance(other, ihex):
            return hfunc.to_dec(self.ID) > hfunc.to_dec(other) 

    def __hash__(self) -> int : 
        return hash(tuple(self.ID))



a = hfunc.generate_hex()
a = a + 150
b = a - 50 
c = b * 3
d = c / 2 
e = d ** 2
f = e // 2 
print(a, b, c, d, e, f) 
print(a < 100, a > 100, a <= 100, a >= 100, a == 100)
z = ihex() 
print(a == z, a > z, a < z, a >= z, a <= z)