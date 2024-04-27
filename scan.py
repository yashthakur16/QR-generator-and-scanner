import cv2
from pyzbar import pyzbar
import csv
import os

def get_next_serial_number(csv_file):
    # Check if the CSV file exists
    if os.path.exists(csv_file):
        # Read the CSV file and find the last serial number
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            if data:
                last_entry = data[-1]
                last_serial_number = int(last_entry[0])
                return last_serial_number + 1
    # Return 1 if the CSV file doesn't exist or is empty
    return 1

def scan_qr_and_store(csv_file):
    # Get the next available serial number
    serial_number = get_next_serial_number(csv_file)
    
    # Open the CSV file in append mode
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Initialize a set to store scanned QR codes
        scanned_qr_codes = set()
        
        # Initialize font for displaying messages
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Initialize colors
        green_color = (0, 255, 0)  # Green color
        red_color = (0, 0, 255)  # Red color
        
        # Initialize camera
        cap = cv2.VideoCapture(0)
        
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            # Check if the frame is captured successfully
            if not ret:
                print("Error: Unable to capture frame.")
                break
            
            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Find QR codes in the grayscale frame
            decoded_objs = pyzbar.decode(gray)
            
            # Loop over the detected QR codes
            for obj in decoded_objs:
                # Extract the data from the QR code
                data = obj.data.decode('utf-8')
                
                # Check if the corresponding QR code image is present in the qr_codes folder
                qr_image_path = os.path.join('qr_codes', f'{data}.png')
                if os.path.isfile(qr_image_path):
                    # Check if the QR code has already been scanned
                    if data not in scanned_qr_codes:
                        # If not, add it to the set of scanned codes
                        scanned_qr_codes.add(data)
                        
                        # Write the serial number and QR code data to the CSV file
                        writer.writerow([serial_number, data])
                        
                        # Display message on the frame
                        cv2.putText(frame, f"Scanned QR code {serial_number}: {data}", (50, 50), font, 1, green_color, 2)
                        
                        # Increment the serial number
                        serial_number += 1
                    else:
                        # Display message on the frame
                        cv2.putText(frame, f"QR code '{data}' scanned.", (50, 50), font, 1, green_color, 2)
                else:
                    # Display "invalid QR code" message in red
                    cv2.putText(frame, f"Invalid QR code", (50, 50), font, 1, red_color, 2)
            
            # Display the resulting frame
            cv2.imshow('QR Code Scanner', frame)
            
            # Check for a key press to quit
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

        # Release the camera and close the CSV file
        cap.release()
        cv2.destroyAllWindows()
        file.close()

# Example usage
scan_qr_and_store('scanned_qr_codes.csv')
