import os
import webbrowser
import time

while(0==0):
    webbrowser.open("https://www.youtube.com/watch?v=EBC5F_JaEMs&t=1s", new=1, autoraise=False)
    webbrowser.open("https://www.youtube.com/watch?v=9c2vhVl24Wk&t=3s", new=1, autoraise=False)
    webbrowser.open("https://www.youtube.com/watch?v=TS7bK9_wv3g&t=1s", new=1, autoraise=False)
    webbrowser.open("https://www.youtube.com/watch?v=6HLIOeGSdUY&t=1s", new=1, autoraise=False)
    webbrowser.open("https://www.youtube.com/watch?v=hdxiH4Co4qc&t=66s", new=1, autoraise=False)
    #webbrowser.open("Your.YT.video.URL=number_of_seconds_that_want_to_start", new=1, autoraise=False)

    time.sleep(200)

    os.system('killall -KILL firefox')
