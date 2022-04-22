import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon=":apple:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.echo():
    st.write('This code will be printed')

# st.help(st.write)

dataframe = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
 })
st.experimental_show(dataframe)

st.experimental_set_query_params(
  show_map=True,
  selected=["asia"]
)

st.write(st.experimental_get_query_params())

df1 = pd.DataFrame(
    np.random.randn(3, 3),
    columns=('col %d' % i for i in range(3)))

my_table = st.table(df1)

df2 = pd.DataFrame(
    np.random.randn(3, 3),
    columns=('col %d' % i for i in range(3)))

my_table.add_rows(df2)
# Now the table shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'

st.text_input('GPU Name', key='gpu')
print(st.session_state.gpu)