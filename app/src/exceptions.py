class InvalidCountryError(Exception):
    def __init__(self, country):
        self.country = country


class InvalidLengthError(Exception):
    def __init__(self, length: int, expected_length: int, country: str):
        self.length = length
        self.expected_length = expected_length
        self.country = country


class AlphaNumericError(Exception):
    pass
