from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='annotate-variants',
    entry_points={
        "console_scripts": ['annotate-variants = annotate_variants.main:main']
    },
    version='1.0',
    description='A command-line utility for obtaining variant information and storing it in a TSV file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dylrei/tc-variant-annotation/',
    author='Dylan Reinhardt',
    author_email='d@dylrei.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    project_urls={
        'Bug Reports': 'https://github.com/dylrei/tc-variant-annotation/issues',
        'Source': 'https://github.com/dylrei/tc-variant-annotation/',
    },
)