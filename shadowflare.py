import streamlit as st
import requests
from urllib.parse import quote_plus

def get_magnet_links(search_term):
    url = f'https://apibay.org/q.php?q={quote_plus(search_term)}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if data:
            # Filter out results without the necessary fields
            valid_results = [result for result in data if all(key in result for key in ['info_hash', 'seeders', 'leechers'])]
            
            # Sort the valid results based on the number of seeds and peers in descending order
            sorted_data = sorted(valid_results, key=lambda x: (int(x['seeders']), int(x['leechers'])), reverse=True)
            
            # Get the top 10 magnet links
            top_10_links = [f"magnet:?xt=urn:btih:{result['info_hash']}" for result in sorted_data[:10]]
            
            return top_10_links
    return ["Magnet links not found"]

# Set page title and configure layout
st.set_page_config(page_title='ShadowFlare.io', layout='wide')

# Add a title and description
st.title('ShadowFlare')
st.write("Discover and retrieve magnet links for your files.")

# Input for the user to enter the name of the file
search_term = st.text_input('Enter the name of the file you want:')

# Button to trigger the magnet link retrieval
if st.button('Get Top 10 Magnet Links'):
    # Display a loading message while retrieving the magnet links
    with st.spinner('Fetching Top 10 Magnet Links...'):
        magnet_urls = get_magnet_links(search_term)
    
    # Display the retrieved top 10 magnet links
    for index, magnet_url in enumerate(magnet_urls, start=1):
        st.write(f'Magnet URL {index}: {magnet_url}')

# Footer with concise information, links, and torrenting disclaimer
st.sidebar.write("""
## About Me
**Samir Sengupta**

Passionate data scientist specializing in machine learning and data analysis. Check out my work on [GitHub](https://github.com/SamirSengupta) and connect with me on [LinkedIn](https://www.linkedin.com/in/samirsengupta/).

**Disclaimer**
Downloading copyrighted material without permission is against the law. This tool is intended for legal use only. Be responsible and respect intellectual property rights.
""")
