from setuptools import setup

modules = ['threadpoolctl']
setup_kwargs = {
    'name': 'threadpoolctl',
    'version': '3.1.0',
    'description': 'Thread-pool Controls',
    'author': 'Thomas Moreau',
    'author_email': 'thomas.moreau.2010@gmail.com',
    'url': 'https://github.com/joblib/threadpoolctl',
    'py_modules': modules,
}

setup(**setup_kwargs)
