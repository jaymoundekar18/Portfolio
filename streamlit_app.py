
import streamlit as st
st.write("Hello!")

st.write("this is ")

st.write("JAY MOUNDEKAR")

st.echo()
with st.echo():
  st.write('Code will be executed and printed')

st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.sidebar.button('Submit')
