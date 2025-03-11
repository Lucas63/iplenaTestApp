import streamlit as st

def render_image_loading(col1,col2,col3):
    # with col1:
    #     front_image = st.file_uploader("Upload Front Image", type=["jpg", "jpeg", "png"], key="front")

    with col1:
        side_image = st.file_uploader("Upload Side Image", type=["jpg", "jpeg", "png"], key="side")

    # with col3:
    #     back_image = st.file_uploader("Upload Back Image", type=["jpg", "jpeg", "png"], key="back")

    # with col1:
    #     if front_image is not None:
    #         st.image(front_image, caption="Uploaded Front Image", use_container_width=True)

    # Side Image Section
    with col2:
        if side_image is not None:
            st.image(side_image, caption="Uploaded Side Image", use_container_width=True)

    # Back Image Section
    # with col3:
    #     if back_image is not None:
    #         st.image(back_image, caption="Uploaded Back Image", use_container_width=True)
    return side_image
    # return front_image, side_image, back_image