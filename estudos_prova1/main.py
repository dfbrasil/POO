from cliente import Cliente
from pessoa import Pessoa
from funcionario import Funcionario

person = Cliente('Daniel','brasil', 40, '123-4')
func = Funcionario ('novadata', 'empresa', 12, '567-8')

print(person.get_idade())
print(person.metodo_abstrato())
print(func.metodo_abstrato())
