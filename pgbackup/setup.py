from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backup locally or to AWS S3.',
    long_description=readme,
    author='jgyy',
    author_email='jgyy@email.com',
    packages=find_packages('pgbackup'),
    package_dir={'': 'pgbackup'},
    install_requires=[]
)
