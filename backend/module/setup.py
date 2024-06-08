from setuptools import setup

setup(
    name="JihwanTModule",
    version="0.1",
    packages=["backend.module"],
    install_requires=[
        "CtrlJson.py",
        "Encryption.py"
    ],
)
