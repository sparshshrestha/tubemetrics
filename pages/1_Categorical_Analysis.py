import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Attempt to read the CSV file with a specified encoding
try:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='latin1')

# Ensure 'Category' column is of type string
data['Category'] = data['Category'].astype(str)

# Calculate views per video
data['Views per Video'] = data['Video Views'] / data['Video Count']

# Main title and description
st.markdown("# Categorical Analysis")
st.write(
    """Welcome to the Categorical Analysis of Top YouTubers! Dive into the world of top YouTube channels, categorized by subscribers, video views, and video counts. Use interactive filters to select top YouTubers and categories, then explore insightful visualizations across tabs, including bar charts, treemaps, and bubble charts. Uncover meaningful trends and relationships among YouTube's leading creators and gain valuable insights into what drives their success in different content categories."""
)

# Create Sidebar for filters
with st.sidebar:
    # Top N Filter
    top_n_options = [1000, 500, 100, 25, 10, 5]
    selected_top_n = st.selectbox("Select Top N YouTubers", top_n_options)
    
    # Category Filter
    category_counts = data['Category'].value_counts()
    category_labels = category_counts.index.tolist()
    category_options = ['Select All'] + category_labels
    selected_categories = st.multiselect("Select Categories", category_options, default='Select All')

# Apply top N filter
data = data.nlargest(selected_top_n, 'Subscribers')

# Apply category filter
if 'Select All' not in selected_categories:
    data = data[data['Category'].isin(selected_categories)]

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs(["Category", "Subscribers by Category", "Video Views & Counts", "Subscribers vs. Video Count vs. Video Views"])

# Tab 1: Category Bar Chart
with tab1:
    st.write("## Category")
    st.write("Explore the distribution of top YouTube channels across different content categories with an interactive bar chart based on channel counts per category.")
    # Group by category and count occurrences
    category_count = data['Category'].value_counts().reset_index()
    category_count.columns = ['Category', 'Count']

    # Sort the data for better visualization
    category_count = category_count.sort_values(by='Count', ascending=False)

    # Create a color list where the top category bar is red and others are a default color
    colors = ['red' if i == 0 else '#33a8ff' for i in range(len(category_count))]

    # Create bar chart using Plotly Express
    fig1 = px.bar(category_count, x='Category', y='Count', title='YouTube Category Counts', labels={'Count': 'Count', 'Category': 'YouTube Category'})

    # Update the bar color
    fig1.update_traces(marker=dict(color=colors))

    # Streamlit app
    st.plotly_chart(fig1, use_container_width=True)  # Display chart

    # Analysis
    st.write("## Analysis")
    st.write("""
    1. **Popularity of Categories:** The bar chart shows which categories have the highest number of top YouTubers. Categories with more channels indicate a higher popularity and demand for content in those areas.
    2. **Dominant Categories:** Certain categories dominate the YouTube landscape, attracting a large number of top creators. This trend highlights the audience's interests and preferences for specific types of content.
    """)

# Tab 2: Subscribers by Category Treemap
with tab2:
    st.write("## Subscribers by Category")
    st.write("Visualize the distribution of total subscribers across different content categories using a Treemap.")

    # Group by category and sum subscribers
    category_subscribers = data.groupby('Category')['Subscribers'].sum().reset_index()

    # Create Treemap using Plotly Express
    fig2 = px.treemap(category_subscribers, path=['Category'], values='Subscribers',
                      title='Subscribers by YouTube Category',
                      color='Subscribers', hover_data=['Subscribers', 'Category'],
                      color_continuous_scale=px.colors.sequential.Viridis[::-1],  # Change the color palette
                      labels={'Subscribers': 'Subscribers'})

    # Customize hover template to display count
    fig2.update_traces(textinfo='label+value')

    # Streamlit app
    st.plotly_chart(fig2, use_container_width=True)  # Display chart

    st.write("## Analysis")
    st.write("""
    1. **Audience Engagement:** The treemap shows how subscribers are distributed across different categories. Categories with a larger share of subscribers indicate higher audience engagement and interest.
    2. **Insights into Popularity:** The visualization helps in understanding which categories are the most popular among viewers, reflecting the success and reach of content creators in those areas.
    """)

# Tab 3: Separate Bar Charts for Video Views and Video Counts
with tab3:
    st.write("## Video Views & Video Counts")
    st.write("Compare the total video views and video counts for each category with separate bar charts.")

    # Group by category and sum video views and counts
    category_views = data.groupby('Category')['Video Views'].sum().reset_index()
    category_counts = data.groupby('Category')['Video Count'].sum().reset_index()

    # Sort data for both charts
    category_views_sorted = category_views.sort_values(by='Video Views', ascending=False)
    category_counts_sorted = category_counts.sort_values(by='Video Count', ascending=False)

    # Create a color list where the top category bar is red and others are a default color
    colors_views = ['red' if i == 0 else '#33a8ff' for i in range(len(category_views_sorted))]
    colors_videos = ['red' if i == 0 else '#33a8ff' for i in range(len(category_counts_sorted))]

    # Create Bar Chart for Video Views
    fig_views = px.bar(category_views_sorted, x='Category', y='Video Views',
                       title='Total Video Views by YouTube Category',
                       labels={'Video Views': 'Total Video Views', 'Category': 'YouTube Category'})

    # Update the bar color
    fig_views.update_traces(marker=dict(color=colors_views))

    # Create Bar Chart for Video Counts
    fig_counts = px.bar(category_counts_sorted, x='Category', y='Video Count',
                        title='Total Video Counts by YouTube Category',
                        labels={'Video Count': 'Total Video Counts', 'Category': 'YouTube Category'})

    # Update the bar color
    fig_counts.update_traces(marker=dict(color=colors_videos))

    # Display charts
    st.plotly_chart(fig_views, use_container_width=True)
    st.plotly_chart(fig_counts, use_container_width=True)

    # Analysis
    st.write("## Analysis")
    st.write("""
    1. **High Video Views:** Categories with the highest total video views indicate strong viewer interest and engagement. These categories often align with popular trends and topics.
    2. **Content Production:** The bar charts reveal the volume of content production in each category. Categories with higher video counts may indicate more frequent content updates and active creators.
    """)

# Tab 4: Bubble Chart for Subscribers vs. Video Count vs. Video Views
with tab4:
    st.write("## Subscribers vs. Video Count vs. Video Views")
    st.write("Explore the relationship between top YouTubers based on their subscriber counts, video production volume, and total video views. This interactive bubble chart visualizes these metrics, with bubble size representing video views and colors indicating different content categories.")

    # Filter data based on the selected categories and top N YouTubers
    filtered_data_tab4 = data.nlargest(selected_top_n, 'Subscribers')
    if 'Select All' not in selected_categories:
        filtered_data_tab4 = filtered_data_tab4[filtered_data_tab4['Category'].isin(selected_categories)]

    # Create bubble chart based on Subscribers, Video Count, and Video Views
    fig_bubble = px.scatter(filtered_data_tab4, x='Subscribers', y='Video Count', size='Video Views', color='Category',
                            hover_name='Youtuber', size_max=30, title='Subscribers vs. Video Count vs. Video Views',
                            color_discrete_sequence=px.colors.qualitative.Light24)

    fig_bubble.update_layout(xaxis=dict(title='Subscribers'),
                             yaxis=dict(title='Video Count'),
                             showlegend=True)

    st.plotly_chart(fig_bubble, use_container_width=True)  # Display bubble chart
    st.write("## Analysis")
    st.write("""
    1. **Viewership and Subscribers:** The number of views on a channel often correlates more with the number of subscribers rather than the total number of videos uploaded, emphasizing the importance of audience engagement over sheer content volume.
    2. **Quality Over Quantity:** High-quality content is more crucial for attracting views and subscribers than the quantity of videos produced.
    3. **YouTube Movies Channel:** An interesting outlier is the YouTube Movies channel, which ranks third in subscribers but has zero videos and views. This channel operates differently by offering movies for rent or purchase, rather than producing original content like other channels.
    4. **Subscriber Gaps:** Significant gaps in subscriber counts between the top channels indicate varying levels of popularity and reach among the top YouTubers.
    """)
