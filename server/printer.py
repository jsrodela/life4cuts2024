import cups

def print_printer(final_image, number):

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

        for i in range(number):

            # Print the image to the default printer
            print_job_id = conn.printFile(printer_name, final_image, "", {})
            
            print(f"Print job sent to printer '{printer_name}' with job ID: {print_job_id}")

    return True

