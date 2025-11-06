#!/usr/bin/env python3
"""
🔐 Password-Protected Bank QR Generator
Author: DeepSeek AI Assistant
Description: Generates QR codes with bank details and optional password protection
"""

import qrcode
from PIL import Image
import zipfile
import os
import datetime
import getpass
import time

def validate_account_number(acc_number):
    """Validate account number contains only digits"""
    return acc_number.isdigit()

def validate_ifsc(ifsc_code):
    """Basic IFSC code validation"""
    ifsc_code = ifsc_code.upper().strip()
    if len(ifsc_code) != 11:
        return False
    if not ifsc_code[:4].isalpha():
        return False
    if not ifsc_code[4:].isalnum():
        return False
    return True

def get_user_input():
    """Collect and validate user input for bank details"""
    print("\n" + "="*50)
    print("🔐 PASSWORD-PROTECTED BANK QR GENERATOR")
    print("="*50)
    
    # Account Holder Name
    while True:
        account_holder = input("\n👤 Enter Account Holder Name: ").strip()
        if account_holder:
            break
        print("❌ Account holder name cannot be empty!")
    
    # Bank Name
    while True:
        bank_name = input("🏦 Enter Bank Name: ").strip()
        if bank_name:
            break
        print("❌ Bank name cannot be empty!")
    
    # Account Number
    while True:
        account_number = input("🔢 Enter Account Number: ").strip()
        if validate_account_number(account_number):
            break
        print("❌ Account number must contain only digits!")
    
    # IFSC Code
    while True:
        ifsc_code = input("🏷️  Enter IFSC Code: ").strip()
        if validate_ifsc(ifsc_code):
            ifsc_code = ifsc_code.upper()
            break
        print("❌ Invalid IFSC code format! (Should be 11 characters: 4 letters + 7 alphanumeric)")
    
    # Account Type
    print("\n📊 Select Account Type:")
    print("1. Savings")
    print("2. Current")
    print("3. Other")
    
    account_type_choice = input("Enter choice (1/2/3): ").strip()
    account_types = {"1": "Savings", "2": "Current", "3": "Other"}
    account_type = account_types.get(account_type_choice, "Savings")
    
    return {
        'account_holder': account_holder,
        'bank_name': bank_name,
        'account_number': account_number,
        'ifsc_code': ifsc_code,
        'account_type': account_type
    }

def get_password():
    """Securely get and confirm password from user"""
    while True:
        print("\n🔒 Enter password for ZIP protection: ", end="")
        password = input()  # Use regular input instead of getpass
        if not password:
            print("❌ Password cannot be empty!")
            continue
            
        print("🔒 Confirm password: ", end="")
        confirm_password = input()  # Use regular input instead of getpass
        
        if password == confirm_password:
            print("✅ Passwords match!")
            return password
        else:
            print("❌ Passwords do not match! Please try again.")
            
def format_bank_data(bank_details):
    """Format bank details into a readable string"""
    return f"""Account Holder: {bank_details['account_holder']}
Bank: {bank_details['bank_name']}
Account Number: {bank_details['account_number']}
IFSC: {bank_details['ifsc_code']}
Type: {bank_details['account_type']}

Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🔐 Secure QR Code - Keep this information safe!"""

def generate_qr_code(data, filename):
    """Generate QR code from data and save to file"""
    try:
        # Create QR code instance with high quality settings
        qr = qrcode.QRCode(
            version=10,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=10,  # Size of each box in pixels
            border=4,  # Border size in boxes
        )
        
        # Add data to QR code
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        qr_image.save(filename)
        
        print(f"✅ QR code generated successfully: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error generating QR code: {e}")
        return False

def create_password_protected_zip(zip_filename, file_to_zip, password):
    """Create a password-protected ZIP file"""
    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Set password for the ZIP file
            zipf.setpassword(password.encode('utf-8'))
            zipf.write(file_to_zip, os.path.basename(file_to_zip))
        
        print(f"🔒 Password-protected ZIP created: {zip_filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating ZIP file: {e}")
        return False

def main():
    """Main function to orchestrate the QR generation process"""
    try:
        # Get bank details from user
        bank_details = get_user_input()
        
        # Ask about password protection
        protect_choice = input("\n🔒 Do you want to password-protect the QR file? (y/N): ").strip().lower()
        use_password = protect_choice in ['y', 'yes']
        
        password = None
        if use_password:
            password = get_password()
        
        # Generate timestamp for unique filenames
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"bank_qr_{timestamp}"
        png_filename = f"{base_filename}.png"
        zip_filename = f"{base_filename}.zip"
        
        # Format data and generate QR code
        formatted_data = format_bank_data(bank_details)
        print(f"\n📊 Formatted data:\n{formatted_data}")
        
        # Generate QR code
        print("\n🔄 Generating QR code...")
        if not generate_qr_code(formatted_data, png_filename):
            return
        
        # Handle password protection if requested
        if use_password and password:
            print("\n🔒 Creating password-protected ZIP...")
            if create_password_protected_zip(zip_filename, png_filename, password):
                # Remove the original PNG file for security
                os.remove(png_filename)
                print(f"🗑️  Original PNG file removed for security: {png_filename}")
                final_file = zip_filename
            else:
                final_file = png_filename
        else:
            final_file = png_filename
        
        # Success message
        print("\n" + "="*50)
        print("🎉 GENERATION COMPLETE!")
        print("="*50)
        print(f"📁 Final file: {final_file}")
        
        if use_password:
            print("🔒 File is password-protected")
            print("⚠️  IMPORTANT: Remember your password - recovery is impossible!")
        else:
            print("🔓 File is not password-protected")
        
        print("\n💡 Security Tips:")
        print("• Store the file in a secure location")
        print("• Share passwords through secure channels")
        print("• Regularly update your security practices")
        print("• Consider encrypting the file before sharing")
        
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user.")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()