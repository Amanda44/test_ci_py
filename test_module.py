import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilise pour tester les fonctions du module 'random'."""

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        self.assertIn(elt, ('a', 'b', 'c'))

    unittest.main()
