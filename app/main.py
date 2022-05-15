from fastapi import FastAPI, HTTPException

from app.src.exceptions import (
    AlphaNumericError,
    InvalidCountryError,
    InvalidLengthError,
)
from app.src.validation import iban_is_valid

app = FastAPI()


@app.get("/api/v1/iban-validation/{iban}")
def iban_validation(iban: str):

    try:
        is_valid = iban_is_valid(iban=iban)
    
    except AlphaNumericError:
        raise HTTPException(
            status_code=400, detail="IBAN must contain only alphanumeric characters"
        )
    
    except InvalidCountryError as exc:
        raise HTTPException(status_code=400, detail=f"IBAN country is invalid. Got {exc.country}.")
    
    except InvalidLengthError as exc:
        raise HTTPException(
            status_code=400,
            detail=(
                f"IBAN length is invalid. Expected length {exc.expected_length}"
                f"for country {exc.country}. Got length {exc.length}."
            ),
        )

    return {"valid": is_valid}
