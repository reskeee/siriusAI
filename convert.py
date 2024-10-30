from moviepy.editor import *
import os

def MP4ToMP3(mp4, mp3):
    project_dir = os.path.dirname(__file__)
    FILETOCONVERT = AudioFileClip(f"{project_dir}/{mp4}")
    FILETOCONVERT.write_audiofile(f"{project_dir}/{mp3}")
    FILETOCONVERT.close()

# VIDEO_FILE_PATH = "/Full/File/Path/ToSong.mp4"
# AUDIO_FILE_PATH = "/Full/File/Path/ToSong.mp3"

# MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
# MoviePy - Writing audio in /Full/File/Path/ToSong.mp3
# MoviePy - Done.                     

if __name__ == "__main__":
    MP4ToMP3("video/videoplayback.mp4", "audio/convert.mp3")
    # print(os.path.dirname(__file__))
