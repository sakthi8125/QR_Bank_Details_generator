# 💳 QR Bank Details Generator (Password-Protected QR Sharing)

### 🏦 Project Title
**QR Bank Details Generator — generate and share password-protected QR images containing bank/UPI details**

---

## 🧾 Overview

This project collects **bank or UPI details**, generates a **QR code** image containing those details, and then places the QR image inside a **password-protected ZIP** so it can be shared securely (via WhatsApp, Email, Drive, etc.).  
It **does not** perform any money transfer. It only **encodes and protects** the recipient's bank/UPI details as a QR image for sharing.

> ⚙️ This project is a backend Python utility. It runs locally — GitHub will only host the code and docs.

---

## 🎯 Objectives

- Collect and encode bank / UPI details as a QR image.  
- Protect the QR image by storing it in a password-protected ZIP file.  
- Make the QR easy to share while ensuring only the intended recipient (who has the password) can open it.

---

## 🧩 Technologies Used

| Category | Technology / Library | Purpose |
|----------|----------------------|---------|
| Programming Language | Python 3.8+ | Core logic |
| QR Code Generation | `qrcode` | Create QR image from data |
| Image Handling | `Pillow` | Save/handle QR images |
| Packaging | `zipfile` (stdlib) | Create password-protected ZIP |
| Secure Input | `getpass` | Securely read password input |

---

## ⚙️ How It Works (Simple Flow)

1. **User enters bank/UPI details** (name, bank, account number, IFSC, UPI ID).  
2. The app **combines these fields** into a text payload.  
3. The payload is **encoded into a QR image** (`bank_qr.png`) using `qrcode`.  
4. The QR image is **zipped and password-protected** (`secure_qr.zip`).  
5. You can **share** `secure_qr.zip` and the recipient must provide the **password** to extract and scan the QR.

---

## 🗂 Project Structure

```

QR_Bank_Details_generator/
│
├── generate_qr.py       # Main script to collect details and create password-protected ZIP
├── redeem_qr.py         # (Optional) Helper to extract zip and open/preview QR image
├── requirements.txt     # Python dependencies
├── README.md
└── outputs/             # (auto) contains generated bank_qr.png and secure_qr.zip

````

---

## 💻 How to Run Locally

### Prerequisites
- Python 3.8 or later
- `pip`

### 1) Clone the repository
```bash
git clone https://github.com/sakthi8125/QR_Bank_Details_generator.git
cd QR_Bank_Details_generator
````

### 2) Install dependencies

Create `requirements.txt` (see exact contents below) and run:

```bash
pip install -r requirements.txt
```

If you prefer manual install:

```bash
pip install qrcode Pillow
```

### 3) Run the generator

```bash
python generate_qr.py
```

Follow the prompts:

* Enter Account Holder Name
* Enter Bank Name
* Enter Account Number
* Enter IFSC Code
* Enter UPI ID (optional)
* Set a password for the ZIP (input hidden)

Output files will be created in the repository root or `outputs/` folder:

* `bank_qr.png` — the generated QR image
* `secure_qr.zip` — password-protected ZIP containing the QR

### 4) Redeem / extract (Receiver)

To extract the QR (receiver):

* Use any ZIP tool that supports password entry (e.g., Windows Explorer, 7-Zip, macOS Archive Utility, or `unzip` on Linux).
* Provide the password the sender shared.
* Open the `bank_qr.png` in any QR scanner or UPI app to view/copy the details.

---

## 🔐 Security Notes & Limitations

* The ZIP password protection uses Python's `zipfile` interface; compatibility for password handling may vary across ZIP tools. For stronger cross-platform encryption consider using `pyminizip` or other encryption libraries in a future update.
* The project does **not** transmit money nor connect to any banking networks. It only encodes and packages data locally.
* Never store real bank credentials in public repositories. Use test/dummy data for demos.

---

## 🧩 File Descriptions

* `generate_qr.py` — interactive script to capture bank details, generate the QR image, and create a password-protected ZIP.
* `redeem_qr.py` — optional helper script to prompt for a password and extract the QR for preview (useful for demos).
* `requirements.txt` — lists Python libraries needed.
* `README.md` — this document.

---

## ✅ Example `requirements.txt`

```
qrcode
Pillow
```

(Optionally pin versions if you want reproducible installs, e.g. `qrcode==7.3`)

---

## 📸 Screenshots

* `screenshots/generator_prompt.png` — show terminal prompts and sample input
* `screenshots/bank_qr.png` — the generated QR image
* `screenshots/secure_qr_zip.png` — the produced ZIP file in file explorer

Add images to `/screenshots/` and reference them in the README with markdown:

```markdown
![Generator Prompt](screenshots/generator_prompt.png)
```

---

## 🧑‍💻 Author

**Sakthidevi**
Final Year – B.Sc. Computer Science with AI
Sathyabama Institute of Science and Technology

---

## 📜 License

This project is released under the **MIT License**. See [LICENSE](./LICENSE) for details.

---

## 📫 Contact / Contributions

If you want to suggest improvements or report issues:

* Use **Issues** in this repository (I added templates for Bug / Feature / General).
* Pull requests welcome — please follow the contribution template (if added).

```

---

If you want, I can:
- produce `generate_qr.py` and `redeem_qr.py` example scripts (complete, ready-to-run), or  
- create a `LICENSE` file text and `requirements.txt` file content ready for copy-paste, or  
- generate the exact `screenshots/` README section with sample image markup.

Which of those should I produce next?
```
