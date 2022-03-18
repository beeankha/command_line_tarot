from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

# read the contents of description file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "PYPI_DESC.md").read_text()


setup(
        name ='cli-tarot',
        version ='0.0.8',
        author ='Bianca Henderson',
        author_email ='beeankha@gmail.com',
        url ='https://github.com/beeankha/command_line_tarot',
        description ='A command line tarot reader.',
        long_description = long_description,
        long_description_content_type ='text/markdown',
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'cli-tarot=cli_tarot.__main__:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3.9",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='tarot cli beeankha',
        install_requires = requirements,
        zip_safe = False,
)
