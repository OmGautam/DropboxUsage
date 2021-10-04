import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def uploadFiles(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.access_token)
        
        f = open(fileFrom,'rb') 
        dbx.files_upload(f.read(),fileTo)

def main():
    access_token = 'UT63PJLuaAwAAAAAAAAAARPJNcOhx_hSmUMx10iLplZWTJ0nRhl33Ux0QVwMUJZD'
    transferData = TransferData(access_token)
    fileFrom = input("Enter file path to transfer: ")
    fileTo = input("Enter full path to upload to dropbox: ")
    transferData.uploadFiles(fileFrom,fileTo)
    print("File has been tranferred")

main()