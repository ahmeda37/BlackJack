import unittest
import sys
sys.path.append('..')
from game import helpers
class TestBasic(unittest.TestCase):
	def test_suit(self):
		suit="Hearts"
		result = helpers.Card("Hearts","Two")
		self.assertEqual(result.suit, suit)
	def test_rank(self):
		rank ="Two"
		result = helpers.Card("Hearts", "Two")
		self.assertEqual(result.rank, rank)
	def test_deck(self):
		count = 52
		result = helpers.Deck()
		self.assertEqual(len(result.deck), count)
	

if __name__ == '__main__':
    unittest.main()