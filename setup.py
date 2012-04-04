from setuptools import setup, find_packages
import sys, os

version = '1.0'
shortdesc = 'checks and restarts plone 3 zeo-clients if disconnected'
longdesc = " "
longdesc =  open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()  
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()  
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()  

setup(name='bda.plone.checkclientdisconnected',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: Beta',
            'License :: OSI Approved :: BSD-simplified',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Software Development',
            "Framework :: Plone",
      ],
      keywords='',
      author='Benjamin Stefaner',
      author_email='bs@kleinundpartner.at',
      url=u'http://github.com/collective/bda.plone.checkclientdisconnected',
      license='BSD-simplified',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=["bda", "bda.plone"],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'setuptools',   
      ],

      entry_points={
      'console_scripts': ['checksingleclient = bda.plone.checkclientdisconnected.checksingleclientscript:run', 
                          'checkmulticlient = bda.plone.checkclientdisconnected.checkmulticlientscript:run'],
      },
)
