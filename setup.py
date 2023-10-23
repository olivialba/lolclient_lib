from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

VERSION = '0.0.3'
DESCRIPTION = 'Basic package to send and receive requests from the League of Legends client with added functionalities to make requests easier'

# Setting up
setup(
    name="lolclient-lib",
    version=VERSION,
    author="Albaq (Alberto Olivi)",
    author_email="olivialberto02@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license='MIT',
    url='https://github.com/olivialba',
    install_requires=['requests'],
    keywords=['python', 'league of legends', 'lol', 'client', 'lcu', 'riot'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)