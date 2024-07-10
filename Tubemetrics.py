import streamlit as st
import pandas as pd
import numpy as np

# Set the title
st.title('YouTube Data Analysis')

# Sidebar success message
st.sidebar.success("Analysis Filters")

# Main page content
st.markdown(
    """
    Welcome to our YouTube Data Analysis Dashboard, a comprehensive platform designed to provide insightful
    and actionable analysis on top YouTubers. Leveraging the power of Streamlit, our dashboard offers an intuitive
    and interactive interface that caters to researchers, marketers, and content creators. Explore various data visualizations, 
    track trends, and delve into in-depth analyses to better understand the patterns and factors influencing YouTube success. 
    Our goal is to empower you with the knowledge needed to drive impactful decisions and improve your content strategy through data-driven insights.
    """
)

# Add an image
st.image("images/youtube_home_page.jpg", caption='YouTube Data Analysis')

# Detailed description of each page
st.markdown(
    """
    ## Page Descriptions:

    ### 1. Top Youtuber Insight
    This page provides a comprehensive analysis of top YouTubers through four interactive tabs: 
    **Subscribers**, **Video Views**, **Number of Videos**, and **Subscribers vs. Video Count vs. Video Views**. 
    Each tab offers unique insights into YouTube channel performance, visualizing key metrics such as subscriber counts, total video views, video upload volume, and their interrelationships.
    """
)
