from functools import wraps as smart_deco_wraps
from martialaw.martialaw import * #well;; it was Joke Libs;; well;;
import builtins
from os.path import splitext

'''
# mdoc, markdown as docstring

# function / decorators
 - globmdoc(globals()) : set module (global scope) docstring as samename-markdown markup-text value.
 - @objmdoc(markdown path) : set obj which class, function's document as markdown file's value.

#not suggested
 - @setmdoc : it gives one positional string argument what markdown file value, but as using is seems like giving mdpath not md value. @setmdoc decorated method should be work as setting docstring by input data.
'''

function_on_builtins = lambda f : setattr(builtins, f.__name__, f)
extless = lambda path : splitext([path])[0]

@(lambda g : lambda f : smart_deco_wraps(f)(g(f))) #smart_closer_deco_wraps
@martialaw
def setmdoc(setter : callable, mdpath : str):
    '''
    # `@setmdoc` decorator. setmdoc by get md value to your function -by mdoc

    ## using example

    ```
    @setmdoc
    def funcion_name(argument_name_that_what_md_value : itmightbestr_orderwise_ithinkthat_impossible_but_anyway_optional_typehint) -> optional_typehint:
        ... #function source that set doc
    ```
    '''
    with open(mdpath) as fp: setter(fp.read())

@function_on_builtins
def globmdoc(scope : dict) -> None:
    '''
    # globmdoc(globals()) -by mdoc
    find same name (extless script file path is same.) md path to set global scope docstring by get __doc__
    '''
    @setmdoc
    def mdocsetter(src : str) -> None:
        '''
        #mdocsetter -byy mdoc global scope docstring setter
        '''
        scope['__doc__'] = src
    mdocsetter(f'{extless(scope["__file__"])}.md') # find same name (extless script file path is same.) path

@function_on_builtins
@setmdoc
def objmdoc(md : str) -> callable:
    '''
    # `@objmdoc` decorator `@objmdoc(mdpath)` to use -by mdoc

    TIPS : also can use at class
    '''
    return lambda ob : setattr(ob, '__doc__', md)