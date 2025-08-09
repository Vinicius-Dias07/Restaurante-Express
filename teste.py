class People:
    def __init__(self, name, age, oficce):
        self._name = name.title()
        self._age = age
        self._oficce = oficce.lower()

    def __str__(self):
        return f'nome: {self._name} | idade: {self._age} | profissão: {self._oficce}'

    def aniversario(self):
        self._age += 1

    def cumprimento(self):
        return print(f'Ola {self._name}, seja bem vindo, é bom ter um {self._oficce} conosco!')    

Claudio = People('claudio', 25, 'Programador')
Claudio.aniversario()

print(Claudio)


