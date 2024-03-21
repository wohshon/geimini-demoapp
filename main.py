import streamlit as st

from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import Part


# Create a title and header for the app
st.title("My Streamlit App")
st.header("Streamlit app to test Gemini model")

option = st.selectbox(
   "Choose a model",
   ("gemini-1.0-pro", "gemini-1.0-pro-vision"),
   index=None,
   placeholder="Select model...",
)

if option:
   # Load Gemini Pro
   # gemini_pro_model = GenerativeModel("gemini-1.0-pro")
   # Load Gemini Pro
   gemini_pro_model = GenerativeModel(option)

   if option == 'gemini-1.0-pro-vision': 
      uploaded_file = st.file_uploader("Choose a file")
   
      if uploaded_file is not None:
         # To read file as bytes:
         bytes_data = uploaded_file.getvalue()
         # st.write(bytes_data)
         st.image(bytes_data)
         img = Part.from_data(bytes_data, mime_type="image/jpeg") 
      # Create a text input field
      text = st.text_input("Enter some text")   
      # Create a button
      if st.button("Submit"):
         model_response = gemini_pro_model.generate_content([text,img ])
         print("model_response\n",model_response)
         # Display the text that was returned
         st.write(f" {model_response.candidates[0].content.parts[0].text}")
   else:
      text = st.text_input("Enter some text")   
      # Create a button
      if st.button("Submit"):
         model_response = gemini_pro_model.generate_content(text)
         print("model_response\n",model_response)
         # Display the text that was returned
         st.write(f" {model_response.candidates[0].content.parts[0].text}")