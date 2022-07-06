from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="TUCchkul",
    description="A small package for dvc DL pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TUCchkul/Data_Version_Control_Deep_Learning_With_Tensorflow",
    author_email="kirticse.chakma869@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        
        'tensorflow',
        'matplotlib',
        'numpy',
        'pandas',
        'tqdm',
        'PyYAML'
    ]
)