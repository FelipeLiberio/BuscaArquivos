from os import DirEntry
import pandas as pd
import xml.etree.ElementTree as ET


def read_excel(path):
    data = pd.read_excel(path)
    return data

def read_xml(codVend):
    tree = ET.parse('/home/felipe/PycharmProjects/BuscaArquivos/data/teste.xml')
    root = tree.getroot()
    for child in root:
        if child.attrib.get('id') == codVend:            
            return(child.find('diretorio').text)
        else:
            print('Codigo vendedor não encontrado')


def get_source(codVend):
    diret = read_xml(codVend)
    return diret
