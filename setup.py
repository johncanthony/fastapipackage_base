from setuptools import setup, find_packages

setup(
    name='base_fast_api_package',
    version='0.1.0',
    description='Baseline Package for Fast API project',
    author='John Anthony',
    packages=find_packages(exclude=('test', '.venv')),
    install_requires=['fastapi', 'uvicorn', 'pytest', 'httpx', 'redis'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6'
)
