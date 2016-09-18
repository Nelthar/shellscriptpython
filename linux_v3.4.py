#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desenvolvimento Aberto
# shell.py


# Importar modulo do sistema operacional
import os, pygame
pygame.init()

#módulo subprocess é necessário para executar comandos externos ao Python
import subprocess 

#relação com os comandos deste sistema
import commands 

#instalar screenfetch
var = os.system("sudo apt-get install gedit")
print var

#limpa tela
var = os.system("clear")
print var

#variável var pegará o return do comando executado (0 se deu certo o comando e diferente de 0 se deu errado)
var = os.system("sudo apt-get update")
print var

#limpa tela
var = os.system("clear")
print var

#atualiza a lista de pacotes disponíveis baseando-se nas fontes listadas no arquivo list-sources
var = os.system("sudo apt-get update") 
print var

#limpa tela
var = os.system("clear")
print var

#atualiza pacotes
var = os.system("sudo apt-get upgrade -s") 
print var

#limpa tela
var = os.system("clear")
print var

#verifica se existem dependências erradas
var = os.system("sudo apt-get check")
print var

#limpa tela
var = os.system("clear")
print var

#instala novos pacotes
var = os.system("sudo apt-get -f install -s") 
print var

#limpa tela
var = os.system("clear")
print var

#Reparar o apt-get
var = os.system("sudo apt-get -f instal") 
print var

#limpa tela
var = os.system("clear")
print var

#Reparar o dpkg
var = os.system("sudo dpkg --configure -a") 
print var

#limpa tela
var = os.system("clear")
print var

#apaga pastas e diretórios obtidos por downlad durante a instalação de pacotes
var = os.system("sudo apt-get clean")
print var

#limpa tela
var = os.system("clear")
print var

#remove automaticamente todos os pacotes não utilizados do sistema, útil após realizar várias atualizações pois deixa o sistema mais limpo
var = os.system("sudo apt-get autoremove -s")
print var

#limpa tela
var = os.system("clear")
print var

#remove automaticamente todos os pacotes não utilizados do sistema, útil após realizar várias atualizações pois deixa o sistema mais limpo
var = os.system("sudo apt-get autoclean -s")
print var

#limpa tela
var = os.system("clear")
print var

#remove pacotes
var = os.system("sudo apt-get -f remove -s")
print var

#limpa tela
var = os.system("clear")
print var

#Instalação headless do Dropbox via linha de comando
return_code = subprocess.call('cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -', shell=True)

#xecute o Dropbox daemon na pasta .dropbox-dist recém-criada
return_code = subprocess.call('~/.dropbox-dist/dropboxd', shell=True)

#Criar um aplicativo de inicialização
return_code = subprocess.call('sh -c ~/.dropbox-dist/dropboxd', shell=True)

#instalar screenfetch
var = os.system("sudo apt-get install screenfetch")
print var

String="Quando abrir, adicione a palavra screenfetch, na última linha. Salve o arquivo e experimente abrir o terminal novamente. Pressione enter para continuar"
print String

#Para automatizar, e toda vez em que o terminal for aberto, o screenfetch seja executado
#return_code = subprocess.call('sudo gedit ~/.bashrc', shell=True)	

#Instalar adobe flashplayer
var = os.system("sudo apt-get install adobe-flashplugin")
print var

#limpa tela
var = os.system("clear")
print var

#apagar qualquer versão anterior do Franz
return_code = subprocess.call('sudo rm -Rf /opt/franz* && sudo rm -Rf /usr/bin/franz && sudo rm -Rf /usr/share/applications/franz.desktop', shell=True)	

#baixar Franz 64 bits
return_code = subprocess.call('wget https://github.com/meetfranz/franz-app/releases/download/4.0.4/Franz-linux-x64-4.0.4.tgz', shell=True)	

#criando pasta para o Franz
return_code = subprocess.call('sudo mkdir /opt/franz', shell=True)	

#comando a seguir para descompactar o arquivo baixado
return_code = subprocess.call('sudo tar -vzxf Franz-linux-x64-4.0.4.tgz -C /opt/franz/', shell=True)	

#atalho para facilitar a execução do programa
return_code = subprocess.call('sudo ln -sf /opt/franz/Franz /usr/bin/franz', shell=True)	

#crie um lançador para o programa
return_code = subprocess.call('echo -e [Desktop Entry]\n Version=1.0\n Name=franz\n Exec=/opt/franz/Franz\n Icon=/opt/franz/resources/app.asar.unpacked/assets/franz.png\n Type=Application\n Categories=Application | sudo tee /usr/share/applications/franz.desktop', shell=True)	

#atalho na área de trabalho
return_code = subprocess.call('sudo chmod +x /usr/share/applications/franz.desktop', shell=True)	

#executar franz
return_code = subprocess.call('franz', shell=True)	

#limpa tela
var = os.system("clear")
print var

#instalar chrome
return_code = subprocess.call('sudo apt-get install google-chrome-stable', shell=True)	

#limpa tela
var = os.system("clear")
print var

#add repositorio sm player
return_code = subprocess.call('sudo add-apt-repository ppa:rvm/smplayer', shell=True)	

#update
return_code = subprocess.call('sudo apt-get update', shell=True)	

#limpa tela
var = os.system("clear")
print var

#baixar o sm player
return_code = subprocess.call('sudo apt-get install smplayer', shell=True)

#limpa tela
var = os.system("clear")
print var

#instalar virtualbox
return_code = subprocess.call('sudo apt-get install virtualbox', shell=True)

#instalar a virtualbox
return_code = subprocess.call('sudo apt-get install virtualbox-qt', shell=True)

#limpa tela
var = os.system("clear")
print var

#instalar a docky
return_code = subprocess.call('sudo apt-get install docky', shell=True)

#Adicione a chave de assinatura do repositório Spotify para ser capaz de verificar os pacotes baixados
return_code = subprocess.call('sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BBEBDCB318AD50EC6865090613B00F1FD2C19886', shell=True)

#Adicione o repositório Spotify
return_code = subprocess.call('echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list', shell=True)

#Atualização de pacotes disponíveis
return_code = subprocess.call('sudo apt-get update', shell=True)

#instalar ao spotify
return_code = subprocess.call('sudo apt-get install spotify-client', shell=True)

#limpa tela
var = os.system("clear")
print var
	
String="Configuração terminou"
print String