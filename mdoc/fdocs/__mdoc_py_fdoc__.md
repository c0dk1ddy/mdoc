# @__mdoc_py_fdoc__(func)

well bro it just function only works in mdoc.py, it just set fdocs temperally.

## src

```python
with open(f'{dirname(__file__)}/fdocs/{func.__name__}') as fp: func.__doc__ = fp.read()
return func
```

## it should be nobody instrest about it.