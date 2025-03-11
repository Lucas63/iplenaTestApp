import streamlit as st
def init_app():
    st.set_page_config(layout="wide")
    st.title("Photos testing")
    st.markdown("""
        <style>
        textarea {
            width: 100%;
            min-height: 100px;
            max-height: 400px;
            transition: height 0.2s ease;
            overflow-y: hidden; /* Hide the vertical scrollbar */
        }
        </style>
        <script>
        const textArea = document.querySelector('textarea');
        textArea.addEventListener('input', function () {
            // Reset the height to 'auto' to shrink as needed
            this.style.height = 'auto';
            // Set the height to scrollHeight (the height needed to display the text)
            this.style.height = (this.scrollHeight) + 'px';
        });
        </script>
    """, unsafe_allow_html=True)