"""
SaltFluxDecomposition: NumPy-based salt flux decomposition.

Author: Gijs G. Hendrickx
"""
from setuptools import setup

with open('README.md', mode='r') as f:
    long_description = f.read()

setup(
    name='SaltFluxDecomposition',
    version='1.0',
    author='Gijs G. Hendrickx',
    author_email='G.G.Hendrickx@tudelft.nl',
    description='NumPy-based salt flux decomposition',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['src', 'tests'],
    license='Apache-2.0',
    keywords=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    install_requires=['numpy'],
    python_requires='>=3.7'
)
