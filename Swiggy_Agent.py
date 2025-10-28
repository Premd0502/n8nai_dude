from flask import Flask, jsonify
import time
import webbrowser
import pyautogui

app = Flask(__name__)


@app.route('/swiggy', methods=['POST'])
def swiggy_automation():
    try:
        # Open Swiggy search page and perform actions
        webbrowser.open("https://www.swiggy.com/search")
        time.sleep(3)
        pyautogui.click(451, 413)
        time.sleep(1)
        pyautogui.typewrite("Nandhana palace briyani", interval=0.1)
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.click(622, 696)
        time.sleep(1)
        pyautogui.press('tab', presses=20, interval=0.5)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(1145, 857)
        time.sleep(4)
        # Optionally uncomment to scroll if needed
        # pyautogui.scroll(2000)

        webbrowser.open("https://www.swiggy.com/checkout")
        time.sleep(5)
        pyautogui.click(867, 586)
        time.sleep(2)
        pyautogui.click(1790, 623)
        pyautogui.scroll(-300)
        time.sleep(0.5)
        pyautogui.click(1565, 553)
        time.sleep(2)
        pyautogui.click(1450, 819)
        time.sleep(2)
        pyautogui.click(945, 780)
        time.sleep(2)
        pyautogui.click(675, 871)
        time.sleep(2)
        pyautogui.click(684, 767)
        time.sleep(1)
        pyautogui.press('tab', presses=2, interval=0.5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.typewrite("", interval=0.1)
        pyautogui.press('enter')

        return jsonify({'status': 'Automation executed successfully'}), 200
    except Exception as e:
        return jsonify({'status': 'Error occurred', 'error': str(e)}), 500


if __name__ == '__main__':
    # The app will run on port 5001
    app.run(port=5001)