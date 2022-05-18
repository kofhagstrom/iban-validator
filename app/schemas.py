from pydantic import BaseModel

class IbanValidation(BaseModel):
    valid: bool