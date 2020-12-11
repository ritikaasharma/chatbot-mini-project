from pytube import YouTube
import os

try:
    link = input('Enter the link of video to be downloaded: ')
    yt = YouTube(link)
except:  
    print("Connection Error")

title = yt.title

print("Available streams for downloading : \n")
for stream in yt.streams:
    print(stream)

cf=os.path.dirname(__file__)
cf2=cf+"/"+title+".mp4"
dp="Downloading : "+title+" ..."
dc="Download Completed !"

while True:
    vd=int(input("Select video quality : 1. Highest resolution available 2. 1080p 3. 720p 4. 480p 5. Lowest resolution available\n"))

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
        print("Error: Progressive Stream Unavailable")

os.startfile(cf2)       