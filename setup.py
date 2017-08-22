
from distutils.core import setup

setup(
    name='quotify',
    version='0.1',
    packages=['tests', 'quotify'],
    url='',
    license='MIT',
    author='Madhavi Jouhari',
    author_email='',
    description='Quote notifications for Ubuntu',
    entry_points={
        'console_scripts': [
            'quotify=quotify.quote_generator:main',
        ]
    }

)