from xlwt import Workbook
import openpyxl

def Excel(data: list):
    wb = openpyxl.Workbook()
    ws = wb.active
    # Cria o cabeçalho
    headers = ['URL', 'User Name', 'User @', 'Date', 'Time', 'Text', 'Lang', 'Likes', 'Retweets', 'Replies']
    ws.append(headers)

    for tweets in data:
        for tweet in tweets:
            row = [
                tweet['URL'],
                tweet['User Name'],
                tweet['User @'],
                tweet['Date'],
                tweet['Time'],
                tweet['Text'],
                tweet['Lang'],
                tweet['Likes'],
                tweet['Retweets'],
                tweet['Replies']
            ]
            ws.append(row)

    wb.save('Excel.xls')
