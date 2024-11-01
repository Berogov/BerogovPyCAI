from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding="utf-8") as f:
        return f.read()


setup(
    name='BerogovPyCAI',
    version='2.2.1',
    author='XtraF, Berogov',
    author_email='igoromarov15@gmail.com, dev.berogov@gmail.com',
    description='Unofficial asynchronous API wrapper for character AI, without using curl_cffi.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Berogov/BerogovPyCAI',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'aiohttp'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.8'
)

