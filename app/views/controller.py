from pydantic import BaseModel

class ControllerResponse(BaseModel):
    controller_field: str
