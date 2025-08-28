import google.generativeai as genai
import time
import pyautogui
import pyperclip
api=""
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.5-flash')
def main():
    num_msg=int(input("Enter the Number of messages to be fetch="))
    print("---"*10)
    print("Starting in 5 seconds... Switch to WhatsApp window.")
    print("---"*10)
    time.sleep(5)

    pyautogui.rightClick(550, 1002)
    time.sleep(0.5)

    pyautogui.click(635, 892,clicks=2,interval=0.2)
    time.sleep(0.5)

    pyautogui.click(635, 967,interval=0.2)
    time.sleep(0.1)
    for i in range(0,num_msg-1):
     pyautogui.press("up", presses=1, interval=0.2)
     pyautogui.press("enter")
     time.sleep(0.5)

    pyautogui.click(1653, 85)
    time.sleep(1)

    text = pyperclip.paste()
    print("RECENT CHAT:-")
    print(text)
    print("---"*10)
    print("Genearting Response ......")
    print("---"*10)

    try:
       
       response = model.generate_content(f"""
You are an exceptionally smart, empathetic, and relatable chat partner. Your persona is a helpful, emotionally intelligent friend.

You will receive a chat history and must generate ONE natural, engaging, and highly context-aware reply.

Here are your core instructions:

1.  **Embody the Persona:** Read the history and adopt the exact language and tone (formal, informal, Hindi/English, mixed, etc.) of the conversation. Match the communication style precisely.
2.  **Be Conversational:** Do not sound like a bot. Use natural, brief conversational fillers where appropriate ("hmm," "oh," "haha," "arre," "lol"). Use emojis only if they are a natural part of the established chat style.
3.  **Demonstrate Empathy:** Identify the other person's emotional state (e.g., happy, sad, frustrated, excited) and explicitly reflect it in your reply. Show genuine interest and validation.
4.  **Be Concise & Relevant:** Your reply must be **one to two sentences at most**. Stick strictly to the topic at hand.
5.  **Be Helpful, Not Vague:** If a direct question is asked, provide a helpful and specific answer instead of a generic one. If you cannot answer, say so gracefully.

Chat history:
{text}
""")
       
       print("Response:-")
       print(response.text)
       print("---"*10)
       pyperclip.copy(response.text)
    except Exception as e:
       print("ERROR with gemini",e)   
    pyautogui.click(892, 1049)
    time.sleep(1)  
    pyautogui.hotkey('ctrl' ,'v')
    time.sleep(1)  
    pyautogui.click(1896, 1047)
    time.sleep(1) 
    print("Response sended to the person")
    print("---"*10)

if __name__ == "__main__":
    main()
