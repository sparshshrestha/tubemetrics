import streamlit as st
import pandas as pd
import plotly.express as px

# Attempt to read the CSV file with a specified encoding
try:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='latin1')

# Main title
st.markdown("# Top YouTuber Insights")
st.write(
    """Explore and analyze top YouTubers based on different metrics such as subscribers, video views, and number of videos. Use filters to customize your view by selecting the top N YouTubers and filtering by category. The page features interactive tabs for easy navigation and visual representation of data through bar charts."""
)
st.image("images/youtube_insight.jpg", use_column_width=True)

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
tab1, tab2, tab3, tab4 = st.tabs(["Subscribers", "Video Views", "Number of Videos", "Subscribers vs. Video Count vs. Video Views"])

# Subscribers Tab
with tab1:
    st.write("# Subscribers")  # Tab title
    st.write("Discover the top YouTubers by subscriber count. See who's leading across different categories with an interactive bar chart.")
    # Sort by Subscribers in descending order
    filtered_data_tab1 = filtered_data.nlargest(selected_top_n, 'Subscribers').sort_values(by='Subscribers', ascending=True)
    
    # Create bar chart based on Subscribers
    fig_subs = px.bar(filtered_data_tab1, y='Youtuber', x='Subscribers', title='Top Youtubers by Subscribers')
    
    # Change the color of the top YouTuber to red
    fig_subs.update_traces(marker=dict(color=['red' if i == len(filtered_data_tab1) - 1 else '#33a8ff' for i in range(len(filtered_data_tab1))]))

    fig_subs.update_layout(xaxis=dict(title='Subscribers'), yaxis=dict(title='YouTuber'))  # Update layout
    st.plotly_chart(fig_subs, use_container_width=True)  # Display chart
    st.write("## Analysis")
    st.write("""
            1. Mr. Beast: Leading as the top YouTuber in the entertainment category and across all categories, showcasing significant subscriber growth and engagement.
            2. T-series: Second overall but the top YouTuber in the music category, highlighting its strong presence and viewer engagement in the music industry.
            3. Cocomelon - Nursery Rhymes: Holds the second position in the Education category but ranks third overall, indicating a strong niche audience and popularity in children's content.
            4. Set India: Fifth overall but dominates the Shows category, illustrating a focused audience interested in television content and entertainment.
            5. PewDiePie: Previously ranked as the second top YouTuber overall, now stands at the 10th position, maintaining its top position in the gaming category despite the overall rank drop, suggesting evolving viewer preferences and competition.
            6. Diverse Content Categories: The top YouTubers demonstrate diversity in their content categories, indicating that success on YouTube is not limited to a single genre. This diversity underscores the platform's broad appeal and the varied interests of its global audience.
            """)

# Video Views Tab
with tab2:
    st.write("# Video Views")  # Tab title
    st.write("Explore the top YouTubers based on their video views. This tab visualizes the most viewed creators across different categories with an interactive bar chart highlighting the top performer.")
    # Sort by Video Views in descending order
    filtered_data_tab2 = filtered_data.nlargest(selected_top_n, 'Video Views').sort_values(by='Video Views', ascending=True)
    
    # Create bar chart based on Video Views
    fig_views = px.bar(filtered_data_tab2, y='Youtuber', x='Video Views', title='Top Youtubers by Video Views')
    
    # Change the color of the top YouTuber to red
    fig_views.update_traces(marker=dict(color=['red' if i == len(filtered_data_tab2) - 1 else '#33a8ff' for i in range(len(filtered_data_tab2))]))

    fig_views.update_layout(xaxis=dict(title='Video Views'), yaxis=dict(title='YouTuber'))  # Update layout
    st.plotly_chart(fig_views, use_container_width=True)  # Display chart
    st.write("## Analysis")
    st.write("""
            1. T-Series: Leading in overall video views and specifically dominating the Music category, leveraging its status as a Bollywood music production company with repeat viewership.
            2. Cocomelon - Nursery Rhymes: Second in overall video views, driven by its popularity in children's content, particularly nursery rhymes that are frequently watched on mobile devices.
            3. Set India: Third in overall video views but holds the top spot in the Shows category, demonstrating strong engagement among viewers interested in television content.
            4. Viewership Dynamics: The relationship between subscriber count and video views varies significantly. For instance, Mr. Beast, the most subscribed channel, ranks 19th in terms of video views, highlighting that factors beyond subscriber numbers influence viewership metrics. 
            """)

# Number of Videos Tab
with tab3:
    st.write("# Number of Videos")  # Tab title
    st.write("Explore the top YouTubers based on the number of videos they have uploaded. This tab visualizes the most prolific creators across different categories with an interactive bar chart highlighting the top performer in terms of video count.")
    # Sort by Video Count in descending order
    filtered_data_tab3 = filtered_data.nlargest(selected_top_n, 'Video Count').sort_values(by='Video Count', ascending=True)
    
    # Create bar chart based on Video Count
    fig_videos = px.bar(filtered_data_tab3, y='Youtuber', x='Video Count', title='Top Youtubers by Number of Videos')
    
    # Change the color of the top YouTuber to red
    fig_videos.update_traces(marker=dict(color=['red' if i == len(filtered_data_tab3) - 1 else '#33a8ff' for i in range(len(filtered_data_tab3))]))

    fig_videos.update_layout(xaxis=dict(title='Number of Videos'), yaxis=dict(title='YouTuber'))  # Update layout
    st.plotly_chart(fig_videos, use_container_width=True)  # Display chart
    st.write("## Analysis")
    st.write("""
            1. Diverse Rankings: The top channels by number of videos uploaded do not rank highly in terms of subscribers or total views.
            2. Category Insights: Many top video uploaders fall under News or People & Blogs categories, indicating a strategy of frequent content updates to capture viewer attention.
            3. TV9 Bharatvarsh: Ranked first in video uploads but lacks competitive positioning in subscriber and views counts, highlighting the importance of content relevance over quantity.
            4. Content Relevance: The analysis suggests that viewer engagement and subscriber growth are primarily driven by content that resonates with audience interests, rather than simply the volume of uploads.            
            """)
    
with tab4:
    st.write("# Subscribers vs. Video Count vs. Video Views")  # Tab title
    st.write("Explore the relationship between top YouTubers based on their subscriber counts, video production volume, and total video views. This interactive bubble chart visualizes these metrics, with bubble size representing video views and colors indicating different content categories.")
    # Apply filters to the data
    if selected_category == 'Select All':
        filtered_data_tab4 = data.nlargest(selected_top_n, 'Subscribers').sort_values(by='Subscribers', ascending=True)
    else:
        filtered_data_tab4 = data[data['Category'] == selected_category].nlargest(selected_top_n, 'Subscribers').sort_values(by='Subscribers', ascending=True)
    
    # Create bubble chart based on Subscribers, Video Count, and Video Views
    fig_bubble = px.scatter(filtered_data_tab4, x='Subscribers', y='Video Count', size='Video Views', color='Category',
                            hover_name='Youtuber', size_max=30, title='Subscribers vs. Video Count vs. Video Views')

    fig_bubble.update_layout(xaxis=dict(title='Subscribers'),
                             yaxis=dict(title='Video Count'),
                             showlegend=True)
    
    st.plotly_chart(fig_bubble, use_container_width=True)  # Display bubble chart
    st.write("## Analysis")
    st.write("""
            1. Viewership and Subscribers: The number of views on a channel depends more on the number of subscribers rather than the total number of videos uploaded, emphasizing the importance of audience engagement over sheer content volume.
            2. Quality Over Quantity: This observation underscores that high-quality content is more crucial for attracting views and subscribers than the quantity of videos produced.
            3. YouTube Movies Channel: An interesting outlier is the YouTube Movies channel, which ranks third in subscribers but has zero videos and views. This channel operates differently by offering movies for rent or purchase, rather than producing original content like other channels.
            4. Subscriber Gaps: There is a significant gap in subscriber counts between the top 2 channels compared to the 3rd and 4th, and similarly, a large gap exists between the 3rd and 4th ranked channels. This indicates varying levels of popularity and reach among the top YouTubers.
             """)
