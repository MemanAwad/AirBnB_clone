#!/usr/bin/python3
"""Defines unittests for console.py"""
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand

class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter"""
    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help commsnd of HBNB command interpreter"""



if __name__ == '__main__':
    unittest.main()
