from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Configurações do banco de dados
    db_user: str = Field(default=None, alias='DB_USER')
    db_password: SecretStr = Field(default=None, alias='DB_PASSWORD')
    db_host: str = Field(default=None, alias='DB_HOST')
    db_port: int = Field(default=None, alias='DB_PORT')
    db_name: str = Field(default=None, alias='DB_NAME')

    # Configurações do servidor
    server_host: str = Field(default=None, alias='SERVER_HOST')
    server_port: int = Field(default=None, alias='SERVER_PORT')


settings = Settings()
