from setuptools import setup

setup(
    name="player",
    version=4.0,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="Myattempt at making command-line music player.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/player",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["cli_app_list"],
    install_requires=[
        "mysql.connector",
        "colr",
        "questionary",
        "click",
    ],
    include_package_data=True,
)
