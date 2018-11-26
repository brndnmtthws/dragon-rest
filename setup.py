import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'requests>=2.20.1',
]

test_requires = [
    'pytest-cov',
    'vcrpy>=1.12.0',
    'pytest>=3.6.1',
]

setuptools.setup(
    name="dragon-rest",
    version="0.2.3",
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
    python_requires=">=3.5",
    install_requires=requires,
    tests_require=test_requires,
    extras_require={
        'test': test_requires,
    },
)
