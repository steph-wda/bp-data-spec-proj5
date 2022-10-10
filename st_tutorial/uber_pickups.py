from distutils import filelist
import streamlit as st
import pandas as pd
import numpy as np

#Create title for page
st.title('Uber pickups in NYC')

#Loading data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data =pd.read_csv(DATA_URL,nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text("Done! (using st.cache)")
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(data[DATE_COLUMN].dt.hour,bins=24,range=(0,24))[0]
st.bar_chart(hist_values)


hour_to_filter = st.slider('hour',0,23,17)
filtered_data= data[data[DATE_COLUMN].dt.hour==hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


lat_count = data['lat'].value_counts()
lat_count

lon_count = data['lon'].value_counts()
lon_count


st.subheader(f'Map of all pickups at {hour_to_filter}:00')
