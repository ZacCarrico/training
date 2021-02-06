The purpose of this directory is to provide examples
for where python imports can cause problems and
how to fix them.

First, the most important thing to know for imports
is what sys.paths are available. For example
if you execute a module this way:
`python3 main.py`
then main.py's directory is in sys.path. Note that
it doesn't matter what your cwd is in this case; ONLY
main.py's directory will be added to sys.path.

However, if you execute a module this way:
`python3 -m main` # note that there's no .py b/c the . indicates a package
then IT DOES matter what your cwd is. Your cwd path
will be added to sys.path, and main.py's path will
NOT be added to sys.path.

Note: When running a script directly, it is impossible 
to import anything from its parent directory

#### Problem Case 1.
main.py: `imports a.a.py`, which works
a.py: `import sub_a.sub_a.py`, which fails b/c sub_a is
not visible within sys.path; it's one
directory beneath `python_imports`

#### Solution1: Modify the import statement to work with sys.path 
If executing `python3 main.py` use `import a.sub_a.sub_a` in `a.py`
HOWEVER, this will now fail if running a.py directly (ie `python3 a/a.py`).
You can run both main.py and a.py successfully using `python3 -m`. 
Remember, when running `python3 -m` your cwd matters so you need
to be in `python_imports` when running `python3 -m main`
and `python3 -m a.a`

#### Solution2: Add to sys.path in the imported modules
I couldn't get this one to work such that either main.py or a/a.py
could be executed using `python3 <file_name>.py`


#### Problem Case 2. Importing from a parent directory
Avoid this. However, if you absolutely need to it's apparently
possible to by modifying sys.path.