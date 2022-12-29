#!/usr/bin/python3
#-------------------------------------------------------------
#Setup script for MTDA-FastAPI
#-------------------------------------------------------------
from setuptools import setup, find_packages
  
setup(
        name='mtda_fastapi',
        packages=find_packages(),
        version='1.0.0',
        scripts=['mtda-fastapi-cli'],
        description='Multi-Tenant Devices Access-FASTAPI',
        url='https://github.com/anushayadav01/mtda__fastapi',
        classifiers=[
            "Topic :: Utilities",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.0",
            "Topic :: Software Development :: Embedded Systems",
            ],

        install_requires=[
            "python-daemon>=2.0",
            "fastapi_websocket_rpc",
            "fastapi>=0.78.0,<1",
            "pydantic>=1.9.1,<2",
            "uvicorn>=0.17.6,<1",
            "websockets>=10.3,<11",
            "tenacity>=8.0.1,<9",
            "asyncinit",
            "pyzmq>=15.0,<23.0.0"
            ],
 )
        
