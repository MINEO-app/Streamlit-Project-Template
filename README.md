# Project Title

A brief description of your MINEO Streamlit project, including its purpose and main objectives.

## Project Structure

```
project-name/
├── src/               # Python source code modules
├── app.py             # Main entrypoint of the Streamlit application
├── assets/            # Images, data files, and other static resources
├── docker/
│   │── Dockerfile    # Dockerfile for local development (can also build MINEO Worker Images)
│   │── requirements.txt   # Python dependencies
└── docker-compose.yml # Docker Compose configuration for local development
```

## Requirements

- Python 3.12 or higher
- Dependencies listed in `requirements.txt`

## Quick Start

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd project-name
   ```

2. Install dependencies:
   ```bash
   # Using pip
   pip install -r docker/requirements.txt
   
   # Alternative using uv (if available)
   uv pip install -r docker/requirements.txt
   ```

3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

4. Main application modules are located in the `src/` directory.

## Docker Support

### Local Development with Docker Compose

Build and run the application with Docker:

```bash
docker compose build
docker compose up -d
```

To run an interactive shell in your container:

```bash
docker compose exec st-project bash
```

**Note:** You may change the `st-project` service name to match your project name in `docker-compose.yml`.

### Building for MINEO Platform

The Dockerfile in the `docker/` directory can be used to build images compatible with the MINEO platform. Refer to MINEO documentation for specific deployment instructions.

---

**This is a template repository for Streamlit projects designed for development in both local environments and the MINEO platform. Modify this README to fit your specific project needs.**

---
