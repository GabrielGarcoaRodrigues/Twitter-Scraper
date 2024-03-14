import subprocess
import sys
import importlib.util
import venv  # Importando o módulo venv para criar o ambiente virtual
import os
def check_and_install_package(package_name):
    """
    Verifica se o pacote está instalado e, se não estiver, o instala.
    """
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"{package_name} foi instalado com sucesso.")
        except subprocess.CalledProcessError:
            print(f"Erro ao instalar {package_name}. Verifique sua conexão com a internet ou tente novamente mais tarde.")

# Lista de bibliotecas que você deseja verificar e instalar (se necessário)
bibliotecas_necessarias = ["selenium", "termcolor", "chromedriver_autoinstaller", "xlwt", "openpyxl"]

# Verifica e instala as bibliotecas
for biblioteca in bibliotecas_necessarias:
    check_and_install_package(biblioteca)

# Agora você pode usar as bibliotecas normalmente em seu código!
