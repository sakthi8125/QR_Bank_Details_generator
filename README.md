
# 💳 Password-Protected UPI Scratch Card Money Transfer System

### 🏦 Project Title
**Password-Protected UPI Scratch Card Money Transfer System**

---

## 🧾 Overview

This project introduces a **secure, digital money transfer mechanism** inspired by **UPI scratch cards**.  
It allows users to generate **password-protected QR codes** that contain bank or UPI details, making digital transactions **safe, private, and easily shareable** through email, WhatsApp, or other platforms.

The QR code is encrypted inside a ZIP file that can be accessed only with a password — ensuring secure redemption by authorized users.

---

## 🎯 Objectives

- Provide a **password-protected** method for UPI-based transactions.  
- Enable **secure sharing** of QR-based digital scratch cards.  
- Protect user bank information using encryption.  
- Allow redemption of QR through secure password validation.  
- Ensure compatibility across **mobile and desktop devices**.

---

## ⚙️ Features

✅ Generate UPI/Bank QR code  
✅ Create password-protected ZIP files  
✅ Secure password handling with `getpass`  
✅ Redeem QR only with valid password  
✅ Shareable via WhatsApp, Email, or Cloud  
✅ Platform-independent (works on any OS)

---

## 🧠 System Workflow

```

    ┌───────────────────────────────┐
    │    User enters bank details   │
    └──────────────┬────────────────┘
                   │
                   ▼
        ┌────────────────────┐
        │ Generate QR code   │
        └─────────┬──────────┘
                  │
                  ▼
      ┌──────────────────────────┐
      │ Create ZIP (with password)│
      └───────────┬──────────────┘
                  │
                  ▼
    ┌────────────────────────────┐
    │ Share QR ZIP file securely │
    └──────────┬─────────────────┘
               │
               ▼
     ┌────────────────────────────┐
     │  Redeem using password     │
     │  and scan QR code          │
     └────────────────────────────┘
```

````

## 🧩 Technologies Used

| Category | Technology / Library | Purpose |
|-----------|----------------------|----------|
| **Programming Language** | Python 3.8+ | Core development |
| **QR Code Generation** | `qrcode` | Create QR image for bank/UPI details |
| **Image Processing** | `Pillow (PIL)` | Handle and save QR images |
| **File Encryption** | `zipfile` | Create password-protected ZIP files |
| **Secure Input** | `getpass` | Hide password while typing |
| **File Management** | `os`, `shutil` | Manage local files and directories |

---

## 💻 Code Example

```python
import qrcode
import zipfile
import getpass

# Step 1: Get user details
name = input("Enter Account Holder Name: ")
bank = input("Enter Bank Name: ")
acc_no = input("Enter Account Number: ")
ifsc = input("Enter IFSC Code: ")
upi_id = input("Enter UPI ID: ")

# Step 2: Create QR data
data = f"Name: {name}\nBank: {bank}\nAccount: {acc_no}\nIFSC: {ifsc}\nUPI: {upi_id}"

# Step 3: Generate QR
qr = qrcode.make(data)
qr_filename = "bank_qr.png"
qr.save(qr_filename)

# Step 4: Create password-protected ZIP
zip_filename = "secure_qr.zip"
password = getpass.getpass("Set Password for ZIP: ")

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.setpassword(password.encode())
    zf.write(qr_filename)

print("✅ QR code generated and secured successfully!")
````

---

## 🔐 Security Concept

* The QR file is encrypted using a **password-based ZIP compression**.
* Prevents unauthorized users from viewing or redeeming the QR.
* The password is handled securely using the `getpass` module (not visible on screen).
* Files can be shared through any medium — Email, WhatsApp, or Cloud Storage.

---

## 🧰 Future Enhancements

🚀 Add login system with database (SQLite or Firebase)
🚀 Integrate OTP or expiry time for QR redemption
🚀 Build GUI using **Tkinter** or **Flask**
🚀 Enable direct mobile camera scanning
🚀 Connect with mock UPI API for live transactions

---

## 📂 Project Structure

```
Bank-QR-Generator/
│
├── generate_qr.py
├── encrypt_zip.py
├── redeem_qr.py
├── requirements.txt
├── README.md
└── outputs/
    ├── bank_qr.png
    └── secure_qr.zip
```

---

## 📸 Screenshots

> Add these screenshots after running your project:

* **QR Generation Screen**
* **Password Entry**
* **ZIP File Output**
* **QR Redeem Process**

---

## 🧑‍💻 Author

**Developed by:**
🎓 *Sakthidevi*
Final Year – B.Sc. Computer Science with AI
Sathyabama Institute of Science and Technology

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it for educational or research purposes.

---

## 🌐 Tags

`#python` `#fintech` `#qr-code` `#banking` `#encryption` `#upi` `#security` `#studentproject`

```

---

Would you like me to also create the **`requirements.txt`** (to include dependencies like `qrcode` and `pillow`) so your GitHub project runs smoothly when others clone it?
```
