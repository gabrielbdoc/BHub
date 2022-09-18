from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from src import __version__
from src.schemas.banking_data_schemas import BankingDataInput, BankingData
from src.schemas.commons import HealthCheckResponse, StandardOutput, CustomOutput
from src.services.banking_data_services import BankingDataService

router = APIRouter(
    tags=["Rotas Banking"],
    prefix="/api/banking",
    include_in_schema=True
)


@router.get(
    "/health-check",
    summary="Health-check interno",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheckResponse,
    include_in_schema=True
)
def health_check():
    '''
    Check-up de saúde da aplicação de dados bancários.
    '''
    return {"message": "It`s alive!", "version": __version__}


@router.get(
    "/list/{bank_code}",
    status_code=status.HTTP_200_OK,
    response_model=List[BankingData],
    responses={
        400: {
            "model": CustomOutput
        }
    }
)
async def bank_list(bank_code: int):
    '''
    Lista todos os usuários ativos de um banco específico (passado como parâmetro).
    '''
    try:
        return await BankingDataService().list_bank_users(bank_code)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.post(
    "/create",
    summary="Cria um novo cadastro de dados bancários no banco.",
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "model": CustomOutput
        }
    }
)
async def banking_data_create(banking_data_input: BankingDataInput):
    '''
    Cria um novo cadastro bancário para um usuário ativo na base.
    '''
    try:
        await BankingDataService.create_banking_data(banking_data_input)
        return StandardOutput(message='Created')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.delete(
    "/delete",
    status_code=status.HTTP_200_OK,
    responses={
        400: {
            "model": CustomOutput
        }
    }
)
async def user_delete(banking_data_input: BankingDataInput):
    '''
    Deleta o cadastro bancário. Isso não significa que o dado será excluído da base, mas sim identificado
     como 'desativado'.
    '''
    try:
        await BankingDataService().delete_banking_data(banking_data_input)
        return StandardOutput(message='Deleted')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
