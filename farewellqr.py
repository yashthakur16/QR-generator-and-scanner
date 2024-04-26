import os
import pandas as pd
import pyqrcode

def generate_qr_from_excel(excel_file, column_name):
    # Read the Excel file
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        print("Excel file not found.")
        return
    except Exception as e:
        print("Error:", e)
        return
    
    # Check if the specified column exists
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the Excel file.")
        return
    
    # Create the directory to save QR codes if it doesn't exist
    qr_codes_dir = 'qr_codes(BE)'
    if not os.path.exists(qr_codes_dir):
        os.makedirs(qr_codes_dir)
    
    # Generate QR codes for each entry in the specified column
    for index, row in df.iterrows():
        name = str(row[column_name])
        qr = pyqrcode.create(name)
        qr.png(os.path.join(qr_codes_dir, f'{name}.png'), scale=8)
        print(f"QR code generated for '{name}'")

# Example usage
generate_qr_from_excel('BE2.xlsx', 'Name')
