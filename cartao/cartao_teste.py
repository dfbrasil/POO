from aniversario import MensagemAniversario
from namorados import MensagemDiaDosNamorados
from natal import MensagemNatal

listMsg = []

m1 = MensagemAniversario('D1', "texto1", 'R1')
m2 = MensagemNatal ('D2', 'texto2', 'R2')
m3 = MensagemDiaDosNamorados ('D3', 'texto3', 'R3')

listMsg.append(m1)
listMsg.append(m2)
listMsg.append(m3)

for msn in listMsg:
    print(msn)
