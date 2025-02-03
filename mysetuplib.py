from sys import argv as _a
from setuptools import setup
import builtins as __builtins__
__builtins__.setup = setup
__builtins__.mysetup_py = lambda scope : lambda main : main() if scope["__name__"]=="__main__" else scope.__setitem__("mybuild", lambda:(_a.extend(["sdist bdist_wheel"]),main()))