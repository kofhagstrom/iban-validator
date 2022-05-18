from fastapi import FastAPI, HTTPException

from app.src.exceptions import (
    NonAlphaNumericError,
    InvalidCountryError,
    InvalidLengthError,
)
from app.src.validation import iban_is_valid
from app.schemas import IbanValidation

description="""
IBANValidator helps you validate IBAN numbers


IBANValidator has one enpoint:\n
    GET /api/v1/iban-validation/{iban}\n
which validates an IBAN given by iban.\n

It returns status code 200 if IBAN is correctly formatted, with schema 
key 'valid' being 'true' if IBAN number is valid, and 'false' otherwise.

It returns status code 422 if the IBAN string is incorrectly formatted"""

app = FastAPI(
    title="IBANValidator",
    description=description,
    version="0.0.1",
)


@app.get("/api/v1/iban-validation/{iban}", response_model=IbanValidation)
def iban_validation(iban: str):
    try:
        is_valid = iban_is_valid(iban=iban)
        return IbanValidation(valid=is_valid)
    except NonAlphaNumericError:
        raise HTTPException(
            status_code=422, detail="IBAN must contain only alphanumeric characters"
        )
    except InvalidCountryError as exc:
        raise HTTPException(status_code=422, detail=f"IBAN country is invalid. Got {exc.country}.")
    except InvalidLengthError as exc:
        raise HTTPException(
            status_code=422,
            detail=(
                f"IBAN length is invalid. Expected length {exc.expected_length}"
                f"for country {exc.country}. Got length {exc.length}."
            ),
        )

