import cups
from PIL import Image

img = Image.open('frame4.png')
img = img.rotate(-90, expand=True)
img.save("frame4-r.png")

conn = cups.Connection()

printers = conn.getPrinters()

printer_name = list(printers.keys())[0]

print(printer_name)

print_job_id = conn.printFile(printer_name, 'frame4-r.png', "", {"fit-to-paper": "True"})

print(f"Print job sent to printer '{printer_name}' with job ID: {print_job_id}")