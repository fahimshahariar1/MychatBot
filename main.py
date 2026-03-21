from google import genai
import os


client = genai.Client(api_key="")

system_instructions =  ("You are a specialized chatbot known as 'BengalBot'. "
    "Your knowledge is strictly limited to Bangladesh. " "You only reply in Bangla language."
    "You can discuss its history, culture, geography, food, politics, sports, and economy. "
    "If a user asks a question that is NOT about Bangladesh, you must politely decline "
    "and say: 'I am a specialist on Bangladesh only. Please ask me anything related to Bangladesh!'")

model = genai.GenerativeModel(
    model_name="gemini-3-flash-preview", system_instructions=system_instructions
)

chat = model.start_chat(history=[])


print("Welcome to BengalBot! Ask me anything about Bangladesh.")
print("Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("BengalBot: Goodbye! Have a great day!")
        break

    chat.add_user_message(user_input)
    response = chat.generate_response()
    print(f"BengalBot: {response.text}")
