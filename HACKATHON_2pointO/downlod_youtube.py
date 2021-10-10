from pytube import YouTube
myvideo=YouTube("https://www.youtube.com/watch?v=ULEQb_l-N08 ")
print("\nSearching...")
# print("video streams")
# print(myvideo.streams.all)
n=myvideo.title
print("Title Name: ", n)
print("\n")
print("Wait until download is finished")
print("Loding...")
myvideo.streams.get_highest_resolution().download('/home/navgurukul20/Videos')
print("Video is downloaded!! : )")