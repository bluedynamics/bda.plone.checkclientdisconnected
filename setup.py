from setuptools import setup, find_packages
import sys, os

version = '1.0'
shortdesc = 'bda.plone.checkclientdisconnected'
longdesc = ""
#longdesc =  open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()  
#longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()  
#longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()  

setup(name='bda.plone.checkclientdisconnected,
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: Alpha/Unstable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Software Development',
            "Framework :: Plone",
      ],
      keywords='',
      author='Benjamin Stefaner',
      author_email='bs@kleinundpartner.at',
      url=u'http://github.com/collective/bda.plone.checkclientdisconnected',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=["bda", "bda.plone"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'setuptools',   
      ],

      entry_points="""
      """,
)
