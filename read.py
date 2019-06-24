from openpyxl import Workbook
from openpyxl import load_workbook
from cogroo_interface import Cogroo

def abrirArquivo():        
        return load_workbook(filename = filepath)
        
def lerPerguntas():
                       
        for i in range(1, max_row+1):
                enunciado = planilha.cell(row = i, column = 2).value
                classe = planilha.cell(row = i, column = 4).value
              
                if enunciado != None and classe != None:
                        pergunta = [i, enunciado, classe]       
                        perguntas.append(pergunta)

                        if classe not in classes:
                                classes.add(classe)
##                else:
##                        planilha.delete_rows(i)
##
##        arquivo.save(filename = "corpus.xlsx")                                

def lematizar(texto):
        return cogroo.lemmatize(texto)

def analisar(texto):
        return cogroo.analyze(texto)

def extrairTokens(texto):
        return texto.sentences[0].tokens

def classificarPergunta(pergunta):

        classe = pergunta[2]

        if classe not in dictDePerguntas.keys():
                perguntasDaClasse = [pergunta]
                dictDePerguntas[classe] = perguntasDaClasse
        else:
                perguntasDaClasse = dictDePerguntas[classe]
                perguntasDaClasse.append(pergunta)

#variáveis globais
classes = set()
perguntas = list()
dictDePerguntas = dict()
filepath = "C:/Users/Maica/Desktop/T2IA/T2_IA/corpus.xlsx"
cogroo = Cogroo.Instance()

#Lendo arquivo
arquivo = abrirArquivo()
planilha = arquivo.active
max_row = planilha.max_row
max_column = planilha.max_column

#Lendo perguntas
lerPerguntas()

#Normalizando e separando as perguntas por classes
for p in perguntas:
        p.append(lematizar(p[1]))
        morfo = analisar(p[3])
        tokens = extrairTokens(morfo)
        p.append(tokens)
        classificarPergunta(p)

print (len(classes))
print (len(dictDePerguntas))

print(perguntas[0])

#classes = list(classes)
#list.sort(classes)
#print (classes)
#print (dictDePerguntas.keys())

aux = set(dictDePerguntas.keys())
print (aux.difference(classes))
print (classes.difference(aux))
##for c in classes:
##        print(c)

##for c in dictDePerguntas.keys():
##        print(c)

print("DONE")
        









# get b1 cell value
# b1 = sheet['B1']
# get b2 cell value
# b2 = sheet['B2']
# get b3 cell value
# b3 = sheet.cell(row = 3, column = 2)
# print b1, b2 and b3
