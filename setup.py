from setuptools import setup, find_packages

setup(
    name='haversine_geo_distance_module',
    version='0.1.0',
    description='A Python module to calculate the distance between two points on the Earth\'s surface.',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/earth_distance',
    packages=find_packages(),
    install_requires=['haversine'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)