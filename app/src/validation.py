from app.src.constants import COUNTRY_TO_LENGTH, LETTER_TO_BASE36
from app.src.exceptions import NonAlphaNumericError, InvalidCountryError, InvalidLengthError


def iban_is_valid(iban: str) -> bool:
    """Check if a string is a valid IBAN number.
    
    Returns True if the string is a valid IBAN number,
    and False otherwise."""

    formatted_iban = _format_iban_string(iban)

    country = _get_iban_country(iban=formatted_iban)

    formatted_iban = _check_iban_length(iban=formatted_iban, country=country)

    iban_integer = _iban_string_to_integer(iban=formatted_iban)

    return (iban_integer % 97) == 1


def _format_iban_string(iban: str) -> str:
    """Replace all spaces in string and make it upper case.
    
    If string contains non-alphanumeric characters,
    AlphaNumericError is raised."""

    formatted_iban = iban.upper().replace(" ", "")
    if not formatted_iban.isalnum():
        raise NonAlphaNumericError
    return formatted_iban


def _check_iban_length(iban: str, country: str) -> str:
    """
    Check that the length of an IBAN string is in agreement
    with the IBAN string length of a given country. If
    the length agrees, the original string is returned.

    If the length does not agree with the length specified for
    the country, InvalidLengthError is raised.
    """

    iban_length = len(iban)
    expected_length = COUNTRY_TO_LENGTH[country]

    if not iban_length == expected_length:
        raise InvalidLengthError(
            length=iban_length, expected_length=expected_length, country=country
        )

    return iban


def _iban_string_to_integer(iban: str) -> int:
    """Convert an IBAN string to an integer by rearranging the string
    and converting its letters to base 36."""

    rearranged_iban = iban[4:] + iban[:4]
    return int("".join([LETTER_TO_BASE36[letter] for letter in rearranged_iban]))


def _get_iban_country(iban: str) -> str:
    """Extract country information from an IBAN string.

    If the country extracted is invalid (i.e. not included in the keys
    of COUNTRY_TO_LENGTH), InvalidCountryError is raised."""
    country = iban[:2]

    if country not in COUNTRY_TO_LENGTH.keys():
        raise InvalidCountryError(country=country)

    return country
