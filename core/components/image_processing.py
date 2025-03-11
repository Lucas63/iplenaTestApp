import streamlit as st

from ..api import upload_front_photo, upload_right_side_photo, upload_sit_photo, get_spine


def render_images_processing(LOCAL_URL, side_image):
    """Processes images step by step with progress updates and messages."""

    if st.button("Process Images"):
        results = {}
        progress_bar = st.progress(0)
        status_text = st.empty()  # Placeholder for status updates
        progress_step = 0.5  # Two steps (0.5 per step)

        with st.spinner("Processing images..."):
            # Step 1: Upload Side Image
            if side_image:
                status_text.write("Uploading side image...")
                results["Side"] = upload_right_side_photo(LOCAL_URL, side_image)
                progress_bar.progress(progress_step)

            # Step 2: Process Spine Analysis
            if "Side" in results:
                status_text.write("Analyzing spine structure...")
                spine_results = get_spine(
                    LOCAL_URL,
                    results["Side"].get('line_points', []),
                    results["Side"].get('feature_points', []),
                    results["Side"].get('keypoints_3d_denormalized', [])
                )
                progress_bar.progress(1.0)  # Complete

        status_text.write("Processing complete ✅")

        return {"spine_results": spine_results, "results": results}