from fastapi import FastAPI, HTTPException

from app.src.exceptions import (AlphaNumericError, InvalidCountryError,
                                InvalidLengthError)
from app.src.iban import iban_is_valid

app = FastAPI()


@app.get("/api/v1/iban-validation/{iban}")
def iban_validation(iban: str):

    try:
        is_valid = iban_is_valid(iban=iban)
    except AlphaNumericError:
        raise HTTPException(
            status_code=400, detail="IBAN must only contain alphanumeric characters")
    except InvalidCountryError:
        raise HTTPException(status_code=400, detail="IBAN country is invalid")
    except InvalidLengthError:
        raise HTTPException(status_code=400, detail="IBAN length is invalid")

    return {"valid": is_valid}
