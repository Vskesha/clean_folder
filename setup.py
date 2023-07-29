from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Sorts files in proper folder',
    url='https://github.com/Vskesha/clean_folder.git',
    author='Vasyl Boliukh',
    author_email='vskesha@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean_folder']}
)
