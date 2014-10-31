#!/usr/bin/python
# -*- coding: utf-8 -*-

import imp
import sys
import functools

import urllib #@UnusedImport

root = sys.path.pop(0)
try: import urllib2
except ImportError: urllib2 = None
finally: sys.path.insert(0, root)

root = sys.path.pop(0)
try: import urllib.error
except ImportError: urllib.error = None
finally: sys.path.insert(0, root)

root = sys.path.pop(0)
try: import urllib.request
except ImportError: urllib.request = None
finally: sys.path.insert(0, root)

try: import cStringIO
except ImportError: import io; cStringIO = io

try: import StringIO as _StringIO
except ImportError: import io; _StringIO = io

try: import urlparse as _urlparse
except ImportError: import urllib.parse; _urlparse = urllib.parse

PYTHON_3 = sys.version_info[0] >= 3
""" Global variable that defines if the current python
interpreter is at least python 3 compliant, this is used
to take some of the conversion decision for runtime """

if PYTHON_3: LONG = int
else: LONG = long #@UndefinedVariable

if PYTHON_3: BYTES = bytes
else: BYTES = str #@UndefinedVariable

if PYTHON_3: UNICODE = str
else: UNICODE = unicode #@UndefinedVariable

if PYTHON_3: OLD_UNICODE = None
else: OLD_UNICODE = unicode #@UndefinedVariable

if PYTHON_3: STRINGS = (str,)
else: STRINGS = (str, unicode) #@UndefinedVariable

if PYTHON_3: INTEGERS = (int,)
else: INTEGERS = (int, long) #@UndefinedVariable

# saves a series of global symbols that are going to be
# used latter for some of the legacy operations
_ord = ord
_chr = chr
_str = str
_bytes = bytes

if PYTHON_3: Request = urllib.request.Request
else: Request = urllib2.Request

if PYTHON_3: HTTPHandler = urllib.request.HTTPHandler
else: HTTPHandler = urllib2.HTTPHandler

if PYTHON_3: HTTPError = urllib.error.HTTPError
else: HTTPError = urllib2.HTTPError

try: _reduce = reduce #@UndefinedVariable
except: _reduce = None

try: _reload = reload #@UndefinedVariable
except: _reload = None

def with_meta(meta, *bases):
    return meta("Class", bases, {})

def eager(iterable):
    if PYTHON_3: return list(iterable)
    return iterable

def ord(value):
    if PYTHON_3 and type(value) == int: return value
    return _ord(value)

def chr(value):
    if PYTHON_3: return _bytes([value])
    if type(value) == int: return _chr(value)
    return value

def chri(value):
    if PYTHON_3: return value
    if type(value) == int: return _chr(value)
    return value

def bytes(value):
    if not PYTHON_3: return value
    if value == None: return value
    if type(value) == _bytes: return value
    return value.encode("latin-1")

def str(value):
    if not PYTHON_3: return value
    if value == None: return value
    if type(value) == _str: return value
    return value.decode("latin-1")

def orderable(value):
    if not PYTHON_3: return value
    return Orderable(value)

def is_str(value):
    return type(value) == _str

def is_unicode(value):
    if PYTHON_3: return type(value) == _str
    else: return type(value) == unicode #@UndefinedVariable

def is_bytes(value):
    if PYTHON_3: return type(value) == _bytes
    else: return type(value) == _str #@UndefinedVariable

def reduce(*args, **kwargs):
    if PYTHON_3: return functools.reduce(*args, **kwargs)
    return _reduce(*args, **kwargs)

def reload(*args, **kwargs):
    if PYTHON_3: return imp.reload(*args, **kwargs)
    return _reload(*args, **kwargs)

def urlopen(*args, **kwargs):
    if PYTHON_3: return urllib.request.urlopen(*args, **kwargs)
    else: return urllib2.urlopen(*args, **kwargs) #@UndefinedVariable

def build_opener(*args, **kwargs):
    if PYTHON_3: return urllib.request.build_opener(*args, **kwargs)
    else: return urllib2.build_opener(*args, **kwargs) #@UndefinedVariable

def urlparse(*args, **kwargs):
    return _urlparse.urlparse(*args, **kwargs)

def urlencode(*args, **kwargs):
    if PYTHON_3: return urllib.parse.urlencode(*args, **kwargs)
    else: return urllib.urlencode(*args, **kwargs) #@UndefinedVariable

def quote(*args, **kwargs):
    if PYTHON_3: return urllib.parse.quote(*args, **kwargs)
    else: return urllib.quote(*args, **kwargs) #@UndefinedVariable

def quote_plus(*args, **kwargs):
    if PYTHON_3: return urllib.parse.quote_plus(*args, **kwargs)
    else: return urllib.quote_plus(*args, **kwargs) #@UndefinedVariable

def unquote(*args, **kwargs):
    if PYTHON_3: return urllib.parse.unquote(*args, **kwargs)
    else: return urllib.unquote(*args, **kwargs) #@UndefinedVariable

def unquote_plus(*args, **kwargs):
    if PYTHON_3: return urllib.parse.unquote_plus(*args, **kwargs)
    else: return urllib.unquote_plus(*args, **kwargs) #@UndefinedVariable

def parse_qs(*args, **kwargs):
    if PYTHON_3: return urllib.parse.parse_qs(*args, **kwargs)
    else: return _urlparse.parse_qs(*args, **kwargs) #@UndefinedVariable

def cmp_to_key(*args, **kwargs):
    if PYTHON_3: return dict(key = functools.cmp_to_key(*args, **kwargs)) #@UndefinedVariable
    else: return dict(cmp = args[0])

def StringIO(*args, **kwargs):
    if PYTHON_3: return cStringIO.StringIO(*args, **kwargs)
    else: return _StringIO.StringIO(*args, **kwargs)

def BytesIO(*args, **kwargs):
    if PYTHON_3: return cStringIO.BytesIO(*args, **kwargs)
    else: return cStringIO.StringIO(*args, **kwargs)

class Orderable(tuple):
    """
    Simple tuple type wrapper that provides a simple
    first element ordering, that is compatible with
    both the python 2 and python 3+ infra-structures.
    """

    def __cmp__(self, value):
        return self[0].__cmp__(value[0])

    def __lt__(self, value):
        return self[0].__lt__(value[0])
