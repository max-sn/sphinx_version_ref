# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

long_desc = open('README.rst').read()

requires = [
    'Sphinx>=1.3',
    'setuptools>=20.7'
]
project_urls = {
    'Documentation': 'http://sphinx-version-ref.readthedocs.io/',
    'Repository': 'https://github.com/max-sn/sphinx_version_ref/',
    'Issue tracker': 'https://github.com/max-sn/sphinx_version_ref/issues',
}

setup(
    name='sphinx-version-ref',
    url=project_urls['Documentation'],
    project_urls=project_urls,
    license='MIT',
    author='M.J.W. Snippe',
    author_email='maxsnippe@gmail.com',
    description='Sphinx extension to substitute version in references.',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities'
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    use_scm_version=True,
    setup_requires=['setuptools_scm'])
