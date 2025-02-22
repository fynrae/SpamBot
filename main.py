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
