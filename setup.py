from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="Robin Norwood",
    author_email='robin@acloud.guru',
    description='Snapshotalyze 30000 is a tool to manage AWS EC2 snapshots',
    licence='GPLv3+',
    packages=['shotty'],
    url="https://github.com/stevemc226/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    ''',

)
