from setuptools import setup, find_packages
version = '0.1'

setup(name='psusymp.traversingdjango',
      version=version,
      description="plone/django integration example",
      long_description="",
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Nathan Van Gheem',
      author_email='vangheem@gmail.com',
      url='',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['psusymp'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Django'
      ]
)
