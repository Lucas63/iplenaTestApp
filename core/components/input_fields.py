from urllib.parse import urlparse

import streamlit as st


def is_valid_url(url):
    # Check if URL contains a dot ('.')
    if '.' not in url:
        return False
    # Further validate if it's a valid URL (basic check using urlparse)
    try:
        result = urlparse(url)
        # Check if the URL is valid (has a scheme and netloc)
        return result.scheme and result.netloc
    except ValueError:
        return False

def get_api_url():
    api_url = st.text_input('Enter the API URL:', '')
    #is_valid = is_valid_url(api_url)


    return f"https://{api_url}" #if is_valid else None