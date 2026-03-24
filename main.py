from google import genai
from google.genai import types


client = genai.Client(api_key="")

system_instructions =  ("You are a specialized chatbot known as 'BengalBot'. "
    "Your knowledge is strictly limited to Bangladesh. " "You only reply in Banglish language."
    "You can discuss its history, culture, geography, food, politics, sports, and economy. "
    "If a user asks a question that is NOT about Bangladesh, you must politely decline "
    "and say: 'I am a specialist on Bangladesh only. Please ask me anything related to Bangladesh!'")


chat = client.chats.create(
    model="gemini-2.5-flash", # gemini-3-flash-preview might require specific tier access
    config= types.GenerateContentConfig(
        system_instruction=system_instructions
    )
)


print("Welcome to BengalBot! Ask me anything about Bangladesh.")
print("Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("BengalBot: Goodbye! Have a great day!")
        break
    response = chat.send_message(user_input)
    print(f"BengalBot: {response.text}")
