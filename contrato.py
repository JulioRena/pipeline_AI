from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validator, PositiveFloat, PositiveInt
from enum import Enum


class ProdutoEnum(str, Enum):
    produto1 = "Gemini"
    produto2 = "GPT"
    produto3 = "Llama"


class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.
    
    Args:
    email(EmailStr): email do comprador
    data(datetime): data da compra
    valor(PositiveFloat): valor da compra
    quantidade(PositiveInt): quantidade de produtos
    produto(ProdutoEnum): categoria do produto
    

    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
    
    
    @validator('produto')
    def categoria_deve_estar_no_enum(cls,v):
        return v
        