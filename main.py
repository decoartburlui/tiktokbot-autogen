"
Auto TikTok Poster
Limba: Română
"
import os

def genereaza_postare():
    imagine = "output.jpg"
    voiceover = "audio.mp3"
    os.system(f"ffmpeg -loop 1 -i {imagine} -i {voiceover} -c:v libx264 -t 15 -pix_fmt yuv420p -vf scale=1080:1920 postare.mp4")

if __name__ == "__main__":
    genereaza_postare()
