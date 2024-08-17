import time
import print # 프린트 모듈
import upload # QR코드 및 업로드 모듈
import combine # 사진 & 프레임 합성 함수

while(True):
    """ 
    5초마다 새로운 파일이 있는지 확인 - 작성필요
    newfile = 새로운 파일이 발견될 시 활성화(트리거)
    uid = 파일 uid, number = 인원수 
    """
    if newfile:
        code = upload.pre_code()
        upload.gen_qrcode(code, uid)
        combine.combine_photo(uid)
        print.print_printer(number)
        upload.post_file(code)
    else: 
        time.sleep(5)

