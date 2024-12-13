from setuptools import setup, find_packages

setup(
    name="flaskPillow",
    version="1.0.0",
    description="Pillow review website.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "python-dotenv",
        "gunicorn",
        "click",
        "blinker",
        "coverage",
        "Cython",
        "itsdangerous",
        "Jinja2",
        "MarkupSafe",
        "packaging",
        "pluggy",
        "pyproject_hooks",
        "pytest",
        "PyYAML",
    ],
)