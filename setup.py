import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eyefootball",
    version="0.0.1",
    author="slvler",
    author_email="slvler@proton.me",
    description="Link adapter for eyefootball.com rss service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slvler/eyefootball",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9.6',
    install_requires=["feedparser>=6.0.0", "future>=0.18.3", "pywebview>=4.0.1"]
)