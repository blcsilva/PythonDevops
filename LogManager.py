import os
import glob

def rotacionar_logs(diretorio, limite):
    for arquivo in glob.glob(os.path.join(diretorio, '*.log')):
        if os.path.getsize(arquivo) > limite:
            os.rename(arquivo, f"{arquivo}.old")
            print(f"Log rotacionado: {arquivo}")

# Exemplo de uso
rotacionar_logs('/caminho/para/logs', 10 * 1024 * 1024)  # 10 MB
