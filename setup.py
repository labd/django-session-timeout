from setuptools import find_packages, setup

docs_require = [
    'sphinx>=1.4.0',
]

tests_require = [
    'coverage==.4.2',
    'freezegun==0.3.11',
    'pytest==4.3.1',
    'pytest-django==3.4.8',

    # Linting
    'isort==4.3.15',
    'flake8==3.7.7',
    'flake8-blind-except==0.1.1',
    'flake8-debugger==3.1.0',
]

setup(
    name='django-session-timeout',
    version='0.0.3',
    description="Middleware to expire sessions after specific amount of time",
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/LabD/django-session-timeout',
    author="Lab Digital",
    author_email="opensource@labdigital.nl",
    install_requires=[
        'Django>=1.8',
        'six>=1.1',
    ],
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    use_scm_version=True,
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=False,
)
