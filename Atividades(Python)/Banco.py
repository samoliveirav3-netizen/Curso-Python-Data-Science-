print("----Banco----")
print("1.extrato")
print("2.saque")
print("3.deposito")
print("4.saldo")
saldo = 100.0
saque = float(input("Quanto deseja retirar?"))
extrato = saldo - saque
print("Extrato:Voce retirou",saque,",e ficou com",extrato )
deposito = float(input("QUanto deseja colocar?"))
extrato_2 = extrato + deposito
print("Extrato:Voce retirou",deposito,",e ficou com",extrato_2 )
print("Saldo Final:Seu saldo final ficou com",extrato_2)
