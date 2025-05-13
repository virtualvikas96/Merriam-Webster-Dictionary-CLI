from setuptools import setup, find_packages

setup(
    name="mwcli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests", "python-dotenv"],
    entry_points={
        'console_scripts': [
            'mwcli=mwcli.cli:main'
        ]
    }
)

