from setuptools import setup, find_packages

requires = [
    'beautifulsoup4==4.6.0',
    'simple_table'
]

setup(
    name='douban_rating',
    version='0.0.1',
    description='Get douban rating in terminal.',
    url='https://github.com/Frederick-S/douban-rating',
    packages=find_packages(exclude=['tests']),
    install_requires=requires,
    test_suite="tests"
)
