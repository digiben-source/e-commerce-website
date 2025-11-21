### **1. Clone the project**

```bash
git clone https://github.com/digiben-source/e-commerce-website.git
```

---

## **2. Create a virtual environment**

Create the `.venv` inside the project root. Run:

```bash
python3 -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

---

## **3. Install project dependencies**

run:

```bash
pip install -r requirements.txt
```

Or install packages individually if preferred.

## **4. Environment variables**

Open file named **`.env`** or create one in the project root if missing and supply your secrets:

```
SECRET_KEY=YOUR_SECRET_KEY
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## **5. Start the server**

```bash
python3 FraudShield.py
```

The server runs at:

```
http://0.0.0.0:5000
```

## **6. Deactivate virtual environment**

When done:

```bash
deactivate
```
