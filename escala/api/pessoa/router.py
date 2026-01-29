from ninja import Router
from django.shortcuts import get_object_or_404

from escala.models.pessoa import Pessoa

from .schemas import (
    PessoaEntradaPost,
    PessoaSaidaGet,
    PessoaSaidaPost,
    PessoaSaidaDelete,
    PessoaEntradaPut,
    PessoaSaidaPut,
)

router_v1 = Router()


@router_v1.get(path='/', response=list[PessoaSaidaGet], summary='Lista pessoas')
def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return pessoas


@router_v1.get(path='/{pessoa_id}', response=PessoaSaidaGet, summary='Busca pessoa por ID')
def busca_pessoa_por_id(request, pessoa_id: int):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    return pessoa


@router_v1.post(path='/', response=PessoaSaidaPost, summary='Cria uma nova pessoa')
def cria_uma_nova_pessoa(request, payload: PessoaEntradaPost):
    payload_dict = payload.dict()
    instrumento_ids = payload_dict.pop('instrumento_ids', [])  # pode vir vazio
    # cria a pessoa sem FK/M2M
    pessoa = Pessoa(**payload_dict)
    pessoa.full_clean()
    pessoa.save()
    # seta o M2M
    if instrumento_ids:
        pessoa.instrumento.set(instrumento_ids)

    return {'id': pessoa.id}


@router_v1.put(path='/{pessoa_id}', response=PessoaSaidaPut, summary='Atualiza uma pessoa')
def atualiza_uma_pessoa(request, pessoa_id: int, payload: PessoaEntradaPut):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    for attr, value in payload.dict().items():
        setattr(pessoa, attr, value)
    pessoa.save()
    return {'success': True}


@router_v1.delete(path='/{pessoa_id}', response=PessoaSaidaDelete, summary='Exclui uma pessoa')
def exclui_uma_pessoa(request, pessoa_id: int):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    pessoa.delete()
    return {'success': True}
