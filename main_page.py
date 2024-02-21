import streamlit as st

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer stats")

link = '[Welcome to my github apges site](https://github.com/Jordan-brunger36/Github_assignment.git)'
st.markdown(link, unsafe_allow_html=True)