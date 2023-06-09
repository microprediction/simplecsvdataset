import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="simplecsvdataset",
    version="0.0.1",
    description="Torch dataset construction from CSV collections",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/simplecsvdataset",
    author="microprediction",
    author_email="peter.cotton@microprediction.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["simplecsvdataset"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=['numpy','torch','pandas'],
    entry_points={
        "console_scripts": [
            "simplecsvdataset=simplecsvdataset.__main__:main",
        ]
    },
)