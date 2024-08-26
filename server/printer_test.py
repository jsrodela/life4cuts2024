import cups

conn = cups.Connection()

printers = conn.getPrinters()

printer_name = list(printers.keys())[0]

print(printer_name)

print_job_id = conn.printFile(printer_name, 'frame2.png', "", {'fit-to-page': "True"})

print(f"Print job sent to printer '{printer_name}' with job ID: {print_job_id}")