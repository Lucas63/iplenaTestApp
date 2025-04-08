import streamlit as st

from core.api import upload_front_photo, upload_right_side_photo, upload_sit_photo, get_spine


def render_images_processing(LOCAL_URL, front_image, side_image):
    """Processes images step by step with progress updates and messages."""

    # Create a list to store the analyses to be displayed
    analyses = []

    # Check for side photo and append appropriate analysis
    if side_image:
        analyses.append("Side photo analysis")
        analyses.append("Spine 3D (Side view)")

    # Check for front photo and append appropriate analysis
    if front_image:
        analyses.append("Front photo analysis (in development)")

    # If both front and side photos are present, append Spine 3D Front view analysis
    if front_image and side_image:
        analyses.append("Spine 3D (Front view)")

    # Display the analyses list
    st.subheader("Analysis to be Applied:")

    if len(analyses) > 0:
        for analysis in analyses:
            st.markdown(f"<p style='font-size:30px;'>- {analysis}</p>", unsafe_allow_html=True)

    else:
        st.markdown(f"<p style='font-size:20px; font-weight: bold;'>- Select photos first</p>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("Process Images"):
        results = {}
        progress_bar = st.progress(0)
        status_text = st.empty()  # Placeholder for status updates
        progress_step = 0.33  # Two steps (0.5 per step)
        st.markdown("---")
        with st.spinner("Processing images..."):
            if front_image:
                status_text.write("Uploading front image...")
                results["Front"] = upload_front_photo(LOCAL_URL, front_image)
                progress_bar.progress(progress_step)

            # Step 1: Upload Side Image
            if side_image:
                status_text.write("Uploading side image...")
                results["Side"] = upload_right_side_photo(LOCAL_URL, side_image)
                progress_bar.progress(2 * progress_step)

            # Step 2: Process Spine Analysis
            if "Side" in results:
                status_text.write("Analyzing spine structure...")
                spine_results = get_spine(
                    LOCAL_URL,
                    results.get("Side",{}).get('feature_points', None),
                    results.get("Side",{}).get('keypoints_3d_denormalized', None),
                    results.get("Front",{}).get('keypoints_2d', None)
                )
                progress_bar.progress(1.0)  # Complete

        status_text.write("Processing complete ✅")
        st.markdown("---")
        return {"spine_results": spine_results, "results": results}