from app.src.constants import COUNTRY_TO_LENGTH, LETTER_TO_BASE36
from app.src.exceptions import AlphaNumericError, InvalidCountryError, InvalidLengthError


def iban_is_valid(iban: str) -> bool:
    """Validate a string containing an IBAN number."""
    
    if not formatted_iban.isalnum():
        raise AlphaNumericError

    formatted_iban = _format_iban_string(iban)

    country = _get_iban_country(iban=formatted_iban)

    if not _iban_length_is_valid(iban=formatted_iban, country=country):
        raise InvalidLengthError(
            length=len(formatted_iban),
            expected_length=COUNTRY_TO_LENGTH[country],
            country=country
        )

    iban_integer = _iban_string_to_integer(iban=formatted_iban)

    return (iban_integer % 97) == 1


def _format_iban_string(iban: str) -> str:
    """Replace all spaces in string and make it upper case"""
    return iban.upper().replace(" ", "")


def _iban_length_is_valid(iban: str, country: str) -> bool:
    """Check that the length of an IBAN string is in agreement
    with the IBAN string length of a given country"""
    return len(iban) == COUNTRY_TO_LENGTH[country]


def _iban_string_to_integer(iban: str) -> int:
    """Convert an IBAN string to an integer by rearranging the string
    and converting its letters to base 36"""
    rearranged_iban = iban[4:] + iban[:4]
    return int("".join([LETTER_TO_BASE36[letter]
                        for letter in rearranged_iban]))


def _get_iban_country(iban: str) -> str:
    """Extract country information from an IBAN string"""
    country = iban[:2]

    if country not in COUNTRY_TO_LENGTH.keys():
        raise InvalidCountryError(country=country)

    return country
