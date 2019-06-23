# import load_workbook
from openpyxl import load_workbook
from cogroo_interface import Cogroo

def abrirArquivo(filepath):        
        # load corpus 
        wb = load_workbook(filepath)
        return wb.active
        
def lerPerguntas():
        # iterate over all rows
                       
        for i in range(2, max_row+1):
                # get particular cell value
                enunciado = planilha.cell(row = i, column = 2).value
                classe = planilha.cell(row = i, column = 4).value
              # print("%s e %s" %(enunciado, classe))

                if enunciado != None:
                        pergunta = [i, enunciado, classe]       
                        perguntas.append(pergunta)

                        if classe != None and classe not in classes:
                                classes.add(classe)

def lematizar(texto):
        return cogroo.lemmatize(texto)

def analisar(texto):
        return cogroo.analyze(texto)

def imprimirTokens(texto):
        print (texto.sentences[0].tokens)

# set file path
filepath = "C:/Users/Maica/Desktop/T2IA/T2_IA/corpus.xlsx"
cogroo = Cogroo.Instance()

classes = set()
perguntas = list()

planilha = abrirArquivo(filepath)

# get max row count
max_row = planilha.max_row
# get max column count
max_column = planilha.max_column

lerPerguntas()

aux = analisar("Testando a implementacao")
print(imprimirTokens(aux))
##for p in perguntas:
##        p.append(lematizar(p[1]))
##       # print(p[3])
##        
##for p in perguntas:
##        morfo = analisar(p[3])
##        tokens = imprimirTokens(morfo)
##        p.append(tokens)
##        print(p[4])

print("DONE")
        
#print(len(classes))







# get b1 cell value
# b1 = sheet['B1']
# get b2 cell value
# b2 = sheet['B2']
# get b3 cell value
# b3 = sheet.cell(row = 3, column = 2)
# print b1, b2 and b3
