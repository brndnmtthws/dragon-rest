import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dragon-rest",
    version="0.1.0",
    author="Brenden Matthews",
    author_email="brenden@diddyinc.com",
    description="Python wrapper for DragonMint T1 REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brndnmtthws/dragon-rest",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
