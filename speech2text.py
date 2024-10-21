'''
import streamlit as st
from whisper import whisper_stt

open_ai_key = "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"
text = whisper_stt(
    openai_api_key=open_ai_key, language = 'en')  # If you don't pass an API key, the function will attempt to load a .env file in the current directory and retrieve it as an environment variable : 'OPENAI_API_KEY'.
if text:
    st.write(text)

'''

import streamlit as st
from streamlit_mic_recorder import mic_recorder, speech_to_text

state = st.session_state

if 'text_received' not in state:
    state.text_received = []

c1, c2 = st.columns(2)
with c1:
    st.write("Convert speech to text:")
with c2:
    text = speech_to_text(language='cn', use_container_width=True, just_once=True, key='STT')

if text:
    state.text_received.append(text)

for text in state.text_received:
    st.text(text)

st.write("Record your voice, and play the recorded audio:")
audio = mic_recorder(start_prompt="⏺️", stop_prompt="⏹️", key='recorder')

if audio:
    st.audio(audio['bytes'])