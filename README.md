# Legacy support for Python 2/3

Set of tools that provide backward compatibility with Python 2.6+.

## Guide

When creating code that is meant to work both in PYthn 2.6+ and Python 3.1+ one must take into consideration
the following topics:

* Usage of the comparison operators `cmp()`
* Usage of the iterator based operators: `xrange`, `iteritems`, `iterkeys`, `itervalues`
* Compatibility between the new iterator based operation and the old eager ones for: `range`, `items`, `keys`, `values`
* Hash related functions must receive byte based strings: `hashlib.update`, `hashlib.md5`, etc
* Base64 encoding/decoding requires byte strings: `base64.b64encode`, `base64.b64decode` (only Python 3.2-)

## References

* [Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html)

## License

Legacy is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://travis-ci.org/hivesolutions/legacy.svg?branch=master)](https://travis-ci.org/hivesolutions/legacy)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/legacy/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/legacy?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/legacy.svg)](https://pypi.python.org/pypi/legacy)
[![License](http://img.shields.io/badge/license-Apache%202.0-blue.svg)](http://www.apache.org/licenses/)
