from google import genai


client = genai.Client()


response = genai.models.generate_content(
    model="models/gemini-3-flash-preview", contents = "Explain how one can use the Google Gemini API to create a chatbot about all the info of Bangladesh.")
print(response)