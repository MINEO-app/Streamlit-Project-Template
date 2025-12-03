#!/bin/bash
set -eux

uv pip install --system -r requirements.txt
streamlit run app.py
