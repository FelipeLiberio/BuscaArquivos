import os
from data.filerepository import get_source
from data.logs import save_log
import shutil

DIRET = get_source('645359')

def find_file(filename):
    for roots, dirs, files in os.walk(DIRET):

        if filename in files:
            save_log(f'Arquivo {filename} encontrado em {roots}')
            copy_file(filename)
            break

        else:
            save_log(f'Arquivo {filename} não encontrado no diretório {roots}')


def find(filename):
    find_file(filename)


def copy_file(filename):
    source_directory = rf'/home/felipe/PycharmProjects/BuscaArquivos/data/files/{filename}'
    destination_directory = rf'/home/felipe/Testes/{filename}'
    save_log(f'Realizada copia de {filename} para o diretório {source_directory}')

    shutil.copy(source_directory, destination_directory)
