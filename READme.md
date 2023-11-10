# Google Sheet API using Python

This repository contains code examples for interacting with Google Sheets using the Google Sheet API and Python.

## Getting Started

Clone this repository and install the requirements:

```
git clone https://github.com/Nehlr1/Google_Sheet_API_using_Python.git
cd Google_Sheet_API_using_Python
pip install -r requirements.txt
```

You must set up a project in the Google Cloud Console and activate the Google Sheets API before you can build the `credentials.json` file for the API. Take these actions:

### Step 1: Create a Project in Google Cloud Console

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the project dropdown at the top of the page, then click on "New Project."
3. Enter a name for your project and click "Create."

### Step 2: Enable the Google Sheets API

1. In the Cloud Console, click on beside Google Cloud logo using the left sidebar.
2. Click on More Products Dropdown and select APIs and Services and then select ENABLE APIS AND SERVICES.
3. Search for "Google Sheets API" in the search bar.
4. Select "Google Sheets API" from the results.
5. Click the "Enable" button.

### Step 3: Create Service Account Credentials

1. In the Cloud Console, navigate to "APIs & Services" > "Credentials" using the left sidebar.
2. Click on the "Create Credentials" dropdown and select "Service account"
3. Under "Service account," create a new service account like "Google sheet API".
4. For "Role," choose "Project" > "Editor" to give the service account access to your entire project.
5. Once the Service account is created, using the left sidebar, click on the "Service account logo" and you will see the created service account. 
6. Click on the action button and select "manage keys"
7. Click the "Create" button choosing the "Key type" as choose JSON. This will download a JSON file containing your credentials.

### Step 4: Save and Use Your Credentials

In the directory containing your Python script, save the downloaded JSON file as `credentials.json`. This file is what your Python script will use to authenticate itself.

Since your `credentials.json` file includes important information, make sure you keep it private and don't share it with the public.

## Jupyter Notebook

The Jupyter Notebook google_sheet_api.ipynb contains examples of:

- Reading data from a Google Sheet
- Adding data to a Google Sheet 
- Updating cells

## Python Script

The Python script google_sheet_api.py shows how to perform the same operations programmatically without a notebook.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.