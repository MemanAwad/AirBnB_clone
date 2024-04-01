#!usr/bin/python3
"""Module for the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User to manage users' information"""

    def __init__(self, *args, **kwargs):
        """Initialize User"""
        super().__init__(*args, **kwargs)
        email = ""
        password = ""
        first_name = ""
        last_name = ""
