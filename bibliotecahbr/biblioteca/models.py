from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=4)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"({str(self.id_usuario)}) {self.nome}"

class Livro(models.Model):
    
    class Disponibilidade(models.TextChoices):
        DISPONIVEL = "Disponível"
        EMPRESTADO = "Emprestado"

    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    isbn = models.CharField(max_length=100)
    disponivel = models.CharField(max_length=10, choices=Disponibilidade, default=Disponibilidade.DISPONIVEL)

    def __str__(self):
        return f"({str(self.id_livro)}) {self.titulo}"
    
class Emprestimo(models.Model):
    class Status(models.TextChoices):
        FINALIZADO = "Finalizado"
        ANDAMENTO = "Em andamento"
        ATRASADO = "Atrasado"

    id_emprestimo = models.AutoField(primary_key=True)
    data_emp = models.DateField()
    dev_prev = models.DateField()
    data_dev = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=12, choices=Status, default=Status.ANDAMENTO)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.id_emprestimo)}"