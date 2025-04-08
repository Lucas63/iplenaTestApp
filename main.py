import streamlit as st

from core.ui.components.image_loading import render_image_loading
from core.ui.components.image_processing import render_images_processing
from core.ui.components.input_fields import get_api_url
from core.ui.components.spine_visualization import visualize_spine_side
from core.settings import init_app
from core.ui.sections import render_analysis_section, render_spine_visualization, render_service_info, \
    draw_spine_sections, image_loading_section
from core.utils.utils_image import base64_to_image

init_app()


def draw_main_content(api_url):
    """Main function to render UI and process images."""

    final_results = image_loading_section(api_url)

    if final_results:
        side_photo_data = final_results.get("results",{}).get("Side", {})
        app_info = side_photo_data.get("app_info", {})
        render_service_info(app_info)

    if final_results:
        render_analysis_section(final_results)
        render_spine_visualization(final_results)

    # draw_spine_sections()




def draw_app():
    api_url = get_api_url()

    if api_url:
        draw_main_content(api_url)


draw_app()