from os import path
from data.filerepository import *
from domain import finder



def read(path):
    data = read_excel(path)
    line = 0
    for row in data.iterrows():
        filename = data.loc[line, 'nome_arquivo']
        line += 1
        finder.find(filename)