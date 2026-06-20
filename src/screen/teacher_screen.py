import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard


def teacher_screen():
    style_background_dashboard()
    style_base_layout()



    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type=='login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type =="register":
        teacher_screen_register()


def teacher_screen_login():
    c1,c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type']= None
            st.rerun()

    # st.header('Teacher Screen')
    st.markdown("""<style>
        div[data-testid="stHeading"] h2{
            color:#2f323f !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.header("Login using password")

    st.markdown("""
        <style>
        /* Label */
        div[data-testid="stTextInput"] label {
            color: #2f323f !important;
            font-weight: 600 !important;
        }

        /* Container around input */
        div[data-testid="stTextInput"] > div > div {
            background-color:white !important;
            border-radius: 12px !important;
        }

        /* Actual input */
        div[data-testid="stTextInput"] input {
            background-color: white !important;
            color: #2f323f !important;
        }

        /* Placeholder */
        div[data-testid="stTextInput"] input::placeholder {
            color: #7B7E8F !important;
            opacity: 1 !important;
        }

        /* Remove dark border */
        div[data-testid="stTextInput"] div[data-baseweb="input"] {
            border: 1px solid #C7CCFF !important;
            background-color: white !important;
        }

        </style>
    """, unsafe_allow_html=True)
    teacher_username = st.text_input("Enter Username", placeholder="Username")    
    
    teacher_pass = st.text_input("Enter Password", placeholder="Password", type="password")

    st.divider()

    btnc1,btnc2 = st.columns(2)

    with btnc1:
        st.button('Login', icon=':material/passkey:', shortcut='control+enter', width="stretch")
    with btnc2:
        if st.button('Register', type='primary', icon=':material/passkey:', width="stretch"):
            st.session_state.teacher_login_type = "register"
            st.rerun()

    footer_dashboard()


def teacher_screen_register():
    c1,c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type="secondary", key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type']= None
            st.rerun()


    # st.header('Teacher Screen')
    st.markdown("""<style>
        div[data-testid="stHeading"] h2{
            color:#2f323f !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.header("Register your teacher profile")

    st.markdown("""
        <style>
        /* Label */
        div[data-testid="stTextInput"] label {
            color: #2f323f !important;
            font-weight: 600 !important;
        }

        /* Container around input */
        div[data-testid="stTextInput"] > div > div {
            background-color:white !important;
            border-radius: 12px !important;
        }

        /* Actual input */
        div[data-testid="stTextInput"] input {
            background-color: white !important;
            color: #2f323f !important;
        }

        /* Placeholder */
        div[data-testid="stTextInput"] input::placeholder {
            color: #7B7E8F !important;
            opacity: 1 !important;
        }

        /* Remove dark border */
        div[data-testid="stTextInput"] div[data-baseweb="input"] {
            border: 1px solid #C7CCFF !important;
            background-color: white !important;
        }

        </style>
    """, unsafe_allow_html=True)
    teacher_username = st.text_input("Enter Username", placeholder="Username")

    teacher_name = st.text_input("Enter Name", placeholder="Teacher Name")

    teacher_pass = st.text_input("Enter Password", placeholder="Password", type="password")

    teacher_pass_confirm = st.text_input("Confirm Password", placeholder="Password", type="password")

    st.divider()

    btnc1,btnc2 = st.columns(2)

    with btnc1:
        st.button('Register', icon=':material/passkey:', shortcut='control+enter', width="stretch")
    with btnc2:
        if st.button('Login', type='primary', icon=':material/passkey:', width="stretch"):
            st.session_state.teacher_login_type = "login"
            st.rerun()

    footer_dashboard()