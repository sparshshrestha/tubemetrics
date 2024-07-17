import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
try:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv('data/Top Youtubers Dataset.csv', encoding='latin1')

# Ensure 'Started' column is of type integer
data['Started'] = data['Started'].astype(int)

# Main title and description
st.markdown("# Yearly Analysis")
st.write(
    """Welcome to the Yearly Analysis of Top YouTubers! Here, you can explore and analyze top YouTube channels based on metrics such as subscribers, video views, and video counts, filtered by the year they started. Customize your view by selecting the top N YouTubers for each year to uncover trends and insights into YouTube's leading creators. Dive into interactive visualizations like bar charts to see who dominated each year in terms of subscribers and explore their categories. Join us in dissecting the annual evolution of YouTube influencers and their impact!"""
)

# Create Sidebar for filters
with st.sidebar:
    # Top N Filter
    top_n_options = [10, 25, 100, 500, 1000]
    selected_top_n = st.selectbox("Select Top N YouTubers", top_n_options)
    
    # Year Filter
    years = sorted(data['Started'].unique())
    default_year = 2012
    selected_year = st.selectbox("Select Year", years, index=years.index(default_year))

# Filter data by selected year and top N YouTubers
filtered_data = data[data['Started'] == selected_year].nlargest(selected_top_n, 'Subscribers')

# Sort filtered data by Subscribers in descending order
filtered_data = filtered_data.sort_values(by='Subscribers', ascending=False)

# Display the filtered data
st.write(f"## Top YouTubers who started in {selected_year}")
st.write(filtered_data[['Rank', 'Youtuber', 'Subscribers', 'Video Views', 'Video Count', 'Category', 'Started']])

# Create a bar chart for top YouTubers by year
st.write("## Top YouTuber by Start Year")
fig = px.bar(filtered_data, x='Youtuber', y='Subscribers', color='Category',
             title=f'Top YouTuber(s) in {selected_year} by Subscribers',
             labels={'Subscribers': 'Subscribers', 'Youtuber': 'Top YouTuber(s)'})
fig.update_xaxes(title='Top YouTuber(s)')
fig.update_yaxes(title='Subscribers')
fig.update_layout(showlegend=True)

st.plotly_chart(fig, use_container_width=True)

st.write("## Analysis")
st.write("""
    1. **Diverse Categories for New YouTubers:** Each year, the top YouTubers tend to come from different content categories, demonstrating that new content creators are not merely following trends but are instead focusing on their unique skills and interests. This variety highlights the richness and diversity of content on YouTube, where different niches can gain significant followings.
    2. **Skill Over Popularity:** The data suggests that new YouTubers prioritize their expertise and passion over creating content in already popular categories. This indicates a platform that rewards originality and niche expertise, allowing creators to thrive by offering unique value to their audiences.
    3. **Evolving Trends:** As new YouTubers emerge from different categories each year, it reflects the evolving interests and demands of the audience. This dynamic landscape suggests that YouTube continues to grow and adapt, providing opportunities for diverse content creators to succeed regardless of prevailing trends.
""")
