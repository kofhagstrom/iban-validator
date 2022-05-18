class InvalidCountryError(Exception):
    """Raised when an invalid country is given in an IBAN string."""
    def __init__(self, country):
        self.country = country


class InvalidLengthError(Exception):
    """Raised when the length of an IBAN string does not agree with
    the country given by the string"""
    def __init__(self, length: int, expected_length: int, country: str):
        self.length = length
        self.expected_length = expected_length
        self.country = country


class NonAlphaNumericError(Exception):
    """Raised when IBAN string contains non-alphanumeric characters"""
    pass
