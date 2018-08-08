from pytube import YouTube
import sys, os
loc = raw_input('link: ')

yt = YouTube(loc)
try:
    f = yt.streams.get_by_itag(251)
    f.download()
    print f.abr
except:
    try:
        f = yt.streams.get_by_itag(171)
        f.download()
        print f.abr
    except:
        try:
            f = yt.streams.get_by_itag(250)
            f.download()
            print f.abr
        except:
            try:
                f = yt.streams.get_by_itag(249)
                f.download()
                print f.abr
            except:
                print "well I'm dumb"
                sys.exit()

os.system('python convertWEBMtoMP3.py')
