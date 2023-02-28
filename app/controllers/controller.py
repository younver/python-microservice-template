from fastapi import APIRouter, HTTPException
from app.configs import settings
from app.models import ControllerRequest
from app.views import ControllerResponse

router = APIRouter()

# TODO: custom exceptions
@router.post("/controller")
async def controller(request: ControllerRequest) -> ControllerResponse:
    
    try:
        field = request.controller_field
        field += settings.SERVICE_KEY
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))

    response = ControllerResponse(controller_field= field)
    return response
