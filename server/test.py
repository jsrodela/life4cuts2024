# QR코드 위치 테스트용 코드

from PIL import Image
import qrcode

frame = Image.open('frame4.png')
bg = Image.new('RGBA',(frame.size[0], frame.size[1]),'white')
bg.paste(frame)
qrc = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_M,
        box_size=4,
        border=1
    )
qrc.add_data('jamsin-file.kro.kr')
qr = qrc.make_image(back_color=(255, 255, 255), fill_color=(0, 0, 0))
qr = qr.resize((325, 325))
bg.paste(qr, (1985, 130))
bg.show()