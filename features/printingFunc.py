import aspose.pdf as ap
from PySide6.QtPrintSupport import QPrinter, QPrinterInfo
from PySide6.QtGui import QImage, QImageReader, QPainter, QPageLayout, QPageSize

def asposePrint (path, copies):
    viewer = ap.facades.PdfViewer()

    # 입력 PDF 파일 열기
    viewer.bind_pdf("Document.pdf");

    # 인쇄용 속성 설정
    viewer.auto_resize = True
    viewer.auto_rotate = True
    viewer.print_page_dialog = False

    # 프린터 및 페이지 설정과 PrintDocument에 대한 개체 만들기
    pgs = ap.printing.PageSettings()
    ps = ap.printing.PrinterSettings()

    # 프린터 이름 설정
    ps.printer_name = "Microsoft Print to PDF"

    ps.print_range = ap.printing.PrintRange.SOME_PAGES
    ps.from_page = 1
    ps.to_page = 2

    # 프린터 및 페이지 설정을 사용하여 문서 인쇄
    viewer.print_document_with_settings(pgs, ps)

    # PDF 파일 닫기
    viewer.close()

def pysidePrint(path, copies):
    # 기본 프린터 정보 가져오기
    default_printer = QPrinterInfo.defaultPrinter()
    if (default_printer.isNull()):
        print('연결된 프린터가 없습니다.')
        return False
    else:
        print('연결된 프린터 : ' + QPrinterInfo.defaultPrinterName())

    # 프린터 생성
    printer = QPrinter(default_printer, mode=QPrinter.HighResolution)
    # 인쇄 매수 설정
    printer.setCopyCount(copies)
    # 페이지 크기 설정 (A4)
    printer.setPageSize(QPageSize.A4)
    # 페이지 방향 설정 (가로)
    printer.setPageOrientation(QPageLayout.Orientation.Landscape)
    # DPI 설정(해상도)
    printer.setResolution(96)

    # 이미지 용량이 큰 경우 메모리 제한 해제
    QImageReader.setAllocationLimit(0)

    img = QImage(path)
    scaled_img = img.scaled(printer.pageRect(QPrinter.DevicePixel).width(),
                            printer.pageRect(QPrinter.DevicePixel).height(), aspectMode=Qt.KeepAspectRatio,
                            mode=Qt.SmoothTransformation)
    painter = QPainter()
    painter.begin(printer)
    painter.drawImage(0, 0, scaled_img)
    painter.end()

#  임시임.