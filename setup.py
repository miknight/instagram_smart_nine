import os
from setuptools import setup, find_packages

requires = ['pytz==2020.5',
            'instagram-scraper==1.9.1',
            'numpy==1.19.3',
            'matplotlib==3.3.3',
            'scipy==1.5.4',
            'pandas==1.2.0',
            'opencv-python-headless==4.4.0.46',
            'pytest==6.2.1']

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(name='smart-nine',
      version='0.0.8',
      description=("smart-nine is a command-line application written in Python"
                 " that generates an Instagram user's top nine photograph collage. Use responsibly."),
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ulysseslizarraga/instagram_smart_nine',
      author='Ulysses Lizarraga',
      author_email='ulises.lizarraga@gmail.com',
      license='Public domain',
      packages=find_packages(exclude=['tests']),
      install_requires=requires,
      entry_points={'console_scripts': ['smart-nine=smart_nine.app:main'],},
      zip_safe=False,
      keywords=['instagram', 'top', 'nine', 'smart', 'photos', 'collage', 'year'])