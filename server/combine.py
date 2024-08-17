from PIL.Image import Image

# 숫자 수정 필요!!!

def combine_photo(number ,uid):

    w = 523
    h = 400

    pos = {(74, 64), (614, 64), (1154, 64), (74, 480)}
    qr_pos = (23, 15)

    background = Image.open('frame1.png').convert("RGBA")
    for i in range(4):
        photo = Image.open(f'{number}-{uid}-{i}.png').convert("RGBA")

        photo = photo.resize((h*16//9, h))

        w_off = photo[i].width - w

        photo = photo.crop((w_off//2, 0, photo[i].width - w_off//2, h))

        background.paste(photo, pos[i])

    qr = Image.open(f'qrcode-{uid}.png').convert("RGBA")
    background.paste(qr, qr_pos)

    background.save(f'final-{uid}.png')