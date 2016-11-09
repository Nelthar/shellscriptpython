#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Desenvolvimento Aberto
# shell.py

 
# Importar modulo do sistema operacional
import os

#relação com os comandos deste sistema
import subprocess 
 
#variável var pegará o return do comando executado (0 se deu certo o comando e diferente de 0 se deu errado)

var = os.system("sudo apt-get update")
print(var)

#atualiza a lista de pacotes disponíveis baseando-se nas fontes listadas no arquivo list-sources
var = os.system("sudo apt-get update") 
print(var)

#atualiza pacotes
var = os.system("sudo apt-get upgrade -s") 
print(var)

#verifica se existem dependências erradas
var = os.system("sudo apt-get check")
print(var)

#instala novos pacotes
var = os.system("sudo apt-get -f install -s") 
print(var)

#apaga pastas e diretórios obtidos por downlad durante a instalação de pacotes
var = os.system("sudo apt-get clean")
print(var)

#remove automaticamente todos os pacotes não utilizados do sistema, útil após realizar várias atualizações pois deixa o sistema mais limpo
var = os.system("sudo apt-get autoremove -s")
print(var)

#remove automaticamente todos os pacotes não utilizados do sistema, útil após realizar várias atualizações pois deixa o sistema mais limpo
var = os.system("sudo apt-get autoclean -s")
print(var)

#remove pacotes
var = os.system("sudo apt-get -f remove -s")
print(var)
