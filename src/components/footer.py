import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown (f"""
        <div style='display:flex; flex-direction:column; align-items:center; justify-content:center;'>
            <p style='font-weight:bold;'> Created with ❤️ by Palash Halder</p>
    """, unsafe_allow_html=True)