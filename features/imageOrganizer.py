import os
import shutil

async def ()
downloadDir = "./static/organizerTest/download"  # 임시 디렉토리임
serverDir = "./static/organizerTest/server"  # 임시 디렉토리임

dirContent = os.listdir(downloadDir)
dirContent.sort()
imgFileName = os.path.splitext(dirContent[0])[0]

fileType = imgFileName[:3]
UUID = imgFileName[-36:]
copies = imgFileName[4:5]

os.mkdir(f"{serverDir}/{UUID}")

shutil.move(os.path.join("./organizerTest", "download"), os.path.join(f"{serverDir}", f"{UUID}"))


print(fileType, copies, UUID)