import streamlit as st
import requests
from urllib.parse import quote_plus

def get_magnet_link(search_term):
    url = f'https://apibay.org/q.php?q={quote_plus(search_term)}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            magnet_link = f"magnet:?xt=urn:btih:{data[0]['info_hash']}"
            return magnet_link
    return "Magnet link not found"

# Set page title and configure layout
st.set_page_config(page_title='ShadowFlare.io', layout='wide')

# Add a title and description
st.title('ShadowFlare')
st.write("Discover and retrieve magnet links for your files.")

# Input for the user to enter the name of the file
search_term = st.text_input('Enter the name of the file you want:')

# Button to trigger the magnet link retrieval
if st.button('Get Magnet Link'):
    # Display a loading message while retrieving the magnet link
    with st.spinner('Fetching Magnet Link...'):
        magnet_url = get_magnet_link(search_term)
    
    # Display the retrieved magnet link
    st.write('Magnet URL:', magnet_url)

# Footer with concise information, links, and torrenting disclaimer
st.sidebar.write("""
## About Me
**Samir Sengupta**

Passionate data scientist specializing in machine learning and data analysis. Check out my work on [GitHub](https://github.com/SamirSengupta) and connect with me on [LinkedIn](https://www.linkedin.com/in/samirsengupta/).

**Disclaimer**
Downloading copyrighted material without permission is against the law. This tool is intended for legal use only. Be responsible and respect intellectual property rights.
""")
