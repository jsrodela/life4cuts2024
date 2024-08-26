import cups

conn = cups.Connection()

printers = conn.getPrinters()

printer_name = list(printers.keys())[0]

print(printer_name)

print_job_id = conn.printFile(printer_name, 'frame1.png', "", {})