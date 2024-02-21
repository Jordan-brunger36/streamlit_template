import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer stats")

link = '[Welcome to my github pages site](https://jordan-brunger36.github.io/Github_assignment/)'
st.markdown(link, unsafe_allow_html=True)