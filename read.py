import os, operator
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
        result = list()
        aux = texto.sentences[0].tokens
        for i in range (len(aux)):
                string = str(aux[i])
                split = string.split('#')
                if((("adv" in split[1]) or "v-inf" in split[1]) or "prop" in split[1]):
                        result.append(split[0])
        return result

def classificarPergunta(pergunta):

        classe = pergunta[2]

        if classe not in dictDePerguntas.keys():
                perguntasDaClasse = [pergunta]
                dictDePerguntas[classe] = perguntasDaClasse
        else:
                perguntasDaClasse = dictDePerguntas[classe]
                perguntasDaClasse.append(pergunta)

def criarBoW():
        for classe in dictDePerguntas: #pego todas as perguntas de cada classe
                tokens = dict() #gero um dicionario dos tokens
                lista = dictDePerguntas[classe]
                for i in range (len(lista)):
                        pergunta = lista[i]
                        pergunta = pergunta[4] #pego os tokens da pergunta atual
                        for token in pergunta:
                                if token not in tokens.keys():
                                        tokens[token] = 1
                                else:
                                        tokens[token] = tokens[token] + 1
                sorted_tokens = sorted(tokens.items(), key=operator.itemgetter(1),reverse=True)
                for j in range(5):
                        aux = sorted_tokens[j][0]
                        if(aux not in listaGeral):
                                listaGeral.append(aux)
                        
def estruturar():
        for i in range(len(perguntas)):
                vector = list()
                aux = perguntas[i]
                for j in range(len(aux[4])):
                        palavra = aux[4][j]
                        for k in range(len(listaGeral)):
                                if(palavra == listaGeral[k]):
                                        vector.append(k)
                result = list()
                for w in range(len(listaGeral)):
                        result.append(0)
                for index in vector:
                        result[index] = 1
                perguntas[i].append(result)
'''
@attribute P1 integer
@attribute P2 integer
@attribute P3 integer
@attribute P4 integer
@attribute classe {Conceito,Tarefa}
@data
0, 0, 0, 1, Conceito
1, 0, 1, 0, Tarefa
0, 0, 0, 1, Conceito
1, 0, 0, 0, Tarefa
1, 0, 0, 1, Conceito
'''
def criarOutput():
        f= open(outpath,"w+")
        f.write("@relation Arquivo \n")
        for i in range(len(listaGeral)):
                f.write("@atribute P"+str(i) +" integer"+"\n")
        f.write("@data \n")
        for i in range(len(perguntas)):
                aux = str(perguntas[i][5])
                aux = aux.strip('[]')
                f.write(aux+", "+perguntas[i][2] +"\n")
        f.close()
#variáveis globais
classes = set() #lista de todas as classes existentes
perguntas = list() #lista com todas as perguntas, suas infos e tokens relevantes
dictDePerguntas = dict() #dicionario com as chaves sendo as classes, os dados as perguntas
listaGeral = list() #lista geral dos termos que mais aparecem, BoW

#filepath = os.getcwd()+"/corpus.xlsx" ALTERAR VALOR DEPOIS DE NOVO
filepath = os.getcwd()+"/dummy.xlsx"
outpath = os.getcwd()+"/weka_input.arff"
if(os.path.exists(outpath)):
        os.remove(outpath)

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

criarBoW()
#print(listaGeral)
estruturar()

criarOutput()
#print (len(classes))
#print (len(dictDePerguntas))

#print(perguntas[0])

#classes = list(classes)
#list.sort(classes)
#print (classes)
#print (dictDePerguntas.keys())

#aux = set(dictDePerguntas.keys())
#print (aux.difference(classes))
#print (classes.difference(aux))
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
