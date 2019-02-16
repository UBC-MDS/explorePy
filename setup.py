from distutils.core import setup

setup(
    name='explorePy',
    version='0.1',
    packages=['explorePy',],
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
      author = ['James Pushor', 'Rachel K. Riggs', 'Milos Milic', 'Arzan Irani'],
    install_requires=[
        "numpy",
        "pandas",
        "pytest",
        
    ]
)
