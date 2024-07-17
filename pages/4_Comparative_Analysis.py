import streamlit as st
import pandas as pd
import plotly.express as px

# Attempt to read the CSV file with a specified encoding
try:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='latin1')

# Main title
st.markdown("# Comparative Analysis")
st.write(
    """Explore and analyze top YouTubers based on different metrics such as subscribers, video views, and number of videos. Customize your view by selecting the top N YouTubers and filtering by category. Interactive tabs provide easy navigation and visual representation through bar charts."""
)

# Create Sidebar for filters
with st.sidebar:
    # Top N Filter
    top_n_options = [5, 10, 25, 100, 500, 1000]
    selected_top_n = st.selectbox("Select Top N Youtubers", top_n_options)

    # Category Filter
    category_counts = data['Category'].value_counts()
    category_labels = category_counts.index.tolist()
    category_options = ['Select All'] + category_labels
    selected_category = st.selectbox("Select Category", category_options, index=0)

# Apply filters to the data
if selected_category == 'Select All':
    filtered_data = data
else:
    filtered_data = data[data['Category'] == selected_category]

# Create tabs
tab1, tab2, tab3 = st.tabs(["Subscribers", "Video Views", "Number of Videos"])

# Subscribers Tab
with tab1:
    st.write("# Subscribers")  # Tab title
    st.write("Discover the top YouTubers by subscriber count. See who's leading across different categories with an interactive bar chart.")
    # Sort by Subscribers in descending order
    filtered_data_tab1 = filtered_data.nlargest(selected_top_n, 'Subscribers').sort_values(by='Subscribers', ascending=True)
    
    # Create bar chart based on Subscribers
    fig_subs = px.bar(filtered_data_tab1, y='Youtuber', x='Subscribers', title='Top Youtubers by Subscribers')
    fig_subs.update_traces(marker=dict(color=['red' if i == len(filtered_data_tab1) - 1 else '#33a8ff' for i in range(len(filtered_data_tab1))]))
    fig_subs.update_layout(xaxis=dict(title='Subscribers'), yaxis=dict(title='YouTuber'))
    st.plotly_chart(fig_subs, use_container_width=True)
    st.write("## Analysis")
    st.write("""
    - Channels like Mr. Beast and T-series dominate across different categories, showcasing substantial growth and engagement.
    - The diversity of content categories among top channels highlights YouTube's broad appeal and viewer interests.
    """)

# Video Views Tab
with tab2:
    st.write("# Video Views")  # Tab title
    st.write("Explore the top YouTubers based on their video views with an interactive bar chart.")
    # Sort by Video Views in descending order
    filtered_data_tab2 = filtered_data.nlargest(selected_top_n, 'Video Views').sort_values(by='Video Views', ascending=True)
    
    # Create bar chart based on Video Views
    fig_views = px.bar(filtered_data_tab2, y='Youtuber', x='Video Views', title='Top Youtubers by Video Views')
    fig_views.update_traces(marker=dict(color=['red' if i == len(filtered_data_tab2) - 1 else '#33a8ff' for i in range(len(filtered_data_tab2))]))
    fig_views.update_layout(xaxis=dict(title='Video Views'), yaxis=dict(title='YouTuber'))
    st.plotly_chart(fig_views, use_container_width=True)
    st.write("## Analysis")
    st.write("""
    - T-series leads in total video views, emphasizing its dominance in the music category.
    - Viewer engagement varies widely across categories, influencing overall video view rankings.
    """)

# Number of Videos Tab
with tab3:
    st.write("# Number of Videos")  # Tab title
    st.write("Explore the top YouTubers based on the number of videos they have uploaded.")
    # Sort by Video Count in descending order
    filtered_data_tab3 = filtered_data.nlargest(selected_top_n, 'Video Count').sort_values(by='Video Count', ascending=True)
    
    # Create bar chart based on Video Count
    fig_videos = px.bar(filtered_data_tab3, y='Youtuber', x='Video Count', title='Top Youtubers by Number of Videos')
    fig_videos.update_traces(marker=dict(color=['red' if i == len(filtered_data_tab3) - 1 else '#33a8ff' for i in range(len(filtered_data_tab3))]))
    fig_videos.update_layout(xaxis=dict(title='Number of Videos'), yaxis=dict(title='YouTuber'))
    st.plotly_chart(fig_videos, use_container_width=True)
    st.write("## Analysis")
    st.write("""
    - Channels with frequent video uploads often cater to news and people-focused content, reflecting strategies to maintain viewer engagement.
    - Video count alone does not guarantee high subscriber or view counts, indicating the importance of content relevance and viewer preferences.
    """)
