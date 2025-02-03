# mdoc, markdown as docstring

installation : `pip install mdocLib`
using : `import mdocLib`ls


## function / decorators
 - [`globmdoc(globals())` : set module (global scope) docstring as samename-markdown markup-text value.](./fdocs/globmdoc.md)
 - [`@objmdoc(markdown path)` : set obj which class, function's document as markdown file's value.](./fdocs/objmdoc.md)

### [globmdoc](./fdocs/globmdoc.md)

 > it can use when you using mdoc
 > ```python
 > #some_file.py
 > import mdoc #using mdoc
 > globmdoc(globals()) #using globmdocs
 > ```
 > 
 > that `some_file.py`'s document will be `some_file.md` which in same place.

### [objmdoc](./fdocs/objmdoc.md)
 
 > it also can use when you using mdoc
 > ```python
 > #any_file.py
 > import mdoc
 > @objmdoc("/somepath.md")
 > def some_funcion(*any, **way):
 >     ...
 > @objmdoc("/also_somepath.md")
 > class some_class:
 >     ...
 > ```
 > 
 > that objs will have docs by md.

## not suggested
 - [`@setmdoc`](./fdocs/setmdoc.md)
    it gives one positional string argument what markdown file value,
    but as using is seems like giving mdpath not md value.
    @setmdoc decorated method should be work as setting docstring by input data.

## inner systemic

# `# ===== [ LAMBAS ] ===== #`
 - `addattr(ret, obj, name, value)` setattr(obj, name, value), then return ret var.
 - `@function_on_builtins` : set function on builtins.
 - `extless(filepath)` : give extless file-name path

### ducktape and ....(?) hahaha;; function that use only mdoc.py that unusible, also not good.

 - [`__mdoc_py_fdoc__` : that ducktape](./fdocs/__mdoc_py_fdoc__.md)
 - [`mdocsetter` : well I couldn't explain it. it just super simple setter what coded by `@setmdoc`](./fdocs/mdocsetter.md)

#### `# [HIDED]` commented value
 - `from functools import wraps as _smart_deco_wraps #[HIDED]` -bettery
 - `from martialaw.martialaw import martialaw as _my_personal_closer #well;; it was Joke Libs;; well;; [tip : if U couldn't import it; use pip install `martialaw`] #[HIDED]` -depends
 - `import builtins as _builtins #[HIDED]` -bettery
 - `from os.path import splitext as _splitext #[HIDED]` -bettery
 - `from os.path import dirname as _dirname #use at __mdoc_py_fdoc__, #[HIDED]` -bettery