from pydantic import BaseSettings
from environs import Env


env = Env()
env.read_env()


class Application(BaseSettings):
    SERVICE_KEY: str = env.str("SERVICE_KEY")


settings = Application()
