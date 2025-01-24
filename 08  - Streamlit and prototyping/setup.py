from setuptools import setup, find_packages

setup(
    name='heart-attack-analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'streamlit',
        'matplotlib',
        'python-dotenv',
        'openai',
        'requests'
    ]
)