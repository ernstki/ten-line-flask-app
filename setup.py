"""
setuptools setup.py for the ten line Flask app

Ref. https://setuptools.readthedocs.io/en/latest/setuptools.html

"""
from setuptools import setup

setup(
    name='TenLineApp',
    version='0.1',
    author="Kevin Ernst",
    author_email='ernstki -at- mail.uc.edu',
    url='https://github.com/ernstki/ten-line-flask-app',
    packages=['tenline'],
    include_package_data=True,
    scripts=['manage.py'],
    entry_points={
        'console_scripts': [ 'tenline = manage:__main__' ]
    }
)