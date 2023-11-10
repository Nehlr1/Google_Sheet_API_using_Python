import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Setting up Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Opening the Google Sheet by title
spreadsheet_title = "penguins_size"
spreadsheet = client.open(spreadsheet_title)

# Selecting the specific worksheet
worksheet = spreadsheet.get_worksheet(0)  # Index 0 represents the first worksheet

# Getting all values from the worksheet
data = worksheet.get_all_values()

# Creating dataframe
df = pd.DataFrame(data[1:], columns=data[0])
print(df.head())