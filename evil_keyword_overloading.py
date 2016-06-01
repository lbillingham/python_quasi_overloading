# -*- coding: utf-8 -*-
"""
Probably evil demonstration of overloading a python class 'constructor'
using a switch mechanism based on supplying different keyword arguments
"""
import inspect
import math


class WithKeyWordArgs(object):
    """
    Fakes 'constructor' overloading by allowing a variety of keyword
    arguments but only one at a time.
    Almost certainly evil.
    """
    def __init__(self, use_sin=None, use_cos=None, use_tan=None):
        # introspect what I was called with and see how many args were set
        #   raise an error if not exactly 1
        args_i_take = inspect.signature(self.__init__)
        locs = locals()
        arg_vals_got = [locs.get(key) for key in args_i_take.parameters.keys()]
        if arg_vals_got.count(None) != len(arg_vals_got) - 1:
            arg_list = list(args_i_take.parameters.keys())
            raise ValueError('must set only one of {}'.format(arg_list))

        self.a_param = 'default'
        self._use_func = None
        if use_sin:
            self.a_param = 'called with sin'
            self._use_func = math.sin
        elif use_cos:
            self.a_param = 'called with cos'
            self._use_func = math.cos
        elif use_tan:
            self.a_param = 'called with tan'
            self._use_func = math.tan
        else:
            self.a_param = 'fail safe'
            self._use_func = print

    def __repr__(self):
        """this is what you get if you try to print an instance"""
        outstr = ('WithKeyWordArgs\n  a_param={}'.format(self.a_param))
        return outstr

    def a_method(self, some_float):
        """
        Return a math function applied to `some_float`
        where the math function is defined as the class is
        initialized
        """
        return self._use_func(some_float)


def main():
    """
    excercise our 'overloaded' class initilization
    """
    angle = math.radians(90.0)
    siny_instance = WithKeyWordArgs(use_sin=True)
    cosy_instance = WithKeyWordArgs(use_cos=True)
    print('sin({}) is evilly {}'.format(angle, siny_instance.a_method(angle)))
    print('cos({}) is evilly {}'.format(angle, cosy_instance.a_method(angle)))
    print('#######################################################')
    print('should now raise an error')
    try:
        WithKeyWordArgs(use_tan=True, use_cos=True)
    except ValueError as verr:
        print('I did raise an error\nit was:')
        print('  {}'.format(verr))


if __name__ == '__main__':
    main()
