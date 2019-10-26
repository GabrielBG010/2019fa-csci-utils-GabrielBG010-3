"""
Unittests for hash_str module.
"""

from unittest import TestCase
from csci_utils.hash_str import hash_str

class HashTests(TestCase):
    def test_basic(self):
        pass
        self.assertEqual(hash_str("world!", salt="hello, ").hex()[:6], "68e656")
