import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Nông Trại Vui Vẻ", layout="wide")

# Đọc file index.html và hiển thị lên web Streamlit
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

components.html(html_data, height=650, scrolling=True)
