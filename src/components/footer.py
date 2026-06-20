import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown (f"""
        <div style='display:flex; flex-direction:column; align-items:center; justify-content:center;'>
            <p style='font-weight:bold; color:white;'> Created with ❤️ by Palash Halder</p>
    """, unsafe_allow_html=True)



def footer_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown (f"""
        <div style='display:flex; flex-direction:column; align-items:center; justify-content:center;'>
            <p style='font-weight:bold; color:black;'> Created with ❤️ by Palash Halder</p>
    """, unsafe_allow_html=True)