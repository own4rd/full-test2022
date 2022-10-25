from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_comissao(value):
    if value > 10 or value < 0:
        raise ValidationError("O percentual de comissão deve ser entre 0 e 10.")
