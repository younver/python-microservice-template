from fastapi.testclient import TestClient
import pytest

from app.views import HealthResponse, ControllerResponse
from app.models import ControllerRequest
from app.configs import settings
from app.main import app


client = TestClient(app)


class TestHealthController:

    def test_should_return_healthy(self):

        response = client.get("/health-check")

        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}

    def test_should_return_not_found_when_invalid_uri(self):

        response = client.get("/health-check/123")

        assert response.status_code == 404

class TestControllerController:

    def test_should_return_controller_response(self):

        response = client.post("/controller", json={
            "controller_field": "something"
            })

        assert response.status_code == 200
        assert response.json() == {"controller_field": "something"+settings.EXAMPLE_VARIABLE}

    def test_should_return_not_found_when_invalid_uri(self):

        response = client.post("/controller/123", json={
            "controller_field": "something"
            })

        assert response.status_code == 404


class TestControllerRequest:
    
    @pytest.mark.parametrize(
        "value",
        [
            "gchord",
            "d'avion",
            419,
            True
        ],
    )
    def test_should_create_controller_request(self, value):
        
        request = ControllerRequest(controller_field= value)

        assert request.controller_field == str(value)


class TestHealthResponse:
    
    @pytest.mark.parametrize(
        "value",
        [
            "ok",
            "healthy",
            42,
            False
        ],
    )
    def test_should_create_health_response(self, value):

        health = HealthResponse(status= value)

        assert health.status == str(value)

class TestControllerResponse:
    
    @pytest.mark.parametrize(
        "field",
        [
            "something",
            "controllerresponse",
            83,
            True
        ],
    )
    def test_should_create_controller_response(self, field):

        controller = ControllerResponse(controller_field= field)

        assert controller.controller_field == str(field)
