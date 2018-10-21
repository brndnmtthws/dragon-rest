import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dragon-rest",
    version="0.2.0",
    author="Brenden Matthews",
    author_email="brenden@diddyinc.com",
    description="Python wrapper for DragonMint/Innosilicon REST API",
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
