
from google.cloud import texttospeech
import streamlit as st

client = texttospeech.TextToSpeechClient()

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Studio-M",
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    speaking_rate=1
)

st.set_page_config(page_title="Text2Speech")
st.header("Text to Speech Generator")
input_text = st.text_area("Enter the text to create speech")

## Input
input_text = texttospeech.SynthesisInput(text= input_text)

if st.button("Generate Speech") and input_text:
    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )
    st.audio(response.audio_content)
    
