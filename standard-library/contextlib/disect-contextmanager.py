# Trying to understand contextlib.contextmanager
#
#    First step: make sure we're independent of the standard-libary.
#    So: copy paste needed code here.

import sys


tq84_indent = 0

def tq84_print(txt):
    print( ('  ' * tq84_indent) + txt)



from _abc import (get_cache_token, _abc_init, _abc_register,
                      _abc_instancecheck, _abc_subclasscheck, _get_dump,
                      _reset_registry, _reset_caches)

tq84_print('before class ABCMeta')

class ABCMeta(type):
     """Metaclass for defining Abstract Base Classes (ABCs).

     Use this metaclass to create an ABC.  An ABC can be subclassed
     directly, and then acts as a mix-in class.  You can also register
     unrelated concrete classes (even built-in classes) and unrelated
     ABCs as 'virtual subclasses' -- these and their descendants will
     be considered subclasses of the registering ABC by the built-in
     issubclass() function, but the registering ABC won't show up in
     their MRO (Method Resolution Order) nor will method
     implementations defined by the registering ABC be callable (not
     even via super()).
     """
     def __new__(mcls, name, bases, namespace, **kwargs):
         global tq84_indent
         tq84_indent+=1
         tq84_print('ABCMeta.__new__')
         cls = super().__new__(mcls, name, bases, namespace, **kwargs)
         _abc_init(cls)
         tq84_indent-=1
         return cls

     def register(cls, subclass):
         """Register a virtual subclass of an ABC.

         Returns the subclass, to allow usage as a class decorator.
         """
         return _abc_register(cls, subclass)

     def __instancecheck__(cls, instance):
         """Override for isinstance(instance, cls)."""
         return _abc_instancecheck(cls, instance)

     def __subclasscheck__(cls, subclass):
         """Override for issubclass(subclass, cls)."""
         return _abc_subclasscheck(cls, subclass)

#q     def _dump_registry(cls, file=None):
#q         """Debug helper to print the ABC registry."""
#q         print(f"Class: {cls.__module__}.{cls.__qualname__}", file=file)
#q         print(f"Inv. counter: {get_cache_token()}", file=file)
#q         (_abc_registry, _abc_cache, _abc_negative_cache,
#q          _abc_negative_cache_version) = _get_dump(cls)
#q         print(f"_abc_registry: {_abc_registry!r}", file=file)
#q         print(f"_abc_cache: {_abc_cache!r}", file=file)
#q         print(f"_abc_negative_cache: {_abc_negative_cache!r}", file=file)
#q         print(f"_abc_negative_cache_version: {_abc_negative_cache_version!r}",
#q               file=file)

     def _abc_registry_clear(cls):
         """Clear the registry (for debugging or testing)."""
         _reset_registry(cls)

     def _abc_caches_clear(cls):
         """Clear the caches (for debugging or testing)."""
         _reset_caches(cls)


tq84_print('before class ABC')

class ABC(metaclass=ABCMeta):
    """Helper class that provides a standard way to create an ABC using
    inheritance.
    """
    __slots__ = ()

tq84_print('before def recursive_repr')

def recursive_repr(fillvalue='...'):
    'Decorator to make a repr function return fillvalue for a recursive call'

    global tq84_indent
    tq84_indent+=1
    tq84_print('recursive_repr')


    def decorating_function(user_function):
        repr_running = set()

        def wrapper(self):
            key = id(self), get_ident()
            if key in repr_running:
                return fillvalue
            repr_running.add(key)
            try:
                result = user_function(self)
            finally:
                repr_running.discard(key)
            return result

        # Can't use functools.wraps() here because of bootstrap issues
        wrapper.__module__ = getattr(user_function, '__module__')
        wrapper.__doc__ = getattr(user_function, '__doc__')
        wrapper.__name__ = getattr(user_function, '__name__')
        wrapper.__qualname__ = getattr(user_function, '__qualname__')
        wrapper.__annotations__ = getattr(user_function, '__annotations__', {})
        return wrapper

    tq84_indent-=1
    return decorating_function

class ContextDecorator(object):
    "A base class or mixin that enables context managers to work as decorators."

    def _recreate_cm(self):
        """Return a recreated instance of self.

        Allows an otherwise one-shot context manager like
        _GeneratorContextManager to support use as
        a decorator via implicit recreation.

        This is a private interface just for _GeneratorContextManager.
        See issue #11647 for details.
        """
        return self

    def __call__(self, func):
        print('  !!!! contextDecorator.__call__')

        @wraps(func)
        def inner(*args, **kwds):
            with self._recreate_cm():
                return func(*args, **kwds)
        return inner




tq84_print('before class partial')
class partial:

    __slots__ = "func", "args", "keywords", "__dict__", "__weakref__"

    def __new__(cls, func, /, *args, **keywords):
        global tq84_indent
        tq84_indent+=1
        tq84_print('partial.__new__')

#q      if not callable(func):
#q          raise TypeError("the first argument must be callable")

#q      if hasattr(func, "func"):
#q          print('    partial.__new__, func has attribute func')
#q          args = func.args + args
#q          keywords = {**func.keywords, **keywords}
#q          func = func.func

        self = super(partial, cls).__new__(cls)
#       print(f'  partial.__new__, type(self)  = {type(self)}')
#       print(f'  partial.__new__, dir(self)  = {dir(self)}')

        self.func = func
        self.args = args
        self.keywords = keywords
        tq84_indent-=1
        return self

    def __call__(self, /, *args, **keywords):
        global tq84_indent
        tq84_indent+=1
        tq84_print('partial.__call__()')
        keywords = {**self.keywords, **keywords}
        tq84_indent-=1
        return self.func(*self.args, *args, **keywords)

#q  @recursive_repr()
#q  def __repr__(self):
#q      tq84_print('!!!!!__repr__')
#q      qualname = type(self).__qualname__
#q      args = [repr(self.func)]
#q      args.extend(repr(x) for x in self.args)
#q      args.extend(f"{k}={v!r}" for (k, v) in self.keywords.items())
#q      if type(self).__module__ == "functools":
#q          return f"functools.{qualname}({', '.join(args)})"
#q      return f"{qualname}({', '.join(args)})"

#q  def __reduce__(self):
#q      tq84_print('!!!!!!!!!!!!!!!!!!!!!!!!!1')
#q      return type(self), (self.func,), (self.func, self.args,
#q             self.keywords or None, self.__dict__ or None)

#q  def __setstate__(self, state):
#q      tq84_print('!!!!!!!!!!!!!!!!!!!!!!!!!1')
#q      if not isinstance(state, tuple):
#q          raise TypeError("argument to __setstate__ must be a tuple")
#q      if len(state) != 4:
#q          raise TypeError(f"expected 4 items in state, got {len(state)}")
#q      func, args, kwds, namespace = state
#q      if (not callable(func) or not isinstance(args, tuple) or
#q         (kwds is not None and not isinstance(kwds, dict)) or
#q         (namespace is not None and not isinstance(namespace, dict))):
#q          raise TypeError("invalid partial state")
#q
#q      args = tuple(args) # just in case it's a subclass
#q      if kwds is None:
#q          kwds = {}
#q      elif type(kwds) is not dict: # XXX does it need to be *exactly* dict?
#q          kwds = dict(kwds)
#q      if namespace is None:
#q          namespace = {}
#q
#q      self.__dict__ = namespace
#q      self.func = func
#q      self.args = args
#q      self.keywords = kwds


WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
WRAPPER_UPDATES     = ('__dict__',)

def update_wrapper(wrapper,
                   wrapped,
                   assigned = WRAPPER_ASSIGNMENTS,
                   updated = WRAPPER_UPDATES):
    """Update a wrapper function to look like the wrapped function

       wrapper is the function to be updated
       wrapped is the original function
       assigned is a tuple naming the attributes assigned directly
       from the wrapped function to the wrapper function (defaults to
       functools.WRAPPER_ASSIGNMENTS)
       updated is a tuple naming the attributes of the wrapper that
       are updated with the corresponding attribute from the wrapped
       function (defaults to functools.WRAPPER_UPDATES)
    """
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
    # from the wrapped function when updating __dict__
    wrapper.__wrapped__ = wrapped
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper


def abstractmethod(funcobj):
    """A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.

    Usage:

        class C(metaclass=ABCMeta):
            @abstractmethod
            def my_abstract_method(self, ...):
                ...
    """
    funcobj.__isabstractmethod__ = True
    return funcobj


class AbstractContextManager(ABC):

    """An abstract base class for context managers."""

    def __enter__(self):
        """Return `self` upon entering the runtime context."""
        global tq84_indent
        tq84_indent+=1
        tq84_print('AbstractContextManager.__enter__')
        tq84_indent-=1
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """Raise any exception triggered within the runtime context."""
        global tq84_indent
        tq84_indent+=1
        tq84_print('AbstractContextManager.__exit__')
        tq84_indent-=1
        return None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AbstractContextManager:
            return _collections_abc._check_methods(C, "__enter__", "__exit__")
        return NotImplemented

class _GeneratorContextManagerBase:
    """Shared functionality for @contextmanager and @asynccontextmanager."""

    def __init__(self, func, args, kwds):
        self.gen = func(*args, **kwds)
        self.func, self.args, self.kwds = func, args, kwds
        # Issue 19330: ensure context manager instances have good docstrings
        doc = getattr(func, "__doc__", None)
        if doc is None:
            doc = type(self).__doc__
        self.__doc__ = doc
        # Unfortunately, this still doesn't provide good help output when
        # inspecting the created context manager instances, since pydoc
        # currently bypasses the instance docstring and shows the docstring
        # for the class instead.
        # See http://bugs.python.org/issue19404 for more details.

class _GeneratorContextManager(_GeneratorContextManagerBase,
                               AbstractContextManager,
                               ContextDecorator):
    """Helper for @contextmanager decorator."""

    def _recreate_cm(self):
        print('!!!!!!!!!!!!!!')
        # _GCM instances are one-shot context managers, so the
        # CM must be recreated each time a decorated function is
        # called
        return self.__class__(self.func, self.args, self.kwds)

    def __enter__(self):
        print('--> _GeneratorContextManager, __enter__')
        # do not keep args and kwds alive unnecessarily
        # they are only needed for recreation, which is not possible anymore
        del self.args, self.kwds, self.func
        try:
            return next(self.gen)
        except StopIteration:
            raise RuntimeError("generator didn't yield") from None

    def __exit__(self, exType, exValue, traceback):
        print('  _GeneratorContextManager, __exit__')
        if exType is None:
            print('    __exit__, exType is None')
            try:
                next(self.gen)
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")
        else:
            print('    __exit__, exType is not None')
            if exValue is None:
                # Need to force instantiation so we can reliably
                # tell if we get the same exception back
                exValue = exType()
            else:
                print('    exValue:', exValue)
            try:
                self.gen.throw(exType, exValue, traceback)
            except StopIteration as exc:
                # Suppress StopIteration *unless* it's the same exception that
                # was passed to throw().  This prevents a StopIteration
                # raised inside the "with" statement from being suppressed.
                return exc is not exValue
            except RuntimeError as exc:
                # Don't re-raise the passed in exception. (issue27122)
                if exc is exValue:
                    return False
                # Likewise, avoid suppressing if a StopIteration exception
                # was passed to throw() and later wrapped into a RuntimeError
                # (see PEP 479).
                if exType is StopIteration and exc.__cause__ is exValue:
                    return False
                raise
            except:
                # only re-raise if it's *not* the exception that was
                # passed to throw(), because __exit__() must not raise
                # an exception unless __exit__() itself failed.  But throw()
                # has to raise the exception to signal propagation, so this
                # fixes the impedance mismatch between the throw() protocol
                # and the __exit__() protocol.
                #
                # This cannot use 'except BaseException as exc' (as in the
                # async implementation) to maintain compatibility with
                # Python 2, where old-style class exceptions are not caught
                # by 'except BaseException'.
                if sys.exc_info()[1] is exValue:
                    return False
                raise
            raise RuntimeError("generator didn't stop after throw()")




def wraps(wrapped,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):

    """Decorator factory to apply update_wrapper() to a wrapper function

       Returns a decorator that invokes update_wrapper() with the decorated
       function as the wrapper argument and the arguments to wraps() as the
       remaining arguments. Default arguments are as for update_wrapper().
       This is a convenience function to simplify applying partial() to
       update_wrapper().
    """
    print(f'  wraps, wrapped = {wrapped.__name__}')
    return partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)


def contextmanager(func):
    print(f'contextmanager, func = {func.__name__}')
    @wraps(func)
    def helper(*args, **kwds):
        print('--> helper, return _GeneratorContextManager')
        return _GeneratorContextManager(func, args, kwds)
    return helper


print('\n\n')

class resource:
      
      def __init__(self, name):
          global tq84_indent
          tq84_indent+=1
          tq84_print(f'  resource.__init__, name = {name}')
          self.name = name
          tq84_indent-=1

      def doSomething(self):
          tq84_print(f'  Resource named {self.name} is used to do something')

      def doSomethingBad(self):
          tq84_print(f'  Resource named {self.name} is doing something bad.')
          raise Exception('uh oh…')
          tq84_print(f'  Not reached.')

      def release(self):
          tq84_print(f'  Resource {self.name} is released.')

          

@contextmanager
def getResource(name):

    tq84_print(f'Going to aquire resource, giving it the name {name}')
    res = resource(name)
 
    try:
       tq84_print('  Returning (yielding) the resource')
       yield res

    finally:
       tq84_print('Calling res.release()')
       res.release()

print('-----------------------------------------')

try:
   with getResource('demo') as abc:
        tq84_indent+=1
#       print('****', dir(abc))
        tq84_print(f'I own the resource named {abc.name}')
   
   
        abc.doSomething()
        tq84_print('This line IS reached')
        tq84_indent-=1

except BaseException as ex:
       tq84_print(f'Caught excpetion: {str(ex)}')


print('-----------------------------------------')

try:
   with getResource('demo') as abc:
        tq84_indent += 1
#       tq84_print('****', dir(abc))
        tq84_print(f'I own the resource named {abc.name}')
   
   
        abc.doSomething()
        tq84_indent -= 1
        abc.doSomethingBad()
        tq84_print('This line is not reached')

except BaseException as ex:
       tq84_print(f'Caught excpetion: {str(ex)}')
