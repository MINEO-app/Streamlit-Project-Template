import streamlit as st
import json


class MineoAuth:
    @staticmethod
    def get_user():
        """Return authenticated user as dictionary"""
        try:
            headers = st.context.headers
            return {
                "uuid": headers.get("X-User-UUID"),
                "username": headers.get("X-User-Username"),
                "email": headers.get("X-User-Email"),
                "first_name": headers.get("X-User-First-Name"),
                "last_name": headers.get("X-User-Last-Name"),
                "groups": json.loads(headers.get("X-User-Groups"))
                if "X-User-Groups" in headers
                else [],
            }
        except:
            return None

    @staticmethod
    def is_authenticated():
        """Check if there's an authenticated user"""
        user = MineoAuth.get_user()
        return user and user.get("uuid") is not None
