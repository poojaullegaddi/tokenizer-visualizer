import streamlit as st
import tiktoken
import random

st.title("🔍 LLM Tokenizer Visualizer")

text = st.text_area("Enter your text below:")

if text:
    encoding = tiktoken.encoding_for_model("gpt-4o-mini")
    tokens = encoding.encode(text)
    decoded_tokens = [encoding.decode([token]) for token in tokens]

    st.subheader("📊 Statistics")
    st.write("Character count:", len(text))
    st.write("Token count:", len(tokens))
    st.write("Character-to-token ratio:", round(len(text)/len(tokens), 2))

    st.subheader("🎨 Token Visualization")

    colors = [
        "#FFCDD2", "#F8BBD0", "#E1BEE7", "#D1C4E9",
        "#C5CAE9", "#BBDEFB", "#B2EBF2", "#C8E6C9",
        "#DCEDC8", "#FFF9C4", "#FFE0B2"
    ]

    token_html = ""
    for token in decoded_tokens:
        color = random.choice(colors)
        token_html += f"<span style='background-color:{color}; padding:5px; margin:2px; border-radius:5px;'>{token}</span>"

    st.markdown(token_html, unsafe_allow_html=True)
