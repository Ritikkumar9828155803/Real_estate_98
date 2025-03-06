import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

new_df = pd.read_csv('new_df.csv')
#feature_text = pickle.load(open('feature_text.pkl','rb'))


#group_df = new_df.groupby('sector').mean()[['price','price_per_sqft',' area','latitude','longitude']]
group_df=pd.read_csv("Gurgoan_sectors_latlong.csv")
st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)

#st.header('Features Wordcloud')

#wordcloud = WordCloud(width = 800, height = 800, background_color ='black', stopwords = set(['s']),  # Any stopwords you'd like to exclude min_font_size = 10).generate(feature_text)

#plt.figure(figsize = (8, 8), facecolor = None)
#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")
#plt.tight_layout(pad = 0)
#st.pyplot()

st.header('Area Vs Price')


fig1 = px.scatter(new_df, x="area", y="price", color="noOfOpenSides", title="Area Vs Price")

st.plotly_chart(fig1, use_container_width=True)


st.header('residency plot Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='noOfOpenSides')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='noOfOpenSides')

    st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side residency plot price comparison')

fig3 = px.box(new_df[new_df['noOfOpenSides'] <= 4], x='noOfOpenSides', y='price', title='Residency Plot Price Range')

st.plotly_chart(fig3, use_container_width=True)




