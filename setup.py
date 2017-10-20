from setuptools import setup, find_packages

setup(
    name='douban_rating',
    version='0.0.1',
    description='Get douban rating in terminal.',
    url='https://github.com/Frederick-S/douban-rating',
    packages=find_packages(exclude=['tests']),
    test_suite="tests"
)
