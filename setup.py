try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup (name = "gprof2dot",
        version = "1.0",
        py_modules = ['gprof2dot'],
        packages = ['gprof2dot'],
        scripts = ['gprof2dot/bin/gprof2dot',\
        'gprof2dot/bin/hotshot'],
        use_2to3=True
      )
