"""
Created on Aug 20, 2019

@author: flba
"""
import os
from resources.data import BROWSER

# Here we will declare environment variables that can come from outside the tests (i.e. gitlab/jenkins)
BROWSER = os.getenv("BROWSER", BROWSER)
