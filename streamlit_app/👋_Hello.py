import pandas as pd
import streamlit as st
import pandas

## Config

PATH_TO_DATA = "../data/Characters.csv"
df = pd.read_csv(PATH_TO_DATA)



st.set_page_config(page_title="Hello", page_icon="👋",)
st.title("Roleplay Station")
st.markdown("### Welcome to **Roleplay Station**, the first RPG feedback tool")

st.markdown("Roleplay Station let you give elaborate feedback about character you played, or played with, as well as your feeling about the whole game.")





st.markdown("## First of all, we need to know who you are !")
st.session_state['player'] = st.selectbox('Who are you ?',["<select>"] + list(df.player.unique()))

if st.session_state['player'] != "<select>":
    st.markdown(f"Hi {st.session_state['player']}, Nice to see ya !")
    st.session_state['player'] = st.session_state['player']