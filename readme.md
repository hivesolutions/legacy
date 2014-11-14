# Legacy support for Python 2/3

Set of tools that provide backward compatibility with Python 2.6+.

## Guide

When creating code that is meant to work both in PYthn 2.6+ and Python 3.1+ one must take into consideration
the following topics:

* Usage of the comparison operators `cmp()` 
* Usage of the iterator based operators: `xrange`, `iteritems`, `iterkeys`, `itervalues`
* Compatibility between the new iterator based operation and the old eager ones for: `range`, `items`, `keys`, `values`
