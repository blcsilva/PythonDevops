import shutil

def verificar_uso_disco(diretorio):
    total, usado, livre = shutil.disk_usage(diretorio)
    uso_percentual = (usado / total) * 100
    return uso_percentual

# Exemplo de uso
uso = verificar_uso_disco('/')
if uso > 90:
    print("Alerta: Uso do disco acima de 90%!")
