import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__filename__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description="A simple Django application to conduct web-based polls.",
    long_description=README,
    url='https://www.kayra.co.uk/',
    author='Kayra Alat',
    author_email='test@test.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
