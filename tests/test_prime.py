import unittest
import sys
from pathlib import Path
from unittest.mock import patch
import io

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "Scripts"))

with patch("builtins.input", return_value="0"), patch("sys.stdout", new=io.StringIO()):
    import prime_number_check


class TestIsPrime(unittest.TestCase):
    def test_values(self):
        self.assertFalse(prime_number_check.is_prime(1))
        self.assertTrue(prime_number_check.is_prime(2))
        self.assertTrue(prime_number_check.is_prime(3))
        self.assertFalse(prime_number_check.is_prime(4))
        self.assertTrue(prime_number_check.is_prime(17))


if __name__ == "__main__":
    unittest.main()
