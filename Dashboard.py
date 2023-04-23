
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cyber Attacks Dashboard",
                   page_icon=":ninja:",
                   layout="wide"
)
                   
# Load the df
df = pd.read_csv("cyber_attacks.csv")


# Main Page
st.title(":ninja: Cyber Attacks Dashboard")
st.markdown("##")

# Top KPI's
#total no of attacks
total_attacks = len(df)
#top attacks
top_attacks = df.groupby('Type of Attack')['Type of Attack'].count().nlargest(1).index.tolist()
top_attack_str = str(top_attacks[0]).replace('[','').replace(']','').replace("'", "")
#top state
top_state = df.groupby('State')['State'].count().nlargest(1).index.tolist()
top_state_str = str(top_state[0]).replace('[','').replace(']','').replace("'", "")

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total No. of Attacks")
    st.subheader(f"{total_attacks:,}")
with middle_column:
    st.subheader("Top Attacks")
    st.subheader(f"{top_attack_str}")
with right_column:
    st.subheader("Top State")
    st.subheader(f"{top_state_str}")
st.markdown("---")

#-----dfVisualization-----
#PieChart Type of Cyber Attacks
type_counts = df['Type of Attack'].value_counts()
fig_pie = px.pie(type_counts, values=type_counts.values, names=type_counts.index,
title='Types of Attacks',
template="plotly_white",
)

# Group the df by month and get the count of attacks
monthly_attacks = df.groupby('Month')['Month'].count()

# Create a bar graph using Plotly
fig_bar = px.bar(x=monthly_attacks.values, y=monthly_attacks.index, orientation='h',
             labels={'x': 'Total Attacks', 'y': 'Month'})

# Add title and adjust layout
fig_bar.update_layout(title='Total Cyber Attacks by Month', )


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_pie, use_container_width=True)
right_column.plotly_chart(fig_bar, use_container_width=True)

#PieChart Type of Cyber Attacks
# Load data from CSV file
data = pd.read_csv('cyber_attacks.csv')

# Filter data to include only attacks from 2019 to 2022
data = data[(data['Year'] >= 2019) & (data['Year'] <= 2022)]

# Create a new column with a combined year and month value
data['YearMonth'] = pd.to_datetime(data['Year'].astype(str) + data['Month'], format='%Y%B')

# Group data by year and month and count the number of attacks
data_grouped = data.groupby(['YearMonth'])['Type of Attack'].count().reset_index()

# Create line graph with time series
fig = px.line(data_grouped, x='YearMonth', y='Type of Attack')

# Add range slider and selector
fig.update_layout(xaxis=dict(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    ),
    rangeslider=dict(
        visible=True
    ),
    type="date"
))


#SunBurst Chart
# Get top 5 states with the most cyber attacks
top_states = df.groupby('State').size().nlargest(5).index.tolist()

# Filter df for top 5 states
df_top_states = df[df['State'].isin(top_states)]

# Create a hierarchical index based on state, month, and type of attack
df_grouped = df_top_states.groupby(['State', 'Month', 'Type of Attack']).size()

# Reset the index to make the hierarchical index into columns
df_grouped = df_grouped.reset_index(name='Count')

# Create sunburst chart
fig_sun = px.sunburst(df_grouped, path=['State', 'Month', 'Type of Attack'], values='Count')
fig_sun.update_layout(title='Cyber Attacks on Top 5 States',
                  template="plotly_white",
)                  

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig, use_container_width=True)
right_column.plotly_chart(fig_sun, use_container_width=True)
st.markdown("---")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)








