import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Setting up Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Opening the Google Sheet by title
spreadsheet_title = "Result_Students"
spreadsheet = client.open(spreadsheet_title)

# Selecting the specific worksheet
worksheet = spreadsheet.get_worksheet(0)  # Index 0 represents the first worksheet

# Getting all values from the worksheet
data = worksheet.get_all_values()
print(data)

# Adding new data
new_data = [
    ['Ahmed', '102', 'Math ', '86'],
    ['Ahmed', '102', 'Physics', '84'],
    ['Ahmed', '102', 'Biology', '82'],
    ['Ahmed', '102', 'Geography', '86'],
    ['Ahmed', '102', 'Computer Science', '84'],
    ['Ahmed', '102', 'Islamic History', '89'],
    ['Ahmed', '102', 'Chemistry', '89'],
    ['Ahmed', '102', 'English', '85']
]

worksheet.append_rows(new_data)

print("Data added successfully.")
data = worksheet.get_all_values()
print(data)

# Data to be updated
update_data = ['Ahmed', '102', 'Computer Science', '94']

# Manually specifying column indices based on the order of columns
name_index = 1
roll_index = 2
subject_index = 3

# Iterating through the rows and find the matching one
for row_number, row in enumerate(worksheet.get_all_values(), start=1):
    if (
        row[name_index - 1] == update_data[0]
        and row[roll_index - 1] == update_data[1]
        and row[subject_index - 1] == update_data[2]
    ):
        # Updating the data in the specified cell
        worksheet.update("D{}".format(row_number), [[update_data[3]]])  # Updating the Marks to 94
        print("Data updated successfully.")
        break

data = worksheet.get_all_values()
print(data)

# Creating dataframe
df = pd.DataFrame(data[1:], columns=data[0])
df