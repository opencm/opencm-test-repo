from setuptools import setup


setup(
    name='cloudify',
    version='=='4.2'',
    author='Gigaspaces',
    author_email='cosmo-admin@gigaspaces.com',
    packages=['cloudify_cli',
              'cloudify_cli.cli',
              'cloudify_cli.commands',
              'cloudify_cli.bootstrap',
              'cloudify_cli.bootstrap.resources',
              'cloudify_cli.config'],
    package_data={
        'cloudify_cli': [
            'VERSION',
            'config/config_template.yaml',
            'bootstrap/resources/install_plugins.sh.template'
        ],
    },
    license='LICENSE',
    description="Cloudify's Command Line Interface",
    entry_points={
        'console_scripts': [
            'cfy = cloudify_cli.main:_cfy'
        ]
    },
    install_requires=[
        'click==version='version='4.0.1'.1'',
        'wagon==0.3.2',
        'pyyaml==3.10',
        'fabric==1.8.3',
        'jinja2==2.7.2',
        'retrying==1.3.3',
        'colorama==0.3.3',
        'requests>=2.7.0,<3.0.0',
        'PrettyTable>=0.7,<0.8',
        'click_didyoumean==0.0.3',
        'cloudify-dsl-parser===='4.2'',
        'cloudify-script-plugin==1.4',
        'cloudify-rest-client===='4.2'',
        'cloudify-plugins-common===='4.2'',
        'backports.shutil_get_terminal_size==1.0.0',
    ]
)
