import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="performance_tuner",
    version="0.1",
    description="A set of tools to performance tune your models",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/EricSchles/performance_tuner",
    author="Eric Schles",
    author_email="ericschles@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["performance_tuner", "performance_tuner.precision_recall_tuner"],
    include_package_data=True,
    install_requires=["sklearn", "scipy", "numpy", "statsmodels", "pytest", "mlxtend", "describer_ml"],
)
