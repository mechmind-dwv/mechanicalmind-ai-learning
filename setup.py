from setuptools import setup, find_packages

setup(
    name="mechanicalmind-ai-learning",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.0.0",
        "requests>=2.25.0",
    ],
    entry_points={
        'console_scripts': [
            'mechmind=scripts.cli:diagnose',
        ],
    },
)
