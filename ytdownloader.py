from pytube import YouTube
import os
from talkbot2 import User_name

import MySQLdb

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "#root9694",
    database = "chatbotdb"
)

cursor = db.cursor()

try:
    link_db = "Enter the link of video to be downloaded: "
    link = input(link_db)
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(link,User_name))
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(link_db,User_name))
    yt = YouTube(link)
except:  
    conn_err = "Connection Error"
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(conn_err,User_name))
    print(conn_err)

title = yt.title

avlbl_db = "Available streams for downloading : "
print("Available streams for downloading : \n")
for stream in yt.streams:
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(stream,User_name))
    print(stream)

cf=os.path.dirname(__file__)
cf2=cf+"/"+title+".mp4"
dp="Downloading : "+title+" ..."
dc="Download Completed !"
dp_db = "Downloading .... "
dc_db = "Download Completed !"
cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(dp_db,User_name))
cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(dc_db,User_name))

while True:
    quality = "Select video quality : 1. Highest resolution available 2. 1080p 3. 720p 4. 480p 5. Lowest resolution available\n"
    cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(quality,User_name))
    vd=int(input(quality))
    cursor.execute("INSERT INTO chathistory (User) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(vd,User_name))
    try:
        if vd==1:
            stream = yt.streams.get_highest_resolution()
            print(dp)
            stream.download(output_path=cf,filename=title)
            print(dc)
            break
        elif vd==2:
            stream = yt.streams.filter(progressive=True).get_by_resolution("1080p")
            print(dp)
            stream.download(output_path=cf,filename=title)
            print(dc)
            break
        elif vd==3:
            stream = yt.streams.filter(progressive=True).get_by_resolution("720p")
            print(dp)
            stream.download(output_path=cf,filename=title)
            print(dc)
            break
        elif vd==4:
            stream = yt.streams.filter(progressive=True).get_by_resolution("480p")
            print(dp)
            stream.download(output_path=cf,filename=title)
            print(dc)
            break
        elif vd==5:
            stream = yt.streams.get_lowest_resolution()
            print(dp)
            stream.download(output_path=cf,filename=title)
            print(dc)
            break

    except:
        err_msg = "Error: Progressive Stream Unavailable"
        print(err_msg)
        cursor.execute("INSERT INTO chathistory (Cia) VALUES (%s) ON DUPLICATE KEY UPDATE Name=%s",(err_msg,User_name))
        

#os.startfile(cf2)       
