import streamlit as st

from core.components.image_loading import render_image_loading
from core.components.image_processing import render_images_processing
from core.components.input_fields import get_api_url
from core.components.spine_visualization import visualize_spine_side
from core.settings import init_app
from core.utils.utils_image import base64_to_image

init_app()


def draw_main_content(api_url):
    """Main function to render UI and process images."""

    # Create three columns for file uploader and image preview
    col1, col2, col3 = st.columns(3)

    # Render side image upload section
    side_image = render_image_loading(col1, col2, col3)

    st.divider()

    final_results = render_images_processing(api_url, side_image) or {}

    if final_results:
        render_analysis_section(final_results)
        render_spine_visualization(final_results)


def render_analysis_section(final_results):
    """Renders the analysis results for Front/Side/Sit photos."""
    st.subheader("Front/Side/Sit Photo Analysis (in development)")
    col1, _, _ = st.columns(3)

    with col1:
        st.json(final_results.get('results', {}).get("Side", {}), expanded=False)


def render_spine_visualization(final_results):
    """Renders the spine visualization results."""
    st.subheader("Spine Visualization (Side View)")

    col1, col2, _ = st.columns([3, 4, 1])

    with col1:
        st.json(final_results.get('spine_results', {}), expanded=False)

    image_base64 = final_results.get('spine_results', {}).get('image_side')
    if image_base64:
        image = base64_to_image(image_base64)
        visualize_spine_side(image, col2)


def draw_app():
    api_url = get_api_url()

    if api_url:
        draw_main_content(api_url)


draw_app()