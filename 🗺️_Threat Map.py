
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cyber Attacks Dashboard",
                   page_icon=":ninja:",
                   layout="wide"
)

# Load the data
df = pd.read_csv("cyber_attacks.csv")

# Main Page
st.title(":ninja: Cyber Attacks ThreatMap")
st.markdown("##")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)