# Smart Task Automator

## Overview
Smart Task Automator is an advanced Python-based automation tool designed to improve productivity and efficiency. It integrates multiple functionalities such as voice control, task scheduling, file organization, system monitoring, and more within a modern, user-friendly GUI.

## Features
- **Voice Control**: Execute commands using voice recognition.
- **File Organizer**: Automatically organize downloaded files.
- **Weather Updates**: Get real-time weather information.
- **News Fetching**: Open Google News for the latest headlines.
- **System Monitoring**: Check CPU, RAM, and battery status.
- **Task Scheduling**: Automate repetitive tasks at scheduled times.
- **Screenshot Capture**: Take screenshots with a single click.
- **Wikipedia Search**: Quickly find information on Wikipedia.
- **Math Solver**: Solve mathematical problems using Wolfram Alpha API.
- **YouTube & Google Search**: Open YouTube and perform Google searches directly.
- **Camera Access**: Open and control the webcam.
- **Email Sending**: Send automated emails.
- **Shutdown & Exit**: Remotely shut down the system.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Required dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### Required Python Libraries
```sh
pip install pyttsx3 speechrecognition schedule requests psutil pyautogui wolframalpha opencv-python smtplib
```

## Usage
Run the script using:
```sh
python Smart_Task_Automater.py
```

## Configuration
- **Weather API**: Replace `your_api_key` in the `get_weather()` function with a valid OpenWeather API key.
- **Wolfram Alpha API**: Replace `your_wolframalpha_api_key` with a valid Wolfram Alpha API key.
- **Email Configuration**: Update `send_email()` with valid sender email credentials.

## GUI Overview
- Click buttons to execute tasks manually.
- Use voice commands to interact with the assistant.
- Automated scheduling of repetitive tasks.

## Voice Commands Examples
- "Open apps"
- "Organize files"
- "Check system status"
- "Take screenshot"
- "Tell me a joke"
- "Shutdown system"

## Future Enhancements
- AI-powered personal assistant with NLP.
- Integration with smart home devices.
- Advanced task automation using AI.

## License
MIT License

## Contributors
Developed by Burhanali2211
