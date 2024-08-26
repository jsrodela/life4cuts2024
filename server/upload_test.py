import upload

code = upload.pre_code()
qrcode = upload.gen_qrcode(code)

print(f'공유코드: {code}')

upload.post_file(code, 'frame1.png')