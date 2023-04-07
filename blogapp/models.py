from django.db import models


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)

    class Meta:
        abstract = True


class Blog(Base):
    title = models.CharField('Title', max_length=100, null=False, blank=False)
    author = models.CharField('Author', max_length=50, null=False, blank=False)
    subtitle = models.CharField('Subtitle', max_length=300, null=False, blank=False)
    text = models.TextField('Text', max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.title
