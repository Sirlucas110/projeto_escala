from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin
from escala.models import Pessoa


class PessoaAdmin(SimpleHistoryAdmin):
    list_display = ['nome', 'email', 'telefone', 'instrumento', 'cargo']


admin.site.register(Pessoa, PessoaAdmin)
