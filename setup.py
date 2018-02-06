"""
setuptools setup.py for the ten line Flask app

Ref. https://setuptools.readthedocs.io/en/latest/setuptools.html

"""
import os
from setuptools import setup

reqfile = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(reqfile, 'r') as f:
    requires = f.readlines()

setup(
    name='tenlineapp',
    version='0.1',
    author="Kevin Ernst",
    author_email='ernstki -at- mail.uc.edu',
    url='https://github.com/ernstki/ten-line-flask-app',
    packages=['tenlineapp'],
    include_package_data=True,
    # Didn't work on my Windows box
    #entry_points={
    #    'console_scripts': [ 'tenline = manage:run_server' ]
    #},
    install_requires=requires,
)