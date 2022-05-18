import pytest

from app.src.exceptions import NonAlphaNumericError, InvalidCountryError, InvalidLengthError
from app.src.validation import (
    _format_iban_string,
    _check_iban_length,
    _iban_string_to_integer,
    iban_is_valid,
)

VALID_IBAN = "AL35202111090000000001234567"


def test_iban_is_valid():
    """Test the main validation function"""

    assert iban_is_valid(iban=VALID_IBAN)
    assert not iban_is_valid(iban="AL35202111090000000001234568")

    with pytest.raises(NonAlphaNumericError):
        iban_is_valid(iban=VALID_IBAN + "!")
    with pytest.raises(InvalidLengthError):
        iban_is_valid(iban=VALID_IBAN + "1")
    with pytest.raises(InvalidCountryError):
        iban_is_valid(iban="XX35202111090000000001234567")


def test_format_iban_string():
    """Test formatting function"""
    assert _format_iban_string(iban=VALID_IBAN) == VALID_IBAN
    assert _format_iban_string(iban="al 352021 110900000000 01234567") == VALID_IBAN
    with pytest.raises(NonAlphaNumericError):
        assert _format_iban_string(iban="!! aa .<.<. 01234567") == "!!AA.<.<.01234567"


def test_iban_length_is_valid():
    """Test length checking function"""
    _check_iban_length(iban=VALID_IBAN, country="AL")
    with pytest.raises(InvalidLengthError):
        _check_iban_length(iban=VALID_IBAN + "1", country="AL")


def test_iban_string_to_integer():
    """Test string to integer conversion function"""
    assert _iban_string_to_integer(iban="AAAA123") == 12310101010

