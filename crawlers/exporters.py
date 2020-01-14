import gspread
from oauth2client.service_account import ServiceAccountCredentials
from scrapy.exporters import BaseItemExporter

class GoogleSheetItemExporter(BaseItemExporter):
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('google_client_secret.json', scope)
        gc = gspread.authorize(credentials)
        self.spreadsheet = gc.open('OnlineJobs')
        self.worksheet = self.spreadsheet.sheet1

    def export_item(self, item):
        self.worksheet.append_row([ item['job_type'], item['position'], item['link'] ])