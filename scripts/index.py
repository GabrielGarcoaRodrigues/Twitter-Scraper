from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from logger import Logger
import json
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time
from tweet import Tweet
from excel import Excel
from links import Atualiza_Parametros

def main():
    # Verifica o token de acesso files -> conf.json -> token
    if not conf["token"]:
        log.warning("Error accessing the Token, update the file './files/conf.json'")
        return

    driver = open_driver(conf["headless"], conf["userAgent"])
    driver.get("https://twitter.com/")
    set_token(driver, conf["token"])
    driver.get("https://twitter.com/")
    log.warning("Getting started...")
    
    # Le o arquivo Criar_URL.txt e atualiza os parametros URLs.txt
    Atualiza_Parametros()

    # Links para cada busca do twitter
    url_file_name = 'files/URLs.txt'

    # Numero de tweets que deseja buscar em cada URL
    # Abre o arquivo
    with open('Criar_URL.txt', 'r') as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

    # Cria um dicionário para armazenar as variáveis
    variaveis = {}

    # Itera sobre cada linha do arquivo
    for linha in linhas:
        # Separa o nome da variável e seu valor
        nome, valor = linha.strip().split(' = ')
        # Armazena a variável no dicionário
        variaveis[nome] = valor
    
    number_tweets = int(variaveis['Tweets'])
    
    
    data = []
    aux = []
    listaErros = []
    
    # Lê os links de um arquivo
    url = read_urls_from_file(url_file_name)

    # Procura os tweets em cada link
    for link in url:
        log.warning(f"\nSearching tweets from {link}...")
        aux = profile_search(driver, link, number_tweets)
        if aux == []:
            log.error(f"URL Vazia ou Erro {link}")
            listaErros.append(link)
        else:
            data.append(aux)

    log.warning("Saving...")

    # Salva os tweets em um arquivo excel, json e txt para as URLs que deram erro
    Excel(data)
    json.dump(data, open("./files/temp.json", "w"))
    open("URLs_Vazias.txt", "w").write("\n".join(listaErros))
    
    log.success("Finished!")

# Função para ler os links de um arquivo
def read_urls_from_file(url_file_name):
    with open(url_file_name, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

# Função para buscar os os dados dos tweets
def profile_search(driver: webdriver.Chrome, url : str, number_tweets : int):
    driver.get(url)
    Ad = []
    results = []

    while len(results) < number_tweets:
        # Função para buscar os tweets
        time.sleep(2)
        tweet = Tweet(driver, Ad)
        
        data = {}

        data["URL"] = tweet.get_url()
        data["User Name"] = tweet.get_user_name()
        data["User @"] = tweet.get_user()
        data["Date"] = tweet.get_date()
        data["Time"] = tweet.get_time()
        data["Text"] = tweet.get_text()
        data["Lang"] = tweet.get_lang()
        data["Likes"] = tweet.get_num_likes()
        data["Retweets"] = tweet.get_num_retweet()
        data["Replies"] = tweet.get_num_reply()

        if data["URL"] == "":
            break
        else:
            results.append(data)
            log.info(f"{len(results)} : {data['URL']}")
                
    return results

def open_driver(headless: bool, agent: str) -> webdriver.Chrome:
    options = Options()
    options.add_argument('--log-level=3')
    options.add_argument('ignore-certificate-errors')

    if headless:
        options.add_argument('--headless')

    options.add_argument(f"user-agent={agent}")

    driver = webdriver.Chrome(options=options)
    return driver

def set_token(driver: webdriver.Chrome, token: str) -> None:
    src = f"""
            let date = new Date();
            date.setTime(date.getTime() + (7*24*60*60*1000));
            let expires = "; expires=" + date.toUTCString();

            document.cookie = "auth_token={token}"  + expires + "; path=/";
        """
    driver.execute_script(src)

def load_conf() -> dict:
    with open("./files/conf.json", "r") as file:
        return json.loads(file.read())

if __name__  == "__main__":
    log = Logger()
    try:
        conf = load_conf()
    except Exception:
        log.warning("Sorry and error occured, Please check your config file")
        input("\n\tPress any key to exit...")
    else:
        main()