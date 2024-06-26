import unittest
"""Модуль, который отвечает за заупуск тестов"""
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(
        start_dir='./test/',
        pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
