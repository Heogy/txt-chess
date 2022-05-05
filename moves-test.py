import moves
import unittest

class TestMoves(unittest.TestCase):

    def test_e4(self):
        self.assertTrue(moves.is_valid_move("e4"))

if __name__ == '__main__':
    unittest.main()
