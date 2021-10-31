from datetime import *

today = str(datetime.now())
date = today[0:10]

def save_log(log):
    logfile = open(f'/home/felipe/PycharmProjects/BuscaArquivos/data/logs/{date}.txt','a')
    logfile.write(f'{today[0:19]} -> {log}\n')