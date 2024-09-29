import paramiko

def implantar_aplicacao(servidor, usuario, senha, arquivo):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(servidor, username=usuario, password=senha)
    
    sftp = ssh.open_sftp()
    sftp.put(arquivo, '/caminho/no/servidor/' + os.path.basename(arquivo))
    sftp.close()
    ssh.close()
    print("Aplicação implantada com sucesso.")

# Exemplo de uso
implantar_aplicacao('servidor.com', 'usuario', 'senha', 'aplicacao.zip')
