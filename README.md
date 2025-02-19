# 📢 SpamBot - A Simple Python Spam Script

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Automation](https://img.shields.io/badge/Automation-PyAutoGUI-orange)

## 📌 Description
SpamBot is a simple Python script that automates text input and sending in messaging applications. It repeatedly types and sends a specified message at a user-defined interval using `PyAutoGUI`.

🚀 **Features:**
- Customizable spam message.
- Adjustable delay before execution.
- Configurable interval between messages.
- Graceful exit using `CTRL + C`.

> ⚠️ **Disclaimer:** Use this script responsibly! Spamming can violate platform policies and may result in consequences.

---

## 🔧 Installation

### 1️⃣ Install Python
Ensure you have Python **3.x** installed. Download it from [python.org](https://www.python.org/downloads/).

### 2️⃣ Install Dependencies
Open a terminal and run:
```sh
pip install pyautogui
```

---

## 🚀 Usage

1️⃣ Run the script:
```sh
python main.py
```

2️⃣ Follow the prompts:
- Enter the message you want to spam.
- Set the delay time before execution.
- Set the interval between each message.

3️⃣ Click on the message box within the given timeout.

4️⃣ The script will start sending messages automatically!

5️⃣ To stop the script, press **CTRL + C**.

---

## 🖥️ Code Overview
```python
import pyautogui
import time

text = input("Enter the text you want to spam: ")
while True:
    try:
        timeout = float(input("Enter the time (in seconds) to click the message box: "))
        break
    except ValueError:
        print("Invalid input! Enter a number.")

while True:
    try:
        interval = float(input("Enter the interval between messages (in seconds): "))
        break
    except ValueError:
        print("Invalid input! Enter a number.")

# Wait for user to click the message box
time.sleep(timeout)

try:
    while True:
        pyautogui.write(text)
        pyautogui.press('enter')
        time.sleep(interval)
except KeyboardInterrupt:
    print("Program interrupted by user.")
```

---

## ⚠️ Important Notes
- The script **requires an active messaging application** (e.g., WhatsApp, Discord, Messenger).
- Ensure you have **focus on the input box** when the script starts.
- Excessive spamming may lead to **account bans or restrictions**.

---

## 🎯 License
This project is **open-source** under the [MIT License](LICENSE).

---

## ❤️ Contributing
Want to improve this script? Feel free to **fork** this repository and submit a **pull request**!

---

## 📞 Contact
For questions or issues, reach out via GitHub Issues.

---

Happy Spamming! 🚀

