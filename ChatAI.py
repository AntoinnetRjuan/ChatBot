import customtkinter as ctk

def chatbot_response(user_input):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you?": "I'm just a computer program, but I'm here to help you!",
        "bye": "Goodbye! Have a great day!",
        "what's your name?": "I'm ChatAI, your virtual assistant.",
    }
    return responses.get(user_input.lower(), "I'm not sure how to respond to that. Can you ask something else?")

def send_message(event=None):
    user_message = user_input.get()
    if user_message.strip() != "":
        chat_history.configure(state="normal")
        chat_history.insert("end", f"You: {user_message}\n", "user")
        bot_response = chatbot_response(user_message)
        chat_history.insert("end", f"ChatAI: {bot_response}\n", "bot")
        chat_history.configure(state="disabled")
        chat_history.see("end")
        user_input.delete(0, "end")

app = ctk.CTk()
app.geometry("400x500")
app.title("ChatAI - Chatbot")

header = ctk.CTkLabel(app, text="Welcome to Antoinnet's ChatAI", font=("Arial", 18, "bold"))
header.pack(pady=20)

chat_history = ctk.CTkTextbox(app, width=700, height=300, state="disabled")
chat_history.tag_config("user", foreground="white")   
chat_history.tag_config("bot", foreground="green") 
chat_history.pack(pady=10, padx=10 , fill="both", expand=True)  

user_input_frame = ctk.CTkFrame(app)
user_input_frame.pack(pady=10, padx=10, fill="x")   

user_input = ctk.CTkEntry(user_input_frame, placeholder_text="Type your message here...", width=300)
user_input.pack(side="left", fill="x", padx=5)

send_button = ctk.CTkButton(user_input_frame, text="Send", command=send_message)
send_button.pack(side="right")

app.bind("<Return>", send_message)
app.mainloop()