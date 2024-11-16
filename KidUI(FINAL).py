
import streamlit as st
import pandas as pd
import numpy as np
#import promptlayer
import anthropic
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import uuid
import math
import requests
from requests.auth import HTTPBasicAuth
import json

HTML = '''
<h1 style="color:blue;">🎉Smart Buddy🎉</h1>
'''
st.markdown(HTML, unsafe_allow_html = True)


#anthropic_key = "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"
#ai_model = "claude-3-sonnet-20240229"
st.text("I am your study assistant! Ask me questions and I will try to answer!")
# student url in school account
url = 'https://sc7e7xcl71.execute-api.ap-southeast-1.amazonaws.com/test/ntc-test'
# url with RAG
# url =  'https://hqrzin7005.execute-api.ap-southeast-1.amazonaws.com/rag/ntc-student'
# original url
#url = 'https://bg68z5nea2.execute-api.ap-southeast-1.amazonaws.com/test/ntc-student'
headers = {'Accept': 'application/json'}
auth = HTTPBasicAuth('kRKNFaknPj2dhCHlHLACyPQJ3x9Rptn3Aywwzq64', '1234abcd')
data = [{"role": "user", "content": "Hi"}]
req = requests.get(url, headers=headers, auth=auth, json=data)
print(req.json())

#client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
#client = anthropic.Anthropic(api_key=anthropic_key)

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

#if "ai_model" not in st.session_state:
#    st.session_state["ai_model"] = ai_model

if "messages" not in st.session_state:
    st.session_state.messages = []

#for message in st.session_state.messages:
#    with st.chat_message(message["role"]):
#        st.markdown(message["content"])

for message in st.session_state.messages:
    if message["role"] in ["user", "assistant"]:
        with st.chat_message(message["role"]):
            #new_prompt.append(message["content"])
            st.markdown(message["content"])
            print('----: ',message["content"])

#if user_input := st.chat_input("How can I help you?"):

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        #messages.append({"role": "user", "content": prompt})
        print('>>>----: ',messages)
        req = requests.get(url, headers=headers, auth=auth, json=messages)
        print("----> req.json: ",req.json())
        #with client.messages.stream(
        #    max_tokens=1024,
        #    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        #    model=st.session_state["ai_model"],
        #) as stream:
        #    for text in stream.text_stream:
        #        full_response += str(text) if text is not None else ""
        #        message_placeholder.markdown(full_response + "▌")
        response = req.json()
        print("response: ",response)
        if 'answer' not in response.keys():
            full_response += "Sorry! I cannot answer the question."
        else:
            if len(response['answer']) == 0:
                full_response += "Sorry! I cannot answer the question."
            else:
                full_response += response['answer'][0]
        message_placeholder.markdown(full_response+ "▌")
    st.session_state.messages.append({"role": "assistant", "content": full_response})
