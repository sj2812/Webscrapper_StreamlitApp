import streamlit as st
import scrapper
st.markdown('The best Webscrapper')
url_input=st.text_input('Enter the url to scrape')
if st.button('Search'):
    st.markdown('The content for'+ url_input + ' is')
    st.markdown(scrapper.scrapeurl(url_input))
    
