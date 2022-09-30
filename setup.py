from importlib.metadata import entry_points
from setuptools import setup
import os

def get_readme():
    """returns the contents of the README file"""
    return open(os.path.join(os.path.dirname(__file__), "README.md")).read()

setup(
   name="manti_go",                       # snake is already taken on PyPi
   version="0.1",                          # uses *semantic versioning*
   description="a terminal-based collect game",   
   long_description=get_readme(),
   author="naive_bayleaves",
   author_email="vrupp@rupali.de",
   packages=["mantigo"],                 # the name of the folder with .py modules
   url="https://github.com/JoNiederhut/manti_go",
   license="MIT",
   classifiers=[
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10"
   ],
   entry_points={
        "console_scripts":["mantigo=mantigo.prototype:main"]
   }
)
    
