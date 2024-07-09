import os
import shutil
import PIL
from PIL import Image

downloadDir = "./static/organizerTest/download"  # 임시 디렉토리임
serverDir = "./static/organizerTest/server"  # 임시 디렉토리임

while True:
    if len(os.listdir(downloadDir)) > 0:

        dirContent = os.listdir(downloadDir)
        dirContent.sort()
        imgFileName = os.path.splitext(dirContent[0])[0]  # 교체필요

        UUID = imgFileName[-36:]
        copies = imgFileName[4:5]
        print(copies, UUID)

        try:
            os.mkdir(f"{serverDir}/{UUID}")
        except FileNotFoundError:
            os.mkdir(f"{serverDir}")
            os.mkdir(f"{serverDir}/{UUID}")

        shutil.move(os.path.join(downloadDir, dirContent[0]), os.path.join(f"{serverDir}/{UUID}", dirContent[0]))

        for i in range(1, len(dirContent)):
            shutil.move(os.path.join(downloadDir, dirContent[i]), os.path.join(f"{serverDir}/{UUID}", dirContent[i]))
        print(f"File Moved. >> Session {UUID}")

        img = PIL.Image.open(f"{serverDir}/{UUID}/{dirContent[0]}").convert("RGB")
        img.save(f"{serverDir}/{UUID}/{imgFileName}.pdf")
        print(f"pdf file created. >> Session{UUID}")

