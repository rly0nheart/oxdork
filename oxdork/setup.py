import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="oxdork",
    version="2021.2.1.0",
    author="Richard Mwewa",
    author_email="richardmwewa@duck.com",
    packages=["oxdork"],
    description="Google dorking tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlyonheart/oxdork",
    license="MIT License",
    install_requires=["google==3.0.0"],
    classifiers=[
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        "console_scripts": [
            "oxdork=oxdork.__main__:dork",
        ]
    },
)
