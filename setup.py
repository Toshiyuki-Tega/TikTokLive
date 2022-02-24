import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TikTokLive",
    packages=setuptools.find_packages(),
    version="1.0.0",
    license="MIT",
    description="Unofficial TikTok Live Client",
    author="Isaac Kogan",
    author_email="info@isaackogan.com",
    url="https://github.com/isaackogan/TikTok-Live-Connector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/davidteather/TikTok-Api/tarball/master",
    keywords=["tiktok", "tiktok live", "python3", "api", "unofficial"],
    install_requires=["aiohttp", "protobuf3-to-dict", "protobuf", "pyee"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)
