from pytube import YouTube

while(True) :
    url = input("Masukkan Link :")

    my_video = YouTube(url)
    print("Apakah judul video yang didownload :")
    print(my_video.title)

    jawab = input("Y/N :")
    if(jawab.lower() =="y") :
        break

my_video = my_video.streams.get_highest_resolution()
my_video.download()
