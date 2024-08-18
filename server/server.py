import time, os, pathlib
from watchdog.observers import Observer # 파일 생성 감시 모듈
from watchdog.events import FileSystemEventHandler
import print # 프린트 모듈
import upload # QR코드 및 업로드 모듈
import combine # 사진 & 프레임 합성 함수

MAIN_DIR = './'

class FileCreationHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the created event is a file, not directory
        if not event.is_directory:
            print(f"File created: {event.src_path}")
            file_name = pathlib.Path(event.src_path).name
            if file_name[-5] == '4': # 4번째 사진 파일이면 업로드&인쇄 실행
                uid = file_name[] # uid 자릿수 결정 필요
                number = file_name[0]
                code = upload.pre_code()
                upload.gen_qrcode(code, uid)
                combine.combine_photo(uid)
                print.print_printer(number)
                upload.post_file(code)

if __name__ == "__main__": # if this python file is excuted
    path = MAIN_DIR # Directory to monitor 
    event_handler = FileCreationHandler()
    observer = Observer()
    
    # Schedule the observer to monitor the specified path
    observer.schedule(event_handler, path, recursive=False)
    
    # Start the observer
    observer.start()
    print(f"Monitoring file creation in: {path}")
    
    try:
        while True:
            time.sleep(5)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


