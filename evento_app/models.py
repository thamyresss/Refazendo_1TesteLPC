from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return "Gatinho(a): " + self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length = 11)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length = 14)
    razaoSocial = models.CharField(max_length = 30)

class Autor(Pessoa):
    curriculo = models.TextField()
    #artigos
class Evento(models.Model):
    nome = models.CharField(max_length = 100)
    eventoPrincipal = models.CharField(max_length = 70)
    dataEHoraDeInicio = models.DateTimeField()
    palavraChave = models.CharField(max_length = 20)
    logotipo = models.CharField(max_length = 20)
   #realizador = models.ForeignKey(PessoaFisica, null = True, blank = False)
    cidade = models.CharField(max_length = 20)
    uf = models.CharField(max_length = 20)
    endereco = models.CharField(max_length = 25)
    cep = models.CharField(max_length = 10)

    def __str__(self):
        return self.nome + " - " + self.logotipo

class EventoCientifico(Evento):
    issn = models.IntegerField(default = 0)

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length = 25)
    #autors = 
    evento_cientifico = models.ForeignKey(EventoCientifico, null = True, blank = False)
# Create your models here.
