import unittest
from models import Operands

class TestOperands(unittest.TestCase):
    def test_init(self):
        operands = Operands(5, 10)
        self.assertEqual(operands.first_operand, 5)
        self.assertEqual(operands.second_operand, 10)

if __name__ == '__main__':
    unittest.main()