from setuptools import setup, find_packages

setup(
    name='VickClass',
    version='0.0.1',
    description='A simple class utility package',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/imvickykumar999/PyPI-API',
    author='Vicky Kumar',
    author_email='imvickykumar999@gmail.com',
    license='MIT',
    packages=find_packages(include=['vicksclass']),
    keywords=['class', 'python', 'utility'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)
