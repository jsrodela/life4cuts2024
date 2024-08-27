import cups
from PIL import Image

conn = cups.Connection()

printers = conn.getPrinters()

printer_name = list(printers.keys())[0]

print(printer_name)

img = Image.open('frame2.png')
img = img.rotate(-90, expand=True)
img.save('frame2-r.png')

print_job_id = conn.printFile(printer_name, 'frame2-r.png', "", {'fit-to-paper': "True"})

print(f"Print job sent to printer '{printer_name}' with job ID: {print_job_id}")