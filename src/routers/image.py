import os

from fastapi import APIRouter
from fastapi.responses import FileResponse
from starlette import status


router = APIRouter(
    prefix="/api/images",
    include_in_schema=False
)


@router.get(
    "/database",
    summary="Internal health-check",
    status_code=status.HTTP_200_OK
)
def database_image():
    """
    Endpoint para busca da imagem da estrutura do banco de dados.
    """
    img = os.path.abspath("../src/utils/images/database.png")
    return FileResponse(img)
