###
# 1
###
# import streamlit as st

# st.title('Counter Example')
# if 'count' not in st.session_state:
#     st.session_state.count = 0
# increment = st.button('Increment')

# if increment:
#     st.session_state.count += 1

# st.write('Count = ', st.session_state.count)


###
# 2
###
# import streamlit as st

# st.title('Counter Example using Callbacks')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def increment_counter():
#     st.session_state.count += 1

# st.button('Increment', on_click=increment_counter)

# st.write('Count = ', st.session_state.count)


###
# 3
###
# import streamlit as st

# st.title('Counter Example using Callbacks with kwargs')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def increment_counter(increment_value=0):
#     st.session_state.count += increment_value

# def decrement_counter(decrement_value=0):
#     st.session_state.count -= decrement_value

# st.button('Increment(5)', on_click=increment_counter,
#     kwargs=dict(increment_value=5))

# st.button('Decrement(1)', on_click=decrement_counter,
#     kwargs=dict(decrement_value=1))

# st.write('Count = ', st.session_state.count)


###
# 4
###
# import streamlit as st
# import datetime

# st.title('Counter Example')
# if 'count' not in st.session_state:
#     st.session_state.count = 0
#     st.session_state.last_updated = datetime.time(0,0)

# def update_counter():
#     st.session_state.count += st.session_state.increment_value
#     st.session_state.last_updated = datetime.datetime.now().time()

# with st.form(key='my_form'):
#     st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
#     st.number_input('Enter a value', value=0, step=1, key='increment_value')
#     submit = st.form_submit_button(label='Update', on_click=update_counter)

# st.write('Current Count = ', st.session_state.count)
# st.write('Last Updated = ', st.session_state.last_updated)


# import streamlit as st

# if "celsius" not in st.session_state:
#     # set the initial default value of the slider widget
#     st.session_state.celsius = 50.0

# # st.slider(
# #     "Temperature in Celsius",
# #     min_value=-100.0,
# #     max_value=100.0,
# #     key="celsius"
# # )

# st.file_uploader('upload')

# # This will get the value of the slider widget
# st.write(st.session_state.celsius)


# import streamlit as st

# if 'my_button' not in st.session_state:
#     st.session_state.my_button = True
#     # Streamlit will raise an Exception on trying to set the state of button

# st.button('Submit', key='my_button')