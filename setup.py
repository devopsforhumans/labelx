#!/usr/bin/env python3

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click >= 8.04", "requests >= 2.27.1", "colorama >= 0.4.4", "pyyaml >= 6.0.0"]

setup_requirements = []

test_requirements = ["pytest==5.4.1"]

setup(
    author="Dalwar Hossain",
    author_email="dalwar23@pm.me",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Label Creator for GitLab Projects.",
    entry_points={"console_scripts": ["labelx=labelx.app:mission_control"]},
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="labelx",
    name="labelx",
    packages=find_packages(include=["labelx", "labelx.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/dalwar23/labelxg",
    version="2.2.1",
    zip_safe=False,
)
