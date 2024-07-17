import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
try:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='latin1')

# Ensure 'Category' column is of type string
data['Category'] = data['Category'].astype(str)

# Calculate views per video
data['Views per Video'] = data['Video Views'] / data['Video Count']

# Main title and description
st.markdown("# Views per Video Analysis")
st.write(
    """Explore YouTube channels based on views per video. Customize your view by selecting categories and the top N YouTubers. Dive into interactive bar charts showing views per video for individual YouTubers and aggregated by category."""
)

# Create Sidebar for filters
with st.sidebar:
    # Category Filter
    categories = sorted(data['Category'].unique())
    category_options = ['Select All'] + categories
    selected_categories = st.multiselect("Select Categories", category_options, default='Select All')

    # Top N Filter
    top_n_options = [5, 10, 25, 100, 500, 1000]
    selected_top_n = st.selectbox("Select Top N YouTubers", top_n_options, index=top_n_options.index(5))

# Filter data by selected categories
if 'Select All' in selected_categories:
    filtered_data = data
else:
    filtered_data = data[data['Category'].isin(selected_categories)]

# Create tabs for different visualizations
tab1, tab2 = st.tabs(["YouTubers", "Categories"])

# Tab 1: Bar Chart for Views per Video for Each YouTuber
with tab1:
    # Apply top N filter based on subscribers
    top_n_filtered_data_tab1 = filtered_data.nlargest(selected_top_n, 'Subscribers')
    
    st.write("## Views per Video for Each YouTuber")
    # Sort by Views per Video
    sorted_filtered_data_tab1 = top_n_filtered_data_tab1.sort_values(by='Views per Video', ascending=False)
    fig1 = px.bar(sorted_filtered_data_tab1, x='Youtuber', y='Views per Video', color='Category',
                  title='Views per Video for Each YouTuber',
                  labels={'Views per Video': 'Views per Video', 'Youtuber': 'YouTuber'})
    fig1.update_layout(showlegend=True)
    st.plotly_chart(fig1, use_container_width=True)
    st.write("## Analysis")
    st.write("""
    1. **Engagement vs. Quantity:** Channels like Cocomelon show high views per video despite having a lower number of videos compared to others. This indicates strong engagement from their primary audience, often children and caregivers, who repeatedly watch their content.
    2. **T-series and Music Category:** Despite T-series having the highest number of total views, it shows significantly lower views per video compared to channels like Cocomelon, indicating different consumption patterns between music and children's content.
    3. **Music and Educational Channels:** Music and educational channels tend to have higher views per video as viewers engage deeply with musical and/or informative content.
    """)

# Tab 2: Bar Chart for Views per Video for Each Category
with tab2:
    # Apply top N filter based on subscribers
    top_n_filtered_data_tab2 = filtered_data.nlargest(selected_top_n, 'Subscribers')
    
    st.write("## Views per Video for Each Category")
    # Group by category and calculate mean views per video, then sort
    category_views_per_video = top_n_filtered_data_tab2.groupby('Category')['Views per Video'].mean().reset_index()
    category_views_per_video = category_views_per_video.sort_values(by='Views per Video', ascending=False)
    fig2 = px.bar(category_views_per_video, x='Category', y='Views per Video', color='Category',
                  title='Views per Video for Each Category',
                  labels={'Views per Video': 'Views per Video', 'Category': 'Category'})
    fig2.update_layout(showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

    # Additional analysis points
    st.write("## Analysis")
    st.write("""
    1. **Music Category:** The music category consistently shows high views per video, driven by repeat consumption behaviors and the popularity of music content on YouTube.
    2. **Educational Channels:** Educational categories tend to have higher views per video due to their informative nature, encouraging viewers to watch and rewatch content.
    """)
