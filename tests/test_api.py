import pytest

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

VALID_IBAN = "AL35202111090000000001234567"

def test_iban_validation():
    """Test API endpoint."""

    # A correctly formatted IBAN number should return status code 200
    # and valid=True
    response = client.get(f"/api/v1/iban-validation/{VALID_IBAN}")
    assert response.status_code == 200
    data = response.json()
    assert data["valid"]

    # A correctly formatted IBAN number with an incorrect remainder modulo 97
    # should return status 200 but with valid=False
    response = client.get(f"/api/v1/iban-validation/AL35202111090000000001234568")
    assert response.status_code == 200
    data = response.json()
    assert not data["valid"]

    # An incorrectly formatted IBAN number containing non-alphanumeric characters
    # should return status code 422
    response = client.get(f"/api/v1/iban-validation/{VALID_IBAN + '!'}")
    assert response.status_code == 422

    # An incorrectly formatted IBAN number which is too long for the given country
    # should return status code 422
    response = client.get(f"/api/v1/iban-validation/{VALID_IBAN + '1'}")
    assert response.status_code == 422
    
    # An incorrectly formatted IBAN number containing a non-existing country
    # should return status code 422
    response = client.get(f"/api/v1/iban-validation/XX35202111090000000001234567")
    assert response.status_code == 422
