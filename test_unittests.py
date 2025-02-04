import unittest   # The test framework
from card_ranking_checks import *

poker_hand_examples = {
    "Royal Flush": [('T', 'H'), ('J', 'H'), ('Q', 'H'), ('K', 'H'), ('A', 'H')],
    "Straight Flush": [('5', 'S'), ('6', 'S'), ('7', 'S'), ('8', 'S'), ('9', 'S')],
    "Four of a Kind": [('A', 'H'), ('A', 'D'), ('A', 'S'), ('A', 'C'), ('K', 'H')],
    "Full House": [('Q', 'H'), ('Q', 'D'), ('Q', 'S'), ('J', 'H'), ('J', 'D')],
    "Flush": [('2', 'H'), ('6', 'H'), ('9', 'H'), ('J', 'H'), ('K', 'H')],
    "Straight": [('4', 'C'), ('5', 'D'), ('6', 'S'), ('7', 'H'), ('8', 'C')],
    "Three Of A Kind": [('9', 'H'), ('9', 'D'), ('9', 'S'), ('J', 'C'), ('K', 'D')],
    "Two Pair": [('J', 'H'), ('J', 'C'), ('8', 'S'), ('8', 'D'), ('K', 'H')],
    "Pair": [('6', 'H'), ('6', 'C'), ('9', 'D'), ('J', 'S'), ('A', 'H')],
    "High Card": [('2', 'H'), ('5', 'D'), ('8', 'S'), ('J', 'C'), ('K', 'H')],
}

class Test(unittest.TestCase):
    # def test_increment(self):
    #     self.assertEqual(3, 3)

    # # This test is designed to fail for demonstration purposes.
    # def test_decrement(self):
    #     self.assertFalse(False)
    def test_has_ace(self):
        self.assertTrue(has_ace(poker_hand_examples["Royal Flush"]))
        self.assertTrue(has_ace(poker_hand_examples["Four of a Kind"]))
        self.assertFalse(has_ace(poker_hand_examples["High Card"]))


    def test_has_flush(self):
        self.assertTrue(has_flush(poker_hand_examples["Royal Flush"]))
        self.assertTrue(has_flush(poker_hand_examples["Straight Flush"]))
        self.assertTrue(has_flush(poker_hand_examples["Flush"]))
        self.assertFalse(has_flush(poker_hand_examples["Three Of A Kind"]))
        self.assertFalse(has_flush(poker_hand_examples["Pair"]))
        self.assertFalse(has_flush(poker_hand_examples["Two Pair"]))

    
    def test_has_straight(self):
        self.assertTrue(has_straight(poker_hand_examples["Royal Flush"]))
        self.assertTrue(has_straight(poker_hand_examples["Straight Flush"]))
        self.assertFalse(has_straight(poker_hand_examples["Flush"]))
        self.assertFalse(has_straight(poker_hand_examples["Three Of A Kind"]))
        self.assertFalse(has_straight(poker_hand_examples["Pair"]))
        self.assertFalse(has_straight(poker_hand_examples["Two Pair"]))

    def test_has_four_of_a_kind(self):
        self.assertTrue(has_four_of_a_kind(poker_hand_examples['Four of a Kind']))
        self.assertFalse(has_four_of_a_kind(poker_hand_examples["Flush"]))
        self.assertFalse(has_four_of_a_kind(poker_hand_examples["Three Of A Kind"]))
        self.assertFalse(has_four_of_a_kind(poker_hand_examples["Pair"]))
        self.assertFalse(has_four_of_a_kind(poker_hand_examples["Two Pair"]))


if __name__ == '__main__':
    unittest.main()