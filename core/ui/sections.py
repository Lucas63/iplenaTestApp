from .components.image_loading import render_image_loading
from .components.image_processing import render_images_processing
from .components.spine_visualization import visualize_spine_side
from ..utils.constants import SPINE_SECTIONS
from ..utils.utils_chart import draw_side_spine, draw_front_data
from ..utils.utils_image import base64_to_image
import streamlit as st


def render_side_photo_analysis(side_data):
    st.subheader("Side Photo Analysis")
    col1, col2, _ = st.columns([4,4,1])

    with col1:
        st.json(side_data, expanded=False)
    with col2:
        draw_side_spine(side_data,col2)
    st.markdown("---")  # Separator


def render_front_photo_analysis(front_data):
    st.subheader("Front Photo Analysis(In development")
    col1, col2, _ = st.columns([4,4,1])

    with col1:
        st.json(front_data, expanded=False)
    with col2:
        draw_front_data(front_data,col2)
    st.markdown("---")  # Separator


def render_analysis_section(final_results):
    """Renders the analysis results for Front/Side/Sit photos."""
    st.header("Front/Side/Sit Photo Analysis (in development)")

    photo_analysis_results = final_results.get('results', {})
    side_data = photo_analysis_results.get("Side", None)
    front_data = photo_analysis_results.get("Front", None)

    if side_data:
        render_side_photo_analysis(side_data)

    if front_data:
        render_front_photo_analysis(front_data)

def render_spine_photos(final_results):
    """Renders the spine visualization results."""
    st.header("3D Spine Images")

    # Load and decode images
    side_base64 = final_results.get('spine_results', {}).get('image_side')
    front_base64 = final_results.get('spine_results', {}).get('image_front')

    side_image = base64_to_image(side_base64) if side_base64 else None
    front_image = base64_to_image(front_base64) if front_base64 else None

    # Settings
    target_height = 600  # Consistent height for both
    max_total_width = 125  # Total column units (used to proportionally allocate space)

    def scale_image(image):
        if image:
            aspect_ratio = image.width / image.height
            new_width = int(target_height * aspect_ratio)
            return image.resize((new_width, target_height)), new_width
        return None, 50  # Return dummy width to avoid division by zero

    side_img, side_w = scale_image(side_image)
    front_img, front_w = scale_image(front_image)

    # Total image width
    total_img_width = side_w + front_w
    side_ratio = side_w / total_img_width
    front_ratio = front_w / total_img_width

    # Column layout (gap, image1, spacer, image2, gap)
    gap_units = 5
    spacer_units = 3
    side_units = int((max_total_width - 2 * gap_units - spacer_units) * side_ratio)
    front_units = max_total_width - gap_units * 2 - spacer_units - side_units

    # Define layout
    _, col1, _, col2, _ = st.columns([gap_units, side_units, spacer_units, front_units, gap_units])

    with col1:
        st.subheader("Lateral View")
        if side_img:
            st.image(side_img)
        else:
            st.text("<<No image>>")

    with col2:
        st.subheader("Posterior View")
        if front_img:
            st.image(front_img)
        else:
            st.text("<<No image>>")

    st.markdown("---")

# def render_spine_photos(final_results):
#     """Renders the spine visualization results."""
#     st.header("3D Spine images")
#
#     side_image_width = 4.8
#     front_image_width = side_image_width / 2.411
#     _, col1, _,  col2, _ = st.columns([2, side_image_width, 2, front_image_width, 2])
#
#     # with col1:
#     #     st.json(final_results.get('spine_results', {}), expanded=False)
#     with col1:
#         st.subheader("Spine Lateral View")
#         image_base64 = final_results.get('spine_results', {}).get('image_side')
#         if image_base64:
#             image = base64_to_image(image_base64)
#             visualize_spine_side(image, column=col1)
#
#     with col2:
#         st.subheader("Spine Anterior View")
#         image_base64 = final_results.get('spine_results', {}).get('image_front')
#         if image_base64:
#             image = base64_to_image(image_base64)
#             visualize_spine_side(image, column=col2)
#
#     st.markdown("---")  # Separator


def render_service_info(service_data):
    st.header("Service Info")
    col1, col2, _ = st.columns(3)

    version = service_data.get("version", "??")
    version_description = service_data.get("version_description", "??")

    with col1:
        st.subheader("Version")
        st.markdown(f"<p style='font-size:18px;'>{version}</p>", unsafe_allow_html=True)

    with col2:
        st.subheader("Details")
        st.markdown(f"<p style='font-size:18px;'>{version_description}</p>", unsafe_allow_html=True)

    st.markdown("---")  # Separator


def draw_spine_sections():
    st.subheader("Spine Sections")

    for index, section in enumerate(SPINE_SECTIONS):
        col1, col2, col3 = st.columns([1, 3, 6])

        with col1:
            st.markdown(
                f"<div style='width: 30px; height: 20px; background-color: {section['color']}; border-radius: 1px;'></div>",
                unsafe_allow_html=True,
            )

        with col2:
            st.subheader(section["name"])

        with col3:
            st.markdown(f"<p style='font-size:16px;'>{section['description']}</p>", unsafe_allow_html=True)

        if index != len(SPINE_SECTIONS) - 1:
            st.markdown("<div style='margin: 5px 0;'></div>", unsafe_allow_html=True)  # Smaller space between sections

    st.markdown("---")  # Separator


def render_spine_visualization(final_results):
    """Renders the spine visualization results."""
    st.header("3D Spine visualization")

    draw_spine_sections()
    render_spine_photos(final_results)


def image_loading_section(api_url):
    # Create three columns for file uploader and image preview
    col1, col2, col3 = st.columns(3)

    # Render side image upload section
    front_image, side_image  = render_image_loading(col1, col2)

    final_results = render_images_processing(api_url, front_image, side_image) or {}

    return final_results
