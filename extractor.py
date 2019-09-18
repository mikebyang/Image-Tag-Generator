import gspread
from oauth2client.service_account import ServiceAccountCredentials
from glob import glob

def tex_extract(name):
    #use credentials and access google sheets
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(name).sheet1
    #returns quote, author
    return sheet.col_values(1), sheet.col_values(2)   

def img_extract():
    return glob('./Images/*')