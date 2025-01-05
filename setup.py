from setuptools import setup, find_packages

setup(
    name='TimurkaaaaProgressBar',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Timurkaaa',
    author_email='timurzarovskiy@gmail.com',
    description='a simple tool for displaying task progress in Python console applications. It allows users to see how far the process has progressed, making your code more interactive and usable.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Timurkaaaaaaa/ProgressBar/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)