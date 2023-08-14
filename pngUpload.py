from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import sys

uploadFile = str(sys.argv[1])

folder = str(sys.argv[2])

if folder == 'SEDs':
    folderPath = '1p0pY3lRDMwjC1l45dDilrAfNQbdZ6OaZ'
if folder == 'Contours':
    folderPath = '1NLDl8hBk0mPldWOexq2wymRM2t_DjPW6'
if folder == 'Images':
    folderPath = '1PCvCOnmhBR13AAL45B9GlC0sHl9OYKft'


gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.json")
if gauth.credentials is None:
	gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
	gauth.Refresh()
else:
	gauth.Authorize()
gauth.SaveCredentialsFile("credentials.json")

drive = GoogleDrive(gauth)
filetitle = uploadFile.split("/")[-1]

gfile = drive.CreateFile({'parents': [{'id': folderPath}]})
gfile.SetContentFile(uploadFile)
gfile.Upload()
gfile['title'] = filetitle
gfile.Upload()
