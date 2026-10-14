Name:		python-google-api-core
Version:	2.42.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/google-api-core/google_api_core-%{version}.tar.gz
Summary:	Google API client core library
URL:		https://pypi.org/project/google-api-core/
License:	Apache 2.0
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Google API client core library

%prep -a
# Cooker python-protobuf provides python3.15dist(protobuf) = 6.32.1.
# opentelemetry-api is not packaged. The library imports it only when tracing is enabled.
find . -name pyproject.toml -o -name PKG-INFO -o -name requires.txt | xargs sed -i \
	-e 's/6\.33\.5/6.32.1/g' \
	-e '/opentelemetry-api/d'

%files
%{py_sitedir}/google
%{py_sitedir}/google_api_core-%{version}.dist-info
