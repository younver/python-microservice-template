from pydantic import BaseSettings
from environs import Env

env = Env()
env.read_env()

class Settings(BaseSettings):
    EXAMPLE_VARIABLE: str = env.str("EXAMPLE_VARIABLE")

settings = Settings()
