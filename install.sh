#!/bin/bash

# Atualizar pacotes
echo "Atualizando pacotes..."
sudo apt update

# Instalar dependências
echo "Instalando dependências necessárias..."
sudo apt install -y python3 python3-pip inotify-tools

# Instalar pacotes Python necessários
pip3 install inotify_simple

# Tornar o script de monitoramento executável
chmod +x scripts/monitor_unificado.py

echo "Instalação concluída! Para iniciar o monitoramento, execute o script:"
echo "sudo python3 scripts/monitor_unificado.py"

