import fen
import unittest

class TestFen(unittest.TestCase):

    def test_start_position(self):
        state = fen.read("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.assertTrue('board' in state)
        self.assertEqual(state['next'], 'white')
        self.assertEqual(state['castles'], ['K','Q','k','q'], "all can castle at start position")
        self.assertEqual(state['en_passant'], '')
        self.assertEqual(state['halfmove_clock'], 0)
        self.assertEqual(state['fullmove_number'], 1)

    def test_king_opening_position(self):
        state = fen.read("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1")
        self.assertTrue('board' in state)
        self.assertTrue(state['next'] == 'black')
        self.assertEqual(state['castles'], ['K','Q','k','q'], "all can castle at start position")
        self.assertEqual(state['en_passant'], 'e3')
        self.assertEqual(state['halfmove_clock'], 0)
        self.assertEqual(state['fullmove_number'], 1)
        
    def test_no_castles(self):
        self.assertEqual([], fen.read_castle('-'))

if __name__ == '__main__':
    unittest.main()
