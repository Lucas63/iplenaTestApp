import streamlit as st
from PIL import Image, ImageOps


def visualize_spine_side(image_side,column):
    with column:
        st.image(image_side, caption="Image from API", use_container_width=True)