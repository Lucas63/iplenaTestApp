import streamlit as st
from PIL import Image, ImageOps


def visualize_spine_side(image_side,col_2):
    with col_2:
        st.image(image_side, caption="Image from API", use_column_width=True)