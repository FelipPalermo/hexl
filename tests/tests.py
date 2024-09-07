import unittest
from hexl import hexl  # Certifique-se de que a classe hexl está no mesmo diretório ou configurada corretamente
from hex_functions import hex_functions

class TestHexl(unittest.TestCase):

    def test_generate_hex(self):
        """Testa se um ID hexadecimal gerado tem 8 dígitos e é uma string"""
        hex_instance = hexl.generate_hex()
        self.assertEqual(len(hex_instance.ID), 8)
        self.assertIsInstance(hex_instance.ID, str)

    def test_hex_conversion(self):
        """Testa se a conversão de decimal para hexadecimal está correta"""
        hex_instance = hexl(255)
        self.assertEqual(str(hex_instance), "FF")

    def test_init_with_hex(self):
        """Testa a criação de uma instância com um valor hexadecimal específico"""
        hex_instance = hexl("A12B34C5")
        self.assertEqual(str(hex_instance), "A12B34C5")

    def test_addition(self):
        """Testa a adição de um valor decimal e hexadecimal"""
        hex_instance = hexl("A12B34C5")
        result = hex_instance + 1
        self.assertEqual(str(result), str(hex_instance + 1))

    def test_subtraction(self):
        """Testa a subtração de um valor decimal e hexadecimal"""
        hex_instance = hexl("A12B34C5")
        result = hex_instance - 1
        self.assertEqual(str(result), str(hex_instance - 1))

    def test_multiplication(self):
        """Testa a multiplicação de um valor decimal"""
        hex_instance = hexl("A12B34C5")
        result = hex_instance * 2
        self.assertEqual(str(result), str(hex_instance * 2))

    def test_power(self):
        """Testa a operação de potência"""
        hex_instance = hexl(2)
        result = hex_instance ** 3
        self.assertEqual(str(result), str(hex_instance ** 3))

    def test_comparisons(self):
        """Testa comparações entre instâncias de hexl"""
        hex1 = hexl("A12B34C5")
        hex2 = hexl("B12B34C5")
        self.assertTrue(hex1 < hex2)
        self.assertTrue(hex2 > hex1)
        self.assertTrue(hex1 <= hex2)
        self.assertTrue(hex2 >= hex1)

    def test_length(self):
        """Testa o tamanho de um ID hexadecimal"""
        hex_instance = hexl("A12B34C5")
        self.assertEqual(len(hex_instance), 8)

    def test_str_representation(self):
        """Testa a representação de string"""
        hex_instance = hexl("A12B34C5")
        self.assertEqual(str(hex_instance), "A12B34C5")

    def test_hash_function(self):
        """Testa se o hash de dois objetos com o mesmo ID é o mesmo"""
        hex1 = hexl("A12B34C5")
        hex2 = hexl("A12B34C5")
        self.assertEqual(hash(hex1), hash(hex2))

if __name__ == "__main__":
    unittest.main()