from setuptools import find_packages, setup


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="shapesqr",
    version="0.0.1",
    author="DmitriyReztsov",
    author_email="rezcov_d@mail.ru",
    description="This is the test task module for shapes square calculation.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="your_url",  # TODO add
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="circle triangle square calculation",
    project_urls={"GitHub": "https://github.com/DmitriyReztsov"},
    python_requires=">=3.10",
)
