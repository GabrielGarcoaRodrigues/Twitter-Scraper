import datetime

# Data de início (1 de janeiro de 2023)
start_date = datetime.date(2023, 1, 1)

# Data final (31 de dezembro de 2023)
end_date = datetime.date(2023, 1, 2)

# Lista para armazenar as URLs
urls = []

# Loop através de cada dia em 2023
current_date = start_date

while end_date != datetime.date(2023, 12, 31):
    # Formate a data no formato yyyy-mm-dd
    formatted_date = current_date.strftime("%Y-%m-%d")
    formatted_end_date = end_date.strftime("%Y-%m-%d")
    # Crie a URL para o dia atual
    url = f"https://twitter.com/search?q=Lollapalooza%20OR%20Lolapalooza%20lang%3Apt%20until%3A{formatted_end_date}%20since%3A{formatted_date}&src=typed_query&f=live"
    # Adicione a URL à lista de URLs
    urls.append(url)
    # Avance para o próximo dia
    current_date += datetime.timedelta(days=1)
    end_date += datetime.timedelta(days=1)

# Imprima as URLs geradas
for url in urls:
    print(url)
