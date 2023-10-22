from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Basic package to send and receive requests to the League of Legends client'

# Setting up
setup(
    name="lolclient-lib",
    version=VERSION,
    author="Albaq (Alberto Olivi)",
    author_email="<olivialberto02@gmail.com>",
    description=DESCRIPTION,
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