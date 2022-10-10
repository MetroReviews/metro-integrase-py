import setuptools 

setuptools.setup(
    name="metro_integrase",
    version="0.0.2",
    author="Rootspring",
    author_email="cheesycod@outlook.com",
    description="A Python wrapper for the Metro Reviews API",
    long_description="A Python wrapper for the Metro Reviews API (https://github.com/MetroReviews)",
    include_dirs=["metro_integrase"],
    install_requires=[
        "fastapi",
        "aiohttp",
        "pydantic",
    ]
)