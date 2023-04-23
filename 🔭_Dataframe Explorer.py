import streamlit as st
import pandas as pd
st.set_page_config(page_title="Dataframe Explorer",
                   page_icon=":telescope:",
                   layout="wide"
)

# Load the data
df = pd.read_csv("cyber_attacks.csv")


# Main Page
st.title(":telescope: Cyber Attacks Dashboard")
st.markdown("##")

from streamlit_extras.dataframe_explorer import dataframe_explorer


filtered_df = dataframe_explorer(df, case=False)
st.dataframe(filtered_df, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)