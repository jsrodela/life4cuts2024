from PIL.Image import Image

# QR코드 위치 수정 필요!!!

def combine_photo(photo, qrcode):

    '''
    background = Image.open(f'frame{frame}.png').convert("RGBA")
    
    w = 523
    h = 400

    pos = {(74, 64), (614, 64), (1154, 64), (74, 480)}

    
    for i in range(4):
        photo = photo[i].convert("RGBA")

        photo = photo.resize((h*16//9, h)) # 사진 가로-세로 비율

        w_off = photo[i].width - w # 너비 오프셋

        photo = photo.crop((w_off//2, 0, photo[i].width - w_off//2, h))

        background.paste(photo, pos[i])
    '''
    qr_pos = (23, 15)

    qr = qrcode.convert("RGBA")
    photo.paste(qr, qr_pos)
    return photo