from setuptools import setup, find_packages

setup(
    name='portscanner',
    version='1.0.0',
    description='This is a port scanner which has multi-threaded scan using concurrent.futures',
    author='Bhavani E',
    author_email='itzhinatanaruto1018@gmail.com',
    url='',
    packages=find_packages(),
    install_requires=[
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'portscanner=modules.core:main'
        ]
    },
    python_requires='>=3.6',
)