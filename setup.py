from setuptools import setup, find_packages

requires = [
    'requests==2.18.4',
    'pyquery==1.2.17'
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
