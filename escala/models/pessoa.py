from django.db.models import PROTECT, CharField, EmailField, ForeignKey, Model

from escala.models.cargo import Cargo
from escala.models.instrumento import Instrumento

from simple_history import register


class Pessoa(Model):
    instrumento = ForeignKey(
        to=Instrumento,
        on_delete=PROTECT,
        related_name='pessoas_que_tocam',
        blank=True,
        null=True,
    )
    cargo = ForeignKey(to=Cargo, on_delete=PROTECT, related_name='pessoas_com_cargo')
    nome = CharField(verbose_name='Nome', max_length=255)
    email = EmailField(verbose_name='Email')
    telefone = CharField(verbose_name='Telefone')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = '"escala"."pessoa"'
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


register(model=Pessoa, table_name='"escala"."historico_pessoa"')
