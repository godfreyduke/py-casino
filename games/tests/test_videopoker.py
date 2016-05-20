"""
Tests for Video Poker
"""
from games.videopoker import VideoPoker

import unittest


class TestVideoPoker(unittest.TestCase):
    def test_start_with_hand(self):
        poker = VideoPoker()
        poker.start()
        self.assertEqual(len(poker.hand), 5)
