# import load_workbook
from openpyxl import load_workbook
from cogroo_interface import Cogroo

def abrirArquivo(filepath):        
        # load corpus 
        wb = load_workbook(filepath)
        return wb.active
        
def lematizar(texto):
        return cogroo.lemmatize(texto)

def analisar(texto):
        return cogroo.analyze(texto)

def imprimirTokens(texto):
        print (texto.sentences[0].tokens)

def lerPerguntas():
        # iterate over all rows
                       
        for i in range(2, max_row+1):
                # get particular cell value
                id = planilha.cell(row = i, column = 1)    
                enunciado = planilha.cell(row = i, column = 2).value
                classe = planilha.cell(row = i, column = 4).value
                print("%s e %s" %(enunciado, classe))
                if enunciado != "None":
                        pergunta = (i, enunciado, classe)       
                        perguntas.append(pergunta)

                        if classe not in classes:
                                classes.add(classe)


# set file path
filepath = "C:/Users/Maica/Desktop/T2 IA/T2_IA/todos.xlsx"
cogroo = Cogroo.Instance()

classes = set()
perguntas = list()

planilha = abrirArquivo(filepath)

# get max row count
max_row = planilha.max_row
# get max column count
max_column = planilha.max_column

lerPerguntas()

print(len(classes))
print(len(perguntas))









# get b1 cell value
# b1 = sheet['B1']
# get b2 cell value
# b2 = sheet['B2']
# get b3 cell value
# b3 = sheet.cell(row = 3, column = 2)
# print b1, b2 and b3
