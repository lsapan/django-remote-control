from distutils.core import setup

setup(
    name = 'django-remote-control',
    packages = ['remote_control'],
    version = '1.0.1',
    install_requires=[
        'requests',
    ],
    description = 'Securely call commands in other django applications.',
    author = 'Luke Sapan',
    author_email = 'lukevsapan@gmail.com',
    url = 'https://github.com/lsapan/django-remote-control',
    download_url = 'https://github.com/lsapan/django-remote-control/archive/1.0.1.tar.gz',
    keywords = ['django', 'remote' 'commands', 'rpc'],
    classifiers = [],
)
