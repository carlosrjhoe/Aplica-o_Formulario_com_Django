from django.db import models
from django.utils.translation import gettext_lazy as _

class ClasseViagem(models.TextChoices):
        ECONOMICA = 'ECO', _('Econômica')
        EXECUTIVA = 'EXE', _('Executiva')
        PRIMEIRA_CLASSE = 'PRI', _('Primeira')