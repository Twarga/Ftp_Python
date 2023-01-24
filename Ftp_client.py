import ftplib

ftp =ftplib.FTP()
ftp.connect("127.0.0.1",2121)

ftp.login("Twarga","123")

ftp.cwd('.')
with open("local_file.txt",'rb') as file:
    ftp.storbinary("STOR remote_file.txt", file)
ftp.cwd('.')
ftp.quit()