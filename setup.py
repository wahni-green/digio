from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in digio/__init__.py
from digio import __version__ as version

setup(
	name="digio",
	version=version,
	description="Frappe Digio Integration",
	author="Wahni IT Solutions",
	author_email="info@wahni.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
