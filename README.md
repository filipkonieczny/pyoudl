pyoudl
======


Table of Contents
-----------------
- [About](https://github.com/filipkonieczny/pyoudl#about),
- [Prerequisites](https://github.com/filipkonieczny/pyoudl#prerequisites),
- [Setup](https://github.com/filipkonieczny/pyoudl#setup),
- [Troubleshooting](https://github.com/filipkonieczny/pyoudl#troubleshooting)


About
-----
Pyoudl(pronounced *pjuːdəl*) is a small script that enables you to download music from [YouTube](https://www.youtube.com/) via [youtube-mp3.org](http://www.youtube-mp3.org/).


Prerequisites
-------------
- [```Python``` 2.7+](https://www.python.org/download/releases/2.7/),
- [```virtualenv```](http://virtualenv.readthedocs.org/en/latest/),
- [```pip```](https://pypi.python.org/pypi/pip),
- [```dryscrape```'s prerequisites](http://dryscrape.readthedocs.org/en/latest/installation.html#prerequisites)


Setup
-----
```
git clone git@github.com:filipkonieczny/pyoudl.git
cd pyoudl
virtualenv .venv
source .venv/bin/activate
pip install -r requirements
```


Troubleshooting
---------------

[```Dryscrape```](https://github.com/niklasb/dryscrape) may require manual installation due to external requirements. Please use the [docs](http://dryscrape.readthedocs.org/en/latest/installation.html) for any refference.
