# -*- coding: utf-8 -*-
#app.py
import APP1
import APP2
import streamlit as st
PAGES = {
    "App1": APP1,
    "App2": APP2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
