import os
import hashlib
import time
from inotify_simple import INotify, flags

# Função para monitorar criação de usuários e logins no /var/log/auth.log
def monitor_auth_log():
    print("Monitorando criação de usuários e logins suspeitos...")
    with open('/var/log/auth.log', 'r') as f:
        f.seek(0, 2)  # Vai para o fim do arquivo
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            if "new user" in line or "sudo" in line:
                print(f"Atividade suspeita detectada: {line.strip()}")

# Função para monitorar alterações em arquivos sensíveis (exemplo: /etc/hosts)
def monitor_file_changes():
    print("Monitorando alterações em arquivos sensíveis...")
    inotify = INotify()
    watch_flags = flags.MODIFY
    wd = inotify.add_watch('/etc/hosts', watch_flags)

    while True:
        for event in inotify.read():
            print(f"Arquivo {event.wd} modificado")

# Função para analisar downloads e verificar hashes MD5
def monitor_downloads():
    print("Monitorando downloads e verificando hashes...")
    download_folder = '/home/user/Downloads'  # Modifique para o diretório correto

    while True:
        for filename in os.listdir(download_folder):
            file_path = os.path.join(download_folder, filename)
            if os.path.isfile(file_path):
                hash_md5 = hashlib.md5()
                with open(file_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
                print(f"Arquivo: {filename} - MD5 Hash: {hash_md5.hexdigest()}")
        time.sleep(10)  # Verifica a pasta de downloads a cada 10 segundos

# Função principal para rodar os monitores em paralelo
def main():
    try:
        # Rodar cada função em paralelo
        monitor_auth_log()  # Monitorar criação de usuários e logins
        monitor_file_changes()  # Monitorar arquivos sensíveis
        monitor_downloads()  # Verificar downloads
    except KeyboardInterrupt:
        print("Monitoramento encerrado.")

if __name__ == "__main__":
    main()


