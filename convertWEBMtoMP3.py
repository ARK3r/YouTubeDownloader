import glob, os
from pydub import AudioSegment

for file in glob.glob("*.webm"):
    name = file.replace(".webm", "").replace(" (Official Audio)", "").replace(" Official Audio", "") + ".mp3"

    audio = AudioSegment.from_file(file, format="webm")
    audio.export(name, format="mp3")
    print ("\"" + name + "\"" + " created")

    os.remove(file)
    print ("\"" + file + "\"" + " removed")

