Name:		python-google-api-core
Version:	2.24.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/g/google-api-core/google_api_core-%{version}.tar.gz
Summary:	Google API client core library
URL:		https://pypi.org/project/google-api-core/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Google API client core library

%files
%{py_sitedir}/google
%{py_sitedir}/google_api_core-*.*-info
