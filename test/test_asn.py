from translate.asn_translate import colorize_ascii_art
import unittest
import filecmp


"""Тестирование"""
class TestAsnArt(unittest.TestCase):
    """Класс, отвечающий за тестирование asn арта"""
    def test_one_file(self):
        file1 = 'save_ascii.txt'
        file2 = 'save_ascii.txt'

        asn_file1 = colorize_ascii_art(file1, 'output1.asn')
        asn_file2 = colorize_ascii_art(file2, 'output2.asn')

        self.assertTrue(filecmp.cmp(asn_file1, asn_file2))
