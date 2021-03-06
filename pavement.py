#!/usr/bin/env python
import os

from paver import svn
from paver.easy import *
from paver.setuputils import setup, find_package_data, find_packages
import paver.setuputils
import paver.virtual


with file("requirements.txt") as f:
    install_requires = f.read().splitlines()


options(
      virtualenv=Bunch(
            packages_to_install=[],
            install_paver = True,
            paver_command_line=None,
            no_site_packages=True
          ),
      )


setup(
      name='pyfibot',
      version='0.9.4',
      description='Python IRC bot',
      long_description='An event-based IRC bot, based on twisted.words.protocols.irc',
      url='https://github.com/lepinkainen/pyfibot',
      author='Riku Lindblad',
      author_email='riku.lindblad@gmail.com',
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Environment :: Console',
            'Framework :: Twisted',
            'Operating System :: OS Independent',
            'Topic :: Communications :: Chat :: Internet Relay Chat'
            ],
      license='MIT',
      packages=['pyfibot', 'pyfibot.modules', 'pyfibot.util', 'pyfibot.lib'],
      zip_safe=False,
      install_requires=install_requires,
      test_suite='nose.collector',
      entry_points={
            'console_scripts': ['pyfibot = pyfibot:main']
            }
      )


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass


@task
def prepare(options):
    pass


@task
def bootstrap(options):
    """create virtualenv"""
    try:
        import virtualenv
    except ImportError, e:
        raise RuntimeError("virtualenv is needed for bootstrap")

    options.virtualenv.no_site_packages = False
    options.virtualenv.packages_to_install = install_requires
    options.bootstrap.no_site_packages = False
    options.virtualenv.paver_command_line='prepare'
    call_task('paver.virtual.bootstrap')
