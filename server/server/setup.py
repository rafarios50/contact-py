from setuptools import find_packages, setup

setup(
    name="contacts",
    version="0.0.1",
    install_requires=[
        "Django==4.0.0",
        "djangorestframework==3.12.4",
        "django-cors-headers==3.10.1",
		"pytz"
    ],
    description="Django project",
    url="https://github.com/jala-dev/contact-py",
    package_dir={"": "."},
    packages=find_packages(where="."),
    python_requires=">=3.9",
    scripts=["manage.py"],
)