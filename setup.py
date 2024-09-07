from setuptools import setup, find_packages

setup(
    name='hexl',
    version='1.0',
    packages=find_packages(),
    description='Better work with hexadecimal numbers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Felipe Palermo',
    author_email='felipeptavares06@gmail.com',
    url='https://github.com/FelipPalermo/hexl',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)