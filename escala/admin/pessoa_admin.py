from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin
from escala.models import Pessoa


class PessoaAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'nome', 'email', 'instrumentos')

    def instrumentos(self, obj):
        return ', '.join(inst.nome for inst in obj.instrumento.all())



admin.site.register(Pessoa, PessoaAdmin)
