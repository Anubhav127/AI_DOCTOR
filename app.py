from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

input_prompt = """
    You are an expert in nutritionist where you need to see the food items from the image and calculate total calories, also provide
    the details of every food items with calories intake in below format:

    1. Item 1: - no. of calories
    2. Item 2: - no. of calories
    -----
    -----
"""

def get_gemini_response(input, image, prompt):
    model=genai.GenerativeModel("gemini-2.5-pro")
    response=model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No image uploaded")
    
def main(__name__):
    st.set_page_config(page_title="AI Nutritionist App")

    st.header("AI Nutritionist App")
    input = st.text_input("Input Prompt", key="input")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

    submit = st.button("Tell me the total Calories")

    if submit:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("Response from Gemini:")
        st.write(response)

if __name__ == "__main__":
    main(__name__)