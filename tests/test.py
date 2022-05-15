import unittest

from app.src.exceptions import AlphaNumericError, InvalidCountryError, InvalidLengthError
from app.src.validation import (
    _format_iban_string,
    _check_iban_length,
    _iban_string_to_integer,
    iban_is_valid,
)

VALID_IBAN = "AL35202111090000000001234567"


class TestIbanValidation(unittest.TestCase):
    def test_iban_is_valid(self):
        """Test the main validation function"""

        self.assertTrue(iban_is_valid(iban=VALID_IBAN))
        self.assertFalse(iban_is_valid(iban="AL35202111090000000001234568"))

        with self.assertRaises(AlphaNumericError):
            iban_is_valid(iban=VALID_IBAN + "!")
        with self.assertRaises(InvalidLengthError):
            iban_is_valid(iban=VALID_IBAN + "1")
        with self.assertRaises(InvalidCountryError):
            iban_is_valid(iban="test" + VALID_IBAN)

    def test_format_iban_string(self):
        """Test formatting function"""
        self.assertEqual(_format_iban_string(iban=VALID_IBAN), VALID_IBAN)
        self.assertEqual(_format_iban_string(iban="al 352021 110900000000 01234567"), VALID_IBAN)
        self.assertEqual(_format_iban_string(iban="!! aa .<.<. 01234567"), "!!AA.<.<.01234567")

    def test_iban_length_is_valid(self):
        """Test length checking function"""
        _check_iban_length(iban=VALID_IBAN, country="AL")
        with self.assertRaises(InvalidLengthError):
            _check_iban_length(iban=VALID_IBAN + "1", country="AL")

    def test_iban_string_to_integer(self):
        self.assertEqual(_iban_string_to_integer(iban="AAAA123"), 12310101010)


if __name__ == "__main__":
    unittest.main()
