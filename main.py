import streamlit as st
import pickle
import pandas as pd
import numpy as np



st.set_page_config(page_title="Viz Demo")



with open('df6.pkl', 'rb') as file:
    df=pickle.load(file)

with open('pipeline6.pkl','rb') as file:
    pipeline = pickle.load(file)

st.dataframe(df)

st.header('Enter your inputs')



# sector
sector = st.selectbox('sector', sorted(df['sector'].unique().tolist()))


#area
area=st.selectbox('area',sorted(df['area'].unique().tolist()))

#noOfOpenSides
noOfOpenSides=st.selectbox('noOfOpenSides',sorted(df['noOfOpenSides'].unique().tolist()))

#Rating
Rating=st.selectbox('Rating',sorted(df['Rating'].unique().tolist()))



#Shrine
Shrine=st.selectbox('Shrine',sorted(df['Shrine'].unique().tolist()))

#possession
possession=st.selectbox('possession',sorted(df['possession'].unique().tolist()))




Mall=st.selectbox('Mall',sorted(df['Mall'].unique().tolist()))

Airport=st.selectbox('Airport',sorted(df['Airport'].unique().tolist()))

Hospital=st.selectbox('Hospital',sorted(df['Hospital'].unique().tolist()))

price_per_sqft=st.selectbox('price_per_sqft',sorted(df['price_per_sqft'].unique().tolist()))

Metro=st.selectbox('Metro',sorted(df['Metro'].unique().tolist()))




if st.button('Predict'):

    # form a dataframe
    data = [[sector,area, noOfOpenSides, possession,
       price_per_sqft, Rating, Metro, Hospital, Shrine, Mall,
       Airport]]
    columns = ['sector', 'area', 'noOfOpenSides', 'possession',
       'price_per_sqft', 'Rating', 'Metro', 'Hospital', 'Shrine', 'Mall',
       'Airport']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text("The price of the flat is between {} and {} cr".format(round(low, 2), round(high, 2)))

