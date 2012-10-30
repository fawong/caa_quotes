from setuptools import setup

setup(name='caa-quotes',
      description="The Django project that powers the web interface to view the quotes collected by the #CAA quotes bot",
      author="Kenny Do",
      author_email="kedo@ocf.berkeley.edu",
      packages=['caaquotes',
                'caaquotes.quotes'],
      install_requires=['Django',
                        'stemming'],
      data_files=[],
      version='1.0.0',
      long_description="""
The Django project that powers the web interface to view the quotes collected by the quotes bot on #CAA, the IRC channel of Cal Animage Alpha, UC Berkeley's anime club
                       """,
      url='http://www.calanimagealpha.com',
      classifiers=['Programming Language :: Python'],
      )
