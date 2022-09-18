from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from src import __version__
from src.schemas.commons import HealthCheckResponse, StandardOutput, CustomOutput
from src.schemas.user_schemas import UserCreateInput, UserDeleteInput, UserListOutput, UserUpdateInput
from src.services.user_services import UserService
from src.utils.user_validator import UserValidator

router = APIRouter(
    tags=["Rotas User"],
    prefix="/api/user",
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
    Check-up de saúde da aplicação de dados cadastrais.
    '''
    return {"message": "It`s alive!", "version": __version__}


@router.get(
    "/list",
    summary="Lista usuários",
    status_code=status.HTTP_200_OK,
    response_model=List[UserListOutput]
)
async def users_list():
    '''
    Lista todos os usuários na base de dados.
    '''
    try:
        return await UserService.list_users()
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.get(
    "/list/{user_id}",
    summary="Lista usuário",
    status_code=status.HTTP_200_OK,
    response_model=List[UserListOutput]
)
async def user_list(user_id: int = None):
    '''
    Lista um usuário específico da base de dados (passado como parâmetro), não importando se está ativo ou inativo.
    '''
    try:
        return await UserService.list_user(user_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.post(
    "/create",
    summary="Cria novo usuário",
    status_code=status.HTTP_201_CREATED,
    response_model=StandardOutput,
    responses={
        400: {
            "model": CustomOutput
        }
    }
)
async def user_create(user_input: UserCreateInput):
    '''
    Cria um novo usuário na base de dados, verificando se seus dados cadastrais são coerentes (formato do email, número
    de telefone válido, etc...)
    '''
    try:
        UserValidator().is_user_data_valid(user_input)
        await UserService.create_user(user_input)
        return StandardOutput(message='Created')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.patch(
    "/patch/{user_id}",
    summary="Atualiza cadadastro do usuário",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        400: {
            "model": CustomOutput
        }
    }
)
async def update_user(user_id: int, user_input: UserUpdateInput):
    '''
    Atualiza somente os dados cadastrais enviados na requisição para um usuário ativo (passado como parâmetro),
    validando os dados.
    '''
    try:
        UserValidator().is_user_data_valid(user_input)
        return await UserService().update_user(user_id, user_input)
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@router.delete(
    "/delete",
    summary="Deleta usuário",
    status_code=status.HTTP_200_OK,
    responses={
        400: {
            "model": CustomOutput
        }
    }
)
async def user_delete(user_input: UserDeleteInput):
    '''
    Deleta o usuário. Isso não significa que o dado será excluído da base, mas sim identificado
     como 'desativado'. Em adição, todos os dados bancários para este usuário também serão deletados.
    '''
    try:
        await UserService().delete_user(user_id=user_input.user_id)
        return StandardOutput(message='Deleted')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
