from typing import Optional

from pydantic import BaseModel, Field


class NotFound(BaseModel):
    message: str = Field(
        description="Erro caso o recurso não for encontrado.",
        example="O CPF informado não possui ofertas ativas na base."
    )


class InternalServerError(BaseModel):
    message: str = Field(
        description="Tratativa de erros.",
        example="Houve um erro."
    )


class HealthCheckResponse(BaseModel):
    message: Optional[str] = Field(example="It`s alive!")
    version: Optional[str] = Field(example="3.0.0")


class StandardOutput(BaseModel):
    message: str


class CustomOutput(BaseModel):
    message: str = Field(
        description="Status code and message.",
        example="(400, 'Not Found.')"
    )
