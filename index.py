from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from logger import Logger
import json
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time
from tweet import Tweet
from excel import Excel


def main():
    if not conf["token"]:
        log.warning("Error accessing the Token, update the file './files/conf.json'")
        return

    driver = open_driver(conf["headless"], conf["userAgent"])
    driver.get("https://twitter.com/")
    set_token(driver, conf["token"])
    driver.get("https://twitter.com/")

    log.warning("Getting started...")
    
    url_file_name = 'Links.txt'
    # url_file_name = 'link.txt'

    number_file_name = 'Number_tweets.txt'
    data = []

    url = read_urls_from_file(url_file_name)
    with open(number_file_name, 'r') as file:
        number_tweets = int(file.read())

    for link in url:
        log.warning(f"Searching tweets from {link}...")
        data.append(profile_search(driver, link, number_tweets))

    log.warning("Saving...")
    Excel(data)
    json.dump(data, open("./files/temp.json", "w"))
    log.warning("Finished!")


def read_urls_from_file(url_file_name):
    with open(url_file_name, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

def profile_search(driver: webdriver.Chrome, url : str, number_tweets : int):
    time.sleep(2)
    driver.get(url)
    Ad = []
    results = []

    log.warning("Searching...")

    while len(results) < number_tweets:
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


