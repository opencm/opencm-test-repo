from setuptools import setup


setup(
    name='cloudify-release-tool',
    version='0.1.0',
    url='https://github.com/cloudify-cosmo/cloudify-build-system',
    author='Gigaspaces',
    author_email='cosmo-admin@gigaspaces.com',
    license='LICENSE',
    platforms='All',
    description='Cloudify Release Tool',
    packages=['crt'],
    entry_points={
        'console_scripts': [
            'crt = crt.crt:main',
        ]
    },
    install_requires=[
        'click==6.2',
        'pyyaml==3.10',
        'repex==0.4.0',
        'python-vagrant==0.5.8',
        'fabric==1.10.1',
        'gitpython==0.3.6',
        'boto==2.36.0',
        'requests==2.7.0',
        'sh==1.11'
    ],
)
