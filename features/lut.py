from PIL import Image
import math


def cubeIndex(r, g, b):
    return int(r + g * 32 + b * 32 * 32)

def mix(a, b, c):
    return a + (b - a) * (c - math.floor(c))

# img = Image.open("static/1.jpeg") 효율개선
# bitmap = img.load()

fd = open('static/lut/Blue.CUBE') #LUT 불러오기 (CUBE파일 사용)
lines = fd.readlines()
rgbFloatCube = []
cubeDataStart = False
for l in lines:  # CUBE파일 파싱
    if cubeDataStart:
        rgbStr = l.split(" ")
        if len(rgbStr) == 3:
            rgbFloat = (float(rgbStr[0]), float(rgbStr[1]), float(rgbStr[2]))
            rgbFloatCube.append(rgbFloat)
    if l.startswith("#LUT data points"):
        cubeDataStart = True

print(len(rgbFloatCube))
img = Image.open("static/lut/neutral-lut.jpg")  # 이미지 불러오기, 여러개 불러올때 반복문 여기부터
bitmap = img.load()  # 이미지 로딩
print(img.size)

for x in range(img.size[0]):  # LUT 적용
    for y in range(img.size[1]):
        pixelColor = bitmap[x, y]
        red = pixelColor[0] / 255.0 * 31
        green = pixelColor[1] / 255.0 * 31
        blue = pixelColor[2] / 255.0 * 31

        redH = math.ceil(red)
        redL = math.floor(red)

        greenH = math.ceil(green)
        greenL = math.floor(green)

        blueH = math.ceil(blue)
        blueL = math.floor(blue)

        indexH = cubeIndex(redH, greenH, blueH)
        indexL = cubeIndex(redL, greenL, blueL)

        toColorH = rgbFloatCube[indexH]
        toColorL = rgbFloatCube[indexL]

        toR = mix(toColorL[0], toColorH[0], red)
        toG = mix(toColorL[1], toColorH[1], green)
        toB = mix(toColorL[2], toColorH[2], blue)

        toColor2 = (int(toR * 255), int(toG * 255), int(toB * 255))
        bitmap[x, y] = toColor2

img.show()