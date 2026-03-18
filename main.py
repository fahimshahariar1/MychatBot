from google import genai
genai.config.api_key = ""


response = genai.models.generate_content(
    model="models/gemini-3-flash-preview", contents = "Explain how one can use the Google Gemini API to create a chatbot about all the info of Bangladesh.")
print(response)
