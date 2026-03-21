from google import genai


client = genai.Client(api_key="YOUR_API_KEY")


response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Give me step by step instructions how can I create a chatbot using Python and the Gemini API. The chatbot will only know about Bangladesh and will be used to answer questions about Bangladesh."
)
print(response.text)
