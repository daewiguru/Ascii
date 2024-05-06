from translate.translate import save_ascii_art
import unittest
import filecmp
"""Тестирование"""
class TestAsciiFile(unittest.TestCase):
    """Класс, овтечающий за тестирование"""
    def test_one_image(self):
        file1 = 'test.jpg'
        file2 = 'test.jpg'

        ascii_file1 = save_ascii_art(file1, 'ascii_save1.txt')
        ascii_file2 = save_ascii_art(file2, 'ascii_save2.txt')
        
        compare = filecmp.cmp(ascii_file1, ascii_file2)
        self.assertTrue(compare)
