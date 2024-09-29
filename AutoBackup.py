import shutil  # Importa o módulo para operações de arquivo de alto nível
import os      # Importa o módulo para interações com o sistema de arquivos
import datetime # Importa o módulo para manipulação de datas e horas

def backup(source, destination):
    # Obtém a data e hora atuais no formato "YYYYMMDD_HHMMSS"
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Cria o caminho da nova pasta de backup, incluindo a data e hora
    backup_folder = os.path.join(destination, f"backup_{now}")
    
    # Copia recursivamente o diretório de origem para a nova pasta de backup
    shutil.copytree(source, backup_folder)
    
    # Exibe uma mensagem confirmando que o backup foi realizado com sucesso
    print(f"Backup realizado em: {backup_folder}")

# Exemplo de uso da função backup
# Substitua '/caminho/para/origem' e '/caminho/para/destino' pelos caminhos desejados
backup('/caminho/para/origem', '/caminho/para/destino')
