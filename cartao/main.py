from birthday import MensagemAniversario
from christmas import MensagemNatal
from vallentine import MensagemDiaDosNamorados

listMsg = []

m1 = MensagemAniversario('D1', 'R1')
m2 = MensagemNatal ('D2', 'R2')
m3 = MensagemDiaDosNamorados ('D3',  'R3')

listMsg.append(m1)
listMsg.append(m2)
listMsg.append(m3)

for msn in listMsg:
    print(msn)
