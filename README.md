# Voice Translator

## Overview
This project is a simple voice translator that recognizes speech, detects the spoken language, translates it to a target language, and converts the translated text into speech.

## Features
- 🎙️ Recognizes speech using `speech_recognition`
- 🌍 Detects the spoken language using `googletrans`
- 🔁 Translates text into a target language
- 🗣️ Converts translated text into speech using `gTTS`
- ⚡ Asynchronous execution for better performance

## Installation
### Prerequisites
Ensure you have Python installed on your system.

### Install Dependencies
Run the following command to install the required libraries:
```sh
pip install speechrecognition gtts googletrans asyncio
