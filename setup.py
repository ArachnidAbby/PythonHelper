import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonHelper-tools-spidertyler2005",
    version="0.0.1",
    author="spidertyler2005",
    author_email="spidertyler1122@gmail.com",
    description="A small package that just adds a few useful but common code bits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/spidertyler2005/PythonHelper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)