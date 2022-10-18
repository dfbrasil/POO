from contaAlura import Conta, Cliente, DataBanco

data = DataBanco()
cliente = Cliente('Daniel', 'Brasil', 123)
conta = Conta('123-4', cliente, 120.0, 1000.0, data)

print (type(conta))
print(conta.numero)

print(conta.titular)

conta.deposita(50)
conta.extrato()
conta.saca(20)
conta.extrato()

