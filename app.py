import streamlit as st
import pandas as pd
import numpy as np
import time
from sqlalchemy.orm import sessionmaker

# 表格
dataframe = pd.DataFrame(
    np.random.randn(3, 2),
    index=None,
    columns=['col1', 'col2']
)
st.table(dataframe)

# 滑动条

slider = st.slider('This is a slider')
st.write(f'Value of slider: {slider}')

# 按钮
button = st.button('This is a button')
st.write(f'Is the button clicked: {button}')
selectbox = st.selectbox('This is a drop-down option box ', ('A', 'B', 'C'))
st.write(f'Option you selected: {selectbox}')

# 每个带有key的小部件都会自动添加到session state
# text_input的值与st.session_state.input等价
text_input = st.text_input('This is a text input box', key='input')
st.write(f'Value you entered is: {st.session_state.input}')

# 使用复选框显示或隐藏数据
if st.checkbox('Show table'):
    chart_data = pd.DataFrame(
        np.random.randn(3, 3),
        columns=['a', 'b', 'c'])
    st.table(chart_data)

## 布局

### 左侧边栏
sidebar_sider = st.sidebar.slider('This is a slider for sidebar')
sidebar_selectbox = st.sidebar.selectbox('This is a drop-down option box for sidebar', ('A', 'B', 'C'))

### 并排显示
left_column, right_column = st.columns(2)
left_column.button('Left button')
right_column.button('Right button')

### 折叠展开

#### 方法1
with st.expander('Expander'): # 用with也可以绑定到别的组件上
     st.write('The hidden content is a picture.')
     st.image('ひみつ_pixiv.net_95225496.png')

#### 方法2
expander = st.expander('Expander')
expander.write('The hidden content is a picture.')
expander.image('ひみつ_pixiv.net_95225496.png')

# 注意st.echo and st.spinner目前不支持在左侧边栏和布局选项中使用

### 进度条

# 添加一个占位符
st.write('This is a progress bar')
bar = st.progress(0)
placeholder = st.empty()
for i in range(100):
    placeholder.text(f'Value of progress bar: {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

### 缓存

#### 不推荐使用st.cache，速度慢
@st.cache
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    for i in range(10):
        time.sleep(0.1)
    output = arg1+arg2
    return output

#### @st.experimental_memo可以现实昂贵的计算
@st.experimental_memo
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)


#### @st.experimental_singleton用来存储键值，共享全局单例对象，适合跨会话，例如TensorFlow/Torch/Keras 会话或者数据库连接
@st.experimental_singleton
def get_db_sessionmaker():
    # This is for illustration purposes only
    DB_URL = "your-db-url"
    engine = create_engine(DB_URL)
    return sessionmaker(engine)

# @st.experimental_memo：数据流计算，存储下载数据 @st.experimental_singleton：Tensorflow会话，数据库连接

### 清除缓存
@st.experimental_memo
def square(x):
    return x**2

a, b = st.columns(2)
if a.button("Clear square cache"):
    # Clear square's memoized values:
    square.clear()

if b.button("Clear all cache"):
    # Clear values from *all* memoized functions:
    st.experimental_memo.clear()

with st.spinner('Wait for it...spinner'):
    time.sleep(3)
st.success('spinner')

st.balloons()
st.snow()

st.error('error')
st.warning('warning')
st.info('info')
st.success('success')
st.exception(RuntimeError('This is an exception of type RuntimeError'))

with st.form(key='form'):
    username = st.text_input("Username")
    password = st.text_input("Password")
    st.form_submit_button("Login")

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')
# rerun
st.experimental_rerun()
