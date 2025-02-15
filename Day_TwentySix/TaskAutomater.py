import os
import shutil
import webbrowser
import schedule
import time
import pyttsx3
import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
import threading
import datetime
import requests
import psutil
import subprocess
import pyautogui
import random


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for commands...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand.")
        return ""


def open_apps():
    speak("Opening apps and websites")
    os.system("code")  # Open VS Code
    webbrowser.open("https://github.com/")
    webbrowser.open("https://www.youtube.com/")


def organize_files():
    speak("Organizing files")
    downloads = os.path.expanduser("~/Downloads")
    documents = os.path.expanduser("~/Documents")
    pictures = os.path.expanduser("~/Pictures")

    for file in os.listdir(downloads):
        if file.endswith(".pdf"):
            shutil.move(os.path.join(downloads, file), documents)
        elif file.endswith((".jpg", ".png")):
            shutil.move(os.path.join(downloads, file), pictures)


def clean_temp():
    speak("Cleaning temporary files")
    temp_folder = os.path.expanduser("~/AppData/Local/Temp")
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
        os.makedirs(temp_folder)


def fetch_news():
    speak("Fetching the latest news")
    webbrowser.open("https://news.google.com/")


def send_reminder():
    messagebox.showinfo("Reminder", "Stay focused and keep coding! 🚀")
    speak("Reminder: Stay focused and keep coding")


def check_system_status():
    battery = psutil.sensors_battery()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    status = f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory_info.percent}%\nBattery: {battery.percent if battery else 'Unknown'}%"
    messagebox.showinfo("System Status", status)
    speak(status)


def get_weather():
    city = "New York"  # Change to your city
    api_key = "your_api_key"  # Replace with a valid OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        weather = f"Temperature: {response['main']['temp']}°C\nWeather: {response['weather'][0]['description']}"
        messagebox.showinfo("Weather Update", weather)
        speak(weather)
    else:
        speak("Could not retrieve weather information.")


def take_screenshot():
    speak("Taking a screenshot")
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot saved successfully")


def tell_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they can't C#.",
        "How do you comfort a JavaScript bug? You console it."
    ]
    joke = random.choice(jokes)
    speak(joke)


def shutdown():
    speak("Are you sure you want to shut down the system? Say yes to confirm or no to cancel.")
    confirmation = listen()
    if "yes" in confirmation:
        speak("Shutting down the system.")
        # For Windows. Use "sudo shutdown -h now" for Linux/macOS
        os.system("shutdown /s /t 5")
    else:
        speak("Shutdown canceled.")


def start_voice_control():
    while True:
        command = listen()
        if "open apps" in command:
            open_apps()
        elif "organize files" in command:
            organize_files()
        elif "clean temp" in command:
            clean_temp()
        elif "fetch news" in command:
            fetch_news()
        elif "system status" in command:
            check_system_status()
        elif "weather update" in command:
            get_weather()
        elif "take screenshot" in command:
            take_screenshot()
        elif "tell me a joke" in command:
            tell_joke()
        elif "shutdown" in command:
            shutdown()
        elif "exit" in command:
            speak("Exiting voice control")
            break


def schedule_tasks():
    schedule.every().day.at("09:00").do(open_apps)
    schedule.every().day.at("10:00").do(organize_files)
    schedule.every().day.at("11:00").do(clean_temp)
    schedule.every().hour.do(send_reminder)
    schedule.every().day.at("08:00").do(get_weather)
    schedule.every().day.at("07:30").do(check_system_status)

    while True:
        schedule.run_pending()
        time.sleep(1)


def run_scheduler():
    thread = threading.Thread(target=schedule_tasks)
    thread.daemon = True
    thread.start()


def run_voice_control():
    thread = threading.Thread(target=start_voice_control)
    thread.daemon = True
    thread.start()


def create_gui():
    root = tk.Tk()
    root.title("Smart Task Automator")
    root.geometry("400x400")

    tk.Label(root, text="Automate your tasks!",
             font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Start Voice Control",
              command=run_voice_control).pack(pady=5)
    tk.Button(root, text="Run Scheduled Tasks",
              command=run_scheduler).pack(pady=5)
    tk.Button(root, text="Fetch News", command=fetch_news).pack(pady=5)
    tk.Button(root, text="Check System Status",
              command=check_system_status).pack(pady=5)
    tk.Button(root, text="Get Weather Update",
              command=get_weather).pack(pady=5)
    tk.Button(root, text="Take Screenshot",
              command=take_screenshot).pack(pady=5)
    tk.Button(root, text="Tell Me a Joke", command=tell_joke).pack(pady=5)
    tk.Button(root, text="Shutdown System", command=shutdown).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
