from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("woah/__version__.py") as f:
    version = f.read().split()[-1].strip('"')

setup(
    name="woah",
    version=version,
    description="Wait for reasonable load average",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tim Hatch",
    author_email="tim@timhatch.com",
    url="https://github.com/thatch/woah",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
    license="Apache 2.0",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={"console_scripts": ["woah = woah.cmdline:main"]},
)
