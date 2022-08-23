import streamlit as st

st.set_page_config(page_title="Evaluate Character", page_icon="📊")
st.title("Evaluate and parse a Character")

if st.session_state['player'] != '<select>':
    st.markdown("Lets do it !")
else:
    st.markdown("**Please select a player in Home Page !**")