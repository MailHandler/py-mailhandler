import os
import sys

from setuptools import find_packages, setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = find_packages()

setup(
    name='mailhandler',
    version='0.0.3',
    description='Python adapter for MailHandler.ru API',
    long_description='Python adapter for MailHandler.ru API. Includes bindings for transactional '
                     'mailing and tracking features',
    author='MailHandler.ru',
    author_email='hello@mailhandler.ru',
    url='https://mailhandler.ru',
    packages=packages,
    include_package_data=True,
    py_modules=['mailhandler'],
    install_requires=[
        'requests==2.11.1',
    ],
    license='Apache License',
    zip_safe=False,
    keywords='mailhandler email',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
