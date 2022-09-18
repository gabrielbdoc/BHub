import uvicorn
from fastapi import FastAPI

from src import __version__
from src.settings import BASE_PATH
from src.utils.swagger import MARKDOWN_DESCRIPTION
from src.routers import api_router

app = FastAPI(
    title="Desafio BHub",
    version=__version__,
    description=MARKDOWN_DESCRIPTION,
    docs_url=f"{BASE_PATH}/apis",
    redoc_url=f"{BASE_PATH}/apis/redoc",
    openapi_url=f"{BASE_PATH}/apis/openapi.json"
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",
        host='127.0.0.1',
        port=8181,
        debug=False,
        reload=False,
        timeout_keep_alive=50
    )
