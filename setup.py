from setuptools import setup

tests_require = [
    'pytest>=3.0.5',
    'pytest-cov>=2.4.0',
    'pytest-flake8>=0.8.1',
    'django>=1.8.0',
]

setup(
    name='django-ranged-fileresponse-filter',
    version='0.0.1',
    description='Modified Django FileResponse that adds Content-Range headers +Bleach.',
    url='https://github.com/dvwright/django-ranged-fileresponse-filter',
    license='MIT',
    packages=['ranged_fileresponse_filter'],
    zip_safe=False,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
)
