from ninja import ModelSchema, Schema

from escala.api.cargo.schemas import CargoSaidaGet
from escala.api.pessoa.schemas import PessoaSaidaGet
from escala.models.escala import Escala


class EscalaSaidaGet(ModelSchema):
    pessoa: PessoaSaidaGet
    cargos: list[CargoSaidaGet]

    class Meta:
        model = Escala
        fields = ['id', 'data', 'descricao']


class EscalaEntradaPost(ModelSchema):
    cargo_ids: list[int]
    pessoa_id: int
    descricao: str | None = None

    class Meta:
        model = Escala
        fields = ['data', 'descricao']


class EscalaSaidaPost(Schema):
    id: int


class EscalaEntradaPut(ModelSchema):
    cargo_ids: list[int]
    pessoa_id: int
    descricao: str | None = None

    class Meta:
        model = Escala
        fields = ['data', 'descricao']


class EscalaSaidaPut(Schema):
    success: bool


class EscalaSaidaDelete(Schema):
    success: bool
