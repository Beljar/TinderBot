import os
from setuptools import setup, Command

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rmdir /Q /S build')
        os.system('rmdir /Q /S dist')
        os.system('for /d %f in (*egg-info) do rmdir /Q /S %f')

setup(name='TinderBot',
      version='0.1',
      description='bot for tinder: liking, spamming, holding chats',
      author='Beljar',
      author_email='ormallen@gmail.com',
      packages=['TinderBot'],
      install_requires=[
          'selenium',
          'pychrome',
          'requests',
          'bs4',
          "pyfiglet",
      ],
      zip_safe=False,
      cmdclass={
        'clean': CleanCommand,
    })