import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JsonConverter", # Replace with your own username
    version="0.0.1",
    author="prgarre",
    author_email="garrepradeepkumar.com",
    description="Json converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gp2kumar/jsonconverter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)