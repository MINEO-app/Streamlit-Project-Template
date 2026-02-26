"""
MINEO Streamlit Application Template
A basic example showing how to structure a MINEO-compatible Streamlit app.
"""

import streamlit as st

# Import from src directory
from src.example_module import say_hello, get_mineo_info
from src.utils import format_text
from src.auth_helper import MineoAuth

# App configuration
st.set_page_config(page_title="MINEO Template App", page_icon="🚀", layout="wide")


# Main app
def main():
    # Header
    user = MineoAuth.get_user()

    if MineoAuth.is_authenticated():
        st.success(f"✅ Authenticated as: {user['email']}")

        # Protected content
        st.write("## Exclusive content for authenticated users")
        st.write(f"Welcome to your personal area, {user['first_name']}!")
    st.title("🚀 Welcome to MINEO")
    st.markdown("This is a basic template for MINEO Streamlit applications.")

    # Sidebar
    with st.sidebar:
        st.header("MINEO Platform")
        st.info("This app demonstrates a basic structure for MINEO projects.")

        # User input
        user_name = st.text_input("Your name:", value="MINEO User")

        # Options
        show_info = st.checkbox("Show MINEO info", value=True)
        use_feature = st.checkbox("Use advanced feature", value=False)

    # Main content area
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Greeting")
        greeting = say_hello(user_name)
        formatted_greeting = format_text(greeting, "bold")
        st.markdown(formatted_greeting)

        if use_feature:
            st.success("✨ Advanced feature is enabled!")

    with col2:
        st.subheader("Platform Information")
        if show_info:
            mineo_info = get_mineo_info()
            st.write(mineo_info)
            st.image(
                "https://via.placeholder.com/400x200/4A6FA5/FFFFFF?text=MINEO+Platform",
                caption="MINEO Analytics Environment",
                width="stretch",
            )

    # Demo section
    with st.expander("📊 Quick Demo"):
        st.write("This is a collapsible section for demonstrations.")
        demo_data = {
            "Metric": ["Users", "Sessions", "Data Points"],
            "Value": [150, 1200, 45000],
        }
        st.table(demo_data)

    # Footer
    st.divider()
    st.caption("Built for MINEO Platform | Template v1.0")


if __name__ == "__main__":
    main()
