from simple_history.admin import SimpleHistoryAdmin
from django.contrib import admin
from escala.models import Escala


class EscalaAdmin(SimpleHistoryAdmin):
    list_display = ['pessoa', 'cargo', 'data', 'descricao']


admin.site.register(Escala, EscalaAdmin)
