#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

nao = ';   nao    ;'
sim = ';   sim    ;'

# abre os arquivos em modo leitura
file1 = open("rg.txt", "r") # aquivo com 1 rg por linha
datafile = open("seguro.txt", "r") # arquivo a conferir se contem os rg
search = []

# cria o vetor contendo todos os rg
for line in file1:
	line = line.strip()
	search.append(line)


# imprime a quantidade de rg
print (len(search))

row = []
i = 0

# Código a ser melhorado a escrita
# diz se o rg foi ou não localizado e mostra o rg
while i<len(search):
        MsgOk= sim + search[i]
        MsgNok= nao + search[i]
        def check():
                for line in datafile:
                        if search[i] in line:
                                found = True
                                line = line.strip()
                                row.append(line)
                                break
                        else:
                                found = False
                return found

        if check():
            print( MsgOk)
        else:
            print (MsgNok)
        i = i + 1

# imprime toda a linha em que aparece o rg
i = 0
while i < len(row):
	print(row[i])
	i = i + 1
	
print( "fim")
