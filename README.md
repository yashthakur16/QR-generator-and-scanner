


# QR Code Generator and Scanner

This project provides an efficient solution for generating and scanning QR codes using Python. It leverages Python's powerful libraries to handle tasks such as reading from Excel files, generating QR codes, and scanning them to store data in a CSV file.

## Features

1. **Generate QR Codes from Excel File**:
   - Reads data from an Excel file.
   - Generates QR codes for each entry in a specified column.
   - Saves the QR codes as PNG images in a designated folder.

2. **Scan QR Codes and Store Data**:
   - Utilizes the camera to scan QR codes.
   - Stores the scanned data in a CSV file.
   - Ensures no duplicate scans and provides feedback for invalid QR codes.

## Technologies Used

- **Python**: The core programming language used for its simplicity and readability.
- **pandas**: To handle Excel file operations seamlessly.
- **pyqrcode**: For generating high-quality QR codes.
- **opencv-python**: For accessing and handling video streams from the camera.
- **pyzbar**: For decoding QR codes from video frames.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `pandas`
  - `pyqrcode`
  - `pypng`
  - `opencv-python`
  - `pyzbar`

Install the required packages using pip:

```sh
pip install pandas pyqrcode pypng opencv-python pyzbar
```

## Usage

### Generating QR Codes

1. Ensure you have an Excel file (e.g., `BE2.xlsx`) with the data for the QR codes.
2. Run the script to generate QR codes from a specified column in the Excel file.
3. The generated QR codes will be saved as PNG images in the `qr_codes(BE)` directory.

### Scanning QR Codes

1. Ensure you have a CSV file to store the scanned QR code data (e.g., `scanned_qr_codes.csv`).
2. Use the script to activate the camera and start scanning QR codes.
3. The scanned data will be stored in the CSV file, and the system will handle duplicate scans and invalid QR codes appropriately.

## Contributing

We welcome contributions! Feel free to submit issues or pull requests if you have suggestions or improvements.

