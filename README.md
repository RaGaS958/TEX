![TEX LOGO](TEX.png)
# 💬 Tex – WhatsApp Auto Reply Automation

**Tex** is a **Python-based automation tool** that reads your WhatsApp messages and generates smart, context-aware auto-replies using **Google Gemini AI**.  

It combines:  
- 🖱️ **PyAutoGUI Automation**  
- 📋 **Clipboard Integration**  
- 🤖 **Google Gemini AI (Generative AI)**  
- ⌨️ **Auto Typing & Sending Replies**  

---

## 🚀 Features
- 📋 **Message Fetching** – Automatically reads WhatsApp messages from the chat window.  
- 🤖 **AI-Powered Replies** – Generates **natural and empathetic responses** using Gemini AI.  
- 🖱️ **Automation with PyAutoGUI** – Simulates clicks, keypresses, and message navigation.  
- ⌨️ **Auto Typing & Sending** – Pastes AI responses back into WhatsApp and sends them automatically.  
- ⚡ **Customizable Persona** – Replies in a friendly, conversational, and context-aware tone.   

---

## 📂 Project Structure
```
Tex/
├── 🧠 main.py # Core automation script (message fetch + Gemini AI reply + auto-send)
├── ✅ check.py #Coordinates fetcher
├── 📦 req.txt # Python dependencies
└── 📘 README.md # Project documentation
```

---
## Demo Video
Link:-https://drive.google.com/file/d/1HYA1j5WogJGJMjWRNa2KCtRtabsVbcOe/view?usp=sharing
---

## 📦 Prerequisites
- **Python 3.9+** installed on your system.  
- Required libraries (listed in `req.txt`).  

Install them with:  
```bash
pip install -r req.txt
```
---
# Setup and Configuration

## 1. Gemini AI API Key
Tex uses the Gemini AI model. To get started, you'll need to obtain an API key from **Google AI Studio**.

1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Create a new API key.
3. Replace the placeholder API key inside main.py with your own:

```python
apikey = "YOUR_API_KEY_HERE"
```
## 2. WhatsApp Window Setup
 - Open WhatsApp Desktop or WhatsApp Web on your computer.

 - Adjust the screen resolution so the script can detect coordinates correctly.

 - Make sure the chat window is open before running the script.

## How to Run
- Make sure you have completed the setup steps above.

 - Open your terminal or command prompt.

- Navigate to the directory where you saved the script.

- Run the script using the following command:
```python
python your_script_name.py
```
---
# Usage
- When you run the script, Tex will:

   1. Fetch recent messages from WhatsApp.

   2. Send the chat history to Gemini AI.

   3. Generate a short, empathetic, and context-aware reply.

   4. Paste and send the response back into the chat automatically.

### ✅ Example flow:

- Incoming message → "Hey, what are you doing?"

- Tex auto-reply → "Just chilling 😅, what about you?"

---
