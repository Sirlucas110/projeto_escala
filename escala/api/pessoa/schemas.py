from ninja import ModelSchema, Schema
from typing import Optional
from escala.models.pessoa import Pessoa
from escala.api.instrumento.schemas import InstrumentoSaidaGet


class PessoaSaidaGet(ModelSchema):
    instrumento: Optional[list[InstrumentoSaidaGet]] = None

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email', 'telefone']


class PessoaEntradaPost(ModelSchema):
    instrumento_ids: Optional[list[int]] = []

    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'telefone']


class PessoaSaidaPost(Schema):
    id: int


class PessoaEntradaPut(ModelSchema):
    instrumento_ids: Optional[list[int]] = []

    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'telefone']


class PessoaSaidaPut(Schema):
    success: bool


class PessoaSaidaDelete(Schema):
    success: bool
