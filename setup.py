from distutils.core import setup, Extension

module_name = 'c_module'
c_files = ['./Utils/c_module.c']

extension = Extension(
    module_name,
    c_files
)

setup(
    name=module_name,
    version='1.0',
    description='The package description',
    author='Nicholas Obert',
    author_email='nchlsuba@gmail.com',
    url='https://my.web.site/some_page',
    ext_modules=[extension]
)