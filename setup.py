from setuptools import find_packages, setup

setup(
    name='pyjo',
    version='0.1.0',

    description='A small utility to create JSON objects',

    url='https://github.com/abawchen/pyjo',

    author='Abaw Chen',
    author_email='abaw.chen@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    keywords='python json jo pyjo',

    packages=find_packages(exclude=['tests']),

    install_requires=[],
    entry_points='''
        [console_scripts]
        pyjo=pyjo.cli:cli
    ''',
    python_requires='>=3.6',
    zip_safe=True,
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest>=5.2.0',
    ],
    test_suite="tests",

)
