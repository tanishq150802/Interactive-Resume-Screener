import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))


# Streamlit UI elements
st.title("Resume Screener - Interactive CV shortlisting tool")

uploaded_file = st.file_uploader("Upload the Job Description", type=["pdf"])

question = st.text_input(
    "Search for something",
    placeholder="What data are looking for?"
)


if question and uploaded_file:
    st.write("Uploaded file:", uploaded_file.name)

    with open("C:\\Users\\tanus\\Dropbox\\", "wb") as f:
        f.write(uploaded_file.read())  # Use read() instead of getbuffer()

    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
