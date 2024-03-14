@echo off
echo Ativando o ambiente virutal...

REM Criar um diretório para o ambiente virtual caso não exista
if not exist "venv" mkdir venv

REM Criar o ambiente virtual dentro do diretório venv
python -m venv venv

REM Ativar o ambiente virtual
call venv\Scripts\activate.bat

echo Verificando as bibliotecas...
REM Executar o arquivo index.py no ambiente virtual
python scripts\install.py

REM Mensagem indicando que o ambiente está pronto para uso
echo Ambiente Virtual criado e dependencias instaladas. Ambiente ativado.

REM Mantém o prompt aberto no ambiente virtual

echo Executando o script...
REM Executa o script principal
python scripts\index.py


cmd /k
