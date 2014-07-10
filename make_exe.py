from distutils.core import setup
import py2exe

setup(
    console = [
        {
            "script": "POD.py",                    ### Main Python script    
            "icon_resources": [(0, "POD.ico")]     ### Icon to embed into the PE file.
        }
    ],
) 
