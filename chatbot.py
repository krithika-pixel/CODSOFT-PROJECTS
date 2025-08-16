import nltk
import streamlit as st
import re 
from nltk.chat.util import Chat, reflections

nltk.download('punkt')


pairs=[
    (r'hi/hello/hey',['Hey mate!,How may I help you?']),
    (r'What is your name?',['I am Lucy, your virtual assistant.']),
    (r'What can you do?',['I can help you with various tasks like answering questions, providing information, and assisting with scheduling.']),
    (r'How are you?',['I am just a chatbot, but I appreciate your concern!']),
    (r'What is the weather like today?',['I am not connected to a weather service, but you can check your local weather app for updates.']),
    (r'Can you help me with my homework?',['Sure! What subject do you need help with?']),
    (r'Can you help me with Engineering Mathematics-3?',['Of course! What specific topic inEngineering Mathematics-3 do you need help with?']),
    (r'I need help to understand Fourier Series',['Fourier Series is a way to represent a function as a sum of sine and cosine functions. It is used in signal processing and other fields. Do you have a specific question about it?']),
    (r'I need help to understand Laplace Transform',['Laplace Transform is a technique used to transform a function of time into a function of a complex variable. It is widely used in engineering and physics to analyze linear time-invariant systems. Do you have a specific question about it?']),
    (r'I need help to understand Z Transform',['Z Transform is a mathematical tool used in digital signal processing and control theory. It converts discrete-time signals into a complex frequency domain representation. If you have a specific question about it, feel free to ask!']),
    (r'Okay, can u tell applications of Fourier Series?',['Sure! Fourier Series has applications in signal processing, image compression, audio analysis, and solving partial differential equations. It is widely used in engineering and physics to analyze periodic functions.']),
    (r'Okay, can u tell applications of Laplace Transform?',['Certainly! Laplace Transform is used in control systems, circuit analysis, signal processing, and solving ordinary differential equations. It helps in analyzing linear time-invariant systems and is essential in engineering fields.']),
    (r'Okay, can u tell applications of Z Transform?',['Absolutely! Z Transform is used in digital signal processing, control systems, and discrete-time system analysis. It helps in analyzing and designing digital filters, control systems, and is essential in the field of digital communications.']),
    (r'I did not know you understand this much about Engineering Mathematics-3',['Yes, I have been programmed with a wide range of knowledge, including Engineering Mathematics-3. If you have any more questions or need further assistance, feel free to ask!']),
    (r'That is great!',['I am glad you think so! If you have any more questions or need help with anything else, just let me know.']),
    (r'No thanks, I am all held up today',['No problem! If you need assistance in the future, feel free to reach out. Have a great day!']),
    (r'bye/exit/quit',['Goodbye! Have a great day!']),

]

chatbot = Chat(pairs, reflections)

st.title("Lucy - Your Virtual Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if user_input:
    response = chatbot.respond(user_input)

    if not response:
        response = "I am sorry, I did not understand that. Can you please rephrase your question?"

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Lucy", response))

for speaker, msg in st.session_state.history:
    st.write(f"**{speaker}**: {msg}")



 
