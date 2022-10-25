from django.db import models

from produtos.validators.validate_comissao import validate_comissao


class Item(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    percentual_comissao = models.IntegerField(validators=[validate_comissao])

    def __str__(self) -> str:
        return self.nome

    def get_percentual_comissao(self):
        return self.percentual_comissao / 100
