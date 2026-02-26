"""
Example module for MINEO Streamlit template.
"""


def say_hello(name: str) -> str:
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to the MINEO platform."


def get_mineo_info() -> str:
    """Return information about MINEO platform."""
    return """
    **MINEO Platform Features:**
    - 🚀 Streamlit app hosting
    - 📊 Interactive dashboards
    - 🔬 Data science notebooks
    - 📈 Advanced analytics
    - 🔐 Secure deployment
    """


def calculate_something(value: float) -> float:
    """Example calculation function."""
    return value * 2.5
