from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/iban-validation/{iban}")
def iban_validation(iban: str):

    return {}
