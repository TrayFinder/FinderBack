import uvicorn
from fastapi import FastAPI
from app.utils.load_env import load_env_variables

load_env_variables('.env')

from app.core.config import settings
from app.utils.logger_class import LoggerClass
from app.core.router import get_api_router
from app.core.database import init_db

LoggerClass.configure("fastapi", debug=True)

app = FastAPI()

app.include_router(get_api_router())

@app.get("/")
def root():
    """
    Root endpoint
    """
    return {"message": "Hello World"}

if __name__ == "__main__":
    init_db()
    uvicorn.run(
        app,
        host = settings.server_host,
        port = settings.server_port
    )