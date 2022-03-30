#!/usr/bin/env python3

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().split("\n")

with open("requirements_dev.txt") as requirements_dev_file:
    dev_requirements = requirements_dev_file.read().split("\n")

test_requirements = ["pytest==5.4.1"]

setup(
    author="Dalwar Hossain",
    author_email="dalwar23@pm.me",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
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
    setup_requires=[],
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/dalwar23/labelx",
    version="2.3.1",
    extras_require={
        "dev": test_requirements + dev_requirements,
    },
    zip_safe=False,
)
