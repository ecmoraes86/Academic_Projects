import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;.!?]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(0,6):
        soma = soma + (abs(as_a[i] - as_b[i]))
    return soma/6
    
def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    n_caracteres_texto = 0
    lista_palavras_texto = []
    for sentenca in separa_sentencas(texto):
        lista_sentencas_texto.append(sentenca)
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                lista_palavras_texto.append(palavra) # cria uma lista de palavras "limpas" (sem pontuação junto das palavras)
                n_caracteres_texto = n_caracteres_texto + len(palavra) # percorre cada palavra da lista de palavras de um texto e soma SOMENTE os caracteres alfanuméricos

    wal = n_caracteres_texto / len(lista_palavras_texto) # média de caracteres por palavra (tamanho médio de cada palavra)
    ttr = n_palavras_diferentes(lista_palavras_texto) / len(lista_palavras_texto) # número de palavras diferentes pelo total de palavras do texto (Relação Type-Token)
    hlr = n_palavras_unicas(lista_palavras_texto) / len(lista_palavras_texto) # número de palavras únicas pelo total de palavras do texto (Razão Hapax Legomana)
    sal = n_caracteres_texto / len(separa_sentencas(texto)) # número de caracteres do texto pelo número de sentenças
    sac = len(separa_frases(texto)) / len(separa_sentencas(texto)) # número de frases do texto pelo número de sentenças
    pal = n_caracteres_texto / len(separa_frases(texto)) # número de caracteres do texto pelo número de frases (tamanho médio de cada frase)

    return [wal, ttr, hlr, sal, sac, pal]    
    
def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor_S = compara_assinatura(calcula_assinatura(textos[0]), ass_cp)
    indice_menor_S = 0

    for i in range(1,len(textos)):
        S = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
        if S < menor_S:
            menor_S = S
            indice_menor_S = i
    print("O autor do texto", indice_menor_S+1, "está infectado com COH-PIAH") # quanto menor o valor de S, maior a similaridade entre os textos
    return indice_menor_S+1
    
def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    avalia_textos(textos, ass_cp)

main()
