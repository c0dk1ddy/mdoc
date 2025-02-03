from functools import wraps as _smart_deco_wraps #[HIDED]
from martialaw.martialaw import martialaw as _my_personal_closer #well;; it was Joke Libs;; well;; [tip : if U couldn't import it; use pip install `martialaw`] #[HIDED]
import builtins as _builtins #[HIDED]
from os.path import splitext as _splitext #[HIDED]
from os.path import dirname as _dirname #use at __mdoc_py_fdoc__, #[HIDED]

# ========================== START MAINSRC ========================= #

addattr = lambda ret, obj, name, value : (ret, setattr(obj, name, value))[0] # see docs.
function_on_builtins = lambda f : addattr(f, _builtins, f.__name__, f)
extless = lambda path : _splitext(path)[0] #path could be str

def __mdoc_py_fdoc__(func : callable) -> callable:
    with open(f'{_dirname(__file__)}/fdocs/{func.__name__}.md') as fp: func.__doc__ = fp.read()
    return func

with open(f'{_dirname(__file__)}/fdocs/__mdoc_py_fdoc__.md') as __fp__ : __mdoc_py_fdoc__.__doc__ = __fp__.read() #see? it's duck tape. It's fucking sucks that I meant.

@(lambda g : lambda f : _smart_deco_wraps(f)(g(f))) #smart_closer_deco_wraps
@_my_personal_closer
@__mdoc_py_fdoc__
def setmdoc(setter : callable, mdpath : str):
    with open(mdpath) as mdfile:
        return setter(mdfile.read())

@function_on_builtins
@__mdoc_py_fdoc__
def globmdoc(scope : dict) -> None:
    @setmdoc
    @__mdoc_py_fdoc__
    def mdocsetter(src : str) -> None:
        scope['__doc__'] = src #scope is global scope, as code shows.... haha;; (this comment write 4 docs)
    mdocsetter(f'{extless(scope["__file__"])}.md') # find same name (extless script file path is same.) path

@function_on_builtins
@setmdoc
@__mdoc_py_fdoc__
def objmdoc(md : str) -> callable:
    return lambda ob : addattr(ob, ob, '__doc__', md)

# ========================== END MAINSRC ========================= #

# ===== LOAD DOCS ===== #
globmdoc(globals())
# ===== LOAD DOCS ===== #

#oh shit I should clean it fuck!!!!!

#was should be simple............ ...oh............. ...nah....... ........no.....
#fstring...
#FP
#decorator
#nah shit.