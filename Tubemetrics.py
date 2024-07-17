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

    ### 1. Categorical Analysis:
    
    Explore the distribution of top YouTube channels across different content categories. 
    Use interactive filters to select top YouTubers and categories, then dive into insightful visualizations 
    such as bar charts, treemaps, and bubble charts. Uncover trends and relationships among YouTube's leading creators 
    and gain valuable insights into what drives their success in various content categories.

    ### 2. Yearly Analysis:
    
    Analyze the growth and performance of top YouTube channels over different years. 
    Visualize trends in subscriber growth, video views, and video counts across various time periods. 
    Utilize interactive features to explore individual channel trajectories and understand the evolving landscape 
    of YouTube content creation over time.

    ### 3. YouTube Views per Video Analysis:
    
    Investigate the efficiency and engagement levels of top YouTube channels based on views per video. 
    Compare and contrast channels across different categories to identify outliers and best practices 
    in content production and audience engagement strategies. Utilize interactive bar charts and filters 
    to delve deeper into individual channel metrics and category-wide trends.

    ### 4. Comparative Analysis:
    
    Conduct side-by-side comparisons of key metrics between top YouTube influencers. 
    Select specific influencers and metrics of interest to visualize performance variations 
    and competitive advantages within the YouTube ecosystem. Leverage interactive features 
    to uncover insights into successful content strategies and audience engagement tactics.
    """
)
