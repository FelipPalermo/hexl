from typing import List, Union
from hex_functions import hex_functions
from random import randint

class hexl : 
    """ 
    ID contains a Unique hexadecimal ID that can be iterated, compared and summed. 
    
    Attributes : 
        hexl_ID (str) = None, this value can be None for a new random ID, or 8 digit string.

    Functions : 
        __init__(self, hexl_ID : str) : 
            create a instance of the class with ID and hexadecimal maps. 
        
        generate_hex : 
                    generate 8 digits random hexadecimal ID 
                    returns : 8 digts hexl instance | example : "A12FFBD0". 

        to_hex : 
            use the values variable to convert and sum hexadecimal values 
            retunrs : hexl instance. 
    """

    @staticmethod
    def _convert_to_hex(values : Union[str, int]) -> str : 
        """
        This function follows a convention to avoid infinite recursion 
        and should not be used.
        A better solution should be applyed, but until i find a solution, that will work.
        """
        try :  
            return hex_functions.dec_to_hex(hex_functions.dec_hex_equation(values))

        except Exception as err : 

            if isinstance(values, str) :

                values = hex_functions.to_dec(values)
                return hex_functions.dec_to_hex(hex_functions.dec_hex_equation(values))

            else : 
                raise AttributeError(f"Type erro : {err} ")

    def __init__(self, hex = None ) : 

        """
        Create a instance of ID, if no arguments it will create a random 8 digit ID
        and then load the hexadecimal maps.

        Args : 
            hexl_ID = None, this value can be None for a new random ID, or 8 digit string 
            also, the value can be int or string.
        
        Returns : 
            hexl instance. 
        """

        if  isinstance(hex, str) or isinstance(hex, int): 
            self.ID = hexl._convert_to_hex(hex) 

        else : 
            self.ID = hexl.generate_hex() 

    @staticmethod
    def to_hex(values : Union[str, int]) -> str : 
        """
            Decimal to hexadecimal. This function merge dex_hex_equation and dec_to_hex, to create
                                    a simplified and secure version.
            
            args : 
                values : str, or int, will be used to cast to hexadecimal. 

            returns : 
                str : String representation of previous number.
        """
    
        try :  
            return hexl(hex_functions.dec_to_hex(hex_functions.dec_hex_equation(values)))

        except Exception as err : 

            if isinstance(values, str) :

                values = hex_functions.to_dec(values)
                return hexl(hex_functions.dec_to_hex(hex_functions.dec_hex_equation(values)))

            else : 
                raise AttributeError(f"Type erro : {err} ")

    @staticmethod    
    def generate_hex() -> "hexl" : 
        """
        Generate random hexl number in a range with 8 positions. 

        Args : 
            do not use args in this function.

        Returns : 
            8 digit hexadecimal string. 
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

        return hexl(''.join(ID))

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
        return hex_functions.to_dec(self.ID)

    def __len__(self) -> int : 
        return len(self.ID)

    def __eq__(self, hex : str) -> bool: 
        return str(self.ID) == hex 
    
# /// ----- math methods ----- ///
    def __add__(self, value: Union[int, str]) -> "hexl":
        new_hexl = hex_functions.to_dec(str(self.ID)) + int(value)
        return hexl(new_hexl)

    def __sub__(self, value: Union[int, str]) -> "hexl":
        new_hexl = hex_functions.to_dec(str(self.ID)) - int(value)
        return hexl(new_hexl)

    def __mul__(self, value: int) -> "hexl":
        new_hexl = hex_functions.to_dec(self.ID) * value
        return hexl(new_hexl)

    def __pow__(self, value: int) -> "hexl":
        new_hexl = hex_functions.to_dec(self.ID) ** value
        return hexl(new_hexl)

    def __floordiv__(self, value: int) -> "hexl":
        new_hexl = hex_functions.to_dec(self.ID) // value
        return hexl(new_hexl)

    def __truediv__(self, value: int) -> "hexl":
        new_hexl = hex_functions.to_dec(self.ID) / value
        return hexl(new_hexl)

# /// ----- reflexive methods ----- ///
    def __radd__(self, value: Union[int, str]) -> "hexl":
        return self.__add__(value)

    def __rsub__(self, value: Union[int, str]) -> "hexl":
        return self.__sub__(value)

    def __rmul__(self, value: int) -> "hexl":
        return self.__mul__(value)

    def __rpow__(self, value: int) -> "hexl":
        return self.__pow__(value)

    def __rfloordiv__(self, value: int) -> "hexl":
        return self.__floordiv__(value)

    def __rtruediv__(self, value: int) -> "hexl":
        return self.__truediv__(value)

# /// ----- comparasion methods ----- /// 
    def  __le__(self, other) -> bool : 
        if isinstance(other, int) : 
            return hex_functions.to_dec(self.ID) <= int(other)

        elif isinstance(other, hexl):
            return hex_functions.to_dec(self.ID) <= hex_functions.to_dec(other) 

    def  __lt__(self, other) -> bool : 
        if isinstance(other, int) : 
            return hex_functions.to_dec(self.ID) < int(other)

        elif isinstance(other, hexl):
            return hex_functions.to_dec(self.ID) < hex_functions.to_dec(other) 

    def  __ge__(self, other) -> bool : 
        if isinstance(other, int) : 
            return hex_functions.to_dec(self.ID) >= int(other)

        elif isinstance(other, hexl):
            return hex_functions.to_dec(self.ID) >= hex_functions.to_dec(other) 

    def  __gt__(self, other) -> bool : 
        if isinstance(other, int) : 
            return hex_functions.to_dec(self.ID) > int(other)

        elif isinstance(other, hexl):
            return hex_functions.to_dec(self.ID) > hex_functions.to_dec(other) 

    def __hash__(self) -> int : 
        return hash(self.ID)