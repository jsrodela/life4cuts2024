from PIL.Image import Image

# 숫자 수정 필요!!!

def combine_photo(photo, qrcode, frame):

    w = 523
    h = 400

    pos = {(74, 64), (614, 64), (1154, 64), (74, 480)}
    qr_pos = (23, 15)

    background = Image.open(f'frame{frame}.png').convert("RGBA")
    for i in range(4):
        photo = photo[i].convert("RGBA")

        photo = photo.resize((h*16//9, h)) # 사진 가로-세로 비율

        w_off = photo[i].width - w # 너비 오프셋

        photo = photo.crop((w_off//2, 0, photo[i].width - w_off//2, h))

        background.paste(photo, pos[i])

    qr = qrcode.convert("RGBA")
    background.paste(qr, qr_pos)
    return background