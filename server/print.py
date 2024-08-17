import cups

# Define the path to your image
image_path = "final.png"

# Connect to the CUPS server
conn = cups.Connection()

# Get the list of available printers
printers = conn.getPrinters()

# Check if there are any printers available
if not printers:
    print("No printers found.")
else:
    # Get the default printer
    printer_name = list(printers.keys())[0]  # Choose default printer

    # Print the image to the default printer
    print_job_id = conn.printFile(printer_name, image_path, "", {})
    
    print(f"Print job sent to printer '{printer_name}' with job ID: {print_job_id}")
