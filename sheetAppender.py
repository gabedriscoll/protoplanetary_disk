def main(modelname, chival):
    import gspread
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    from google.oauth2.service_account import Credentials

    scopes = ['https://www.googleapis.com/auth/spreadsheets',
              'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file('client_key.json', scopes=scopes) # using existing creds file

    gc = gspread.authorize(credentials) # authorize program to do things

    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    gs = gc.open_by_key('1BuyxFfV0C_RqYA_5UKN6eLL2XMXL2SHtLsfW-oIPg88') # whatever the spreadsheet key is (needs to be set to public edit)

    results = gs.worksheet('Results') # needs to have a sheet called Results -- I think this line is redundant
    chival = float(chival)
    vals = [[modelname, chival]]
    gs.values_append('Results', {'valueInputOption': 'RAW'}, {'values': vals}) # append to the sheet
