"""
Utility functions for the MINEO template app.
"""

def format_text(text: str, style: str = "normal") -> str:
    """Format text based on style."""
    styles = {
        "bold": f"**{text}**",
        "italic": f"*{text}*",
        "header": f"### {text}",
        "info": f"ℹ️ {text}"
    }
    return styles.get(style, text)

def check_environment() -> str:
    """Check and return current environment."""
    import os
    env = os.getenv("MINEO_ENVIRONMENT", "local")
    return f"Running in: {env.upper()} environment"
