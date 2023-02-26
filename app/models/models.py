from pydantic import BaseModel

class Request(BaseModel):
    some_field: str

class Response(BaseModel):
    some_field: str
