from pydantic import BaseModel

class ControllerRequest(BaseModel):
    controller_field: str
