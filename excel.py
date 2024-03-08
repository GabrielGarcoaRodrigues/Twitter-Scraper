from xlwt import Workbook
import openpyxl

def Excel(data: list):
    wb = openpyxl.Workbook()
    ws = wb.active

    headers = ['URL', 'Date', 'Text', 'Lang', 'Likes', 'Retweets', 'Replies']
    ws.append(headers)

    for tweets in data:
        for tweet in tweets:
            row = [
                tweet['URL'],
                tweet['Date'],
                tweet['Text'],
                tweet['Lang'],
                tweet['Likes'],
                tweet['Retweets'],
                tweet['Replies']
            ]
            ws.append(row)

    wb.save('Excel.xls')
