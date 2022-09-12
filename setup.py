import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zitadel-python",
    version="0.1.0",
    author="fatelei",
    author_email="fatelei@gmail.com",
    description="zitadel python sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fatelei/zitadel-python",
    project_urls={
        "Bug Tracker": "https://github.com/fatelei/zitadel-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    package_data={
        "": ["*.html"]
    }
)
