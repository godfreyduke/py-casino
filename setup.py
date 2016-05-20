from setuptools import setup

setup(
    name="pycasino",
    version="0.0.1",
    author=["Allen Mohemani", "Mike Herold"],
    author_email="",
    description="A Casino framework.",
    license="",
    keywords=["casino", "poker", "games", "framework"],
    url="https://github.com/codeNameMahi/py-casino/",
    packages=['pycasino', 'games', 'pycasino.framework'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 2.7",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Arcade",
        "Topic :: Games/Entertainment :: Turn Based Strategy",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    entry_points = {
        'console_scripts': [
            'vpoker = games.videopoker:run',
        ],
    }
)
