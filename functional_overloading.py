# -*- coding: utf-8 -*-
"""
overloading making an instance by letting the caller pass a function that will
give us what we need
"""
import math
import numpy as np

from classmethod_overloading import MagneticField


class FunctionTakingMageticField(MagneticField):

    def __init__(self, xyz_returning_function, that_functions_keyword_args):
        """
        MagneticField constucted from a function and a dictionary
        of named arguments.

        the function should be such that calling
        `xyz_returning_function(kwargs)`
        returns the north- east- and down-pointing components of the magnetic
        field as a tuple
        """
        x, y, z = xyz_returning_function(**that_functions_keyword_args)
        super(FunctionTakingMageticField, self).__init__(x=x, y=y, z=z)


def xyz_from_hdz(h, d, z):
    """
    North-(`x` [nT]), east-(`y` [nT]), and down-(`z` [nT])
    pointing components given:
        * horizontal-field- `h` (nT)
        * declination- `d` (degrees)
        * down-pointing component- `z` (nT)
    """
    d = math.radians(d)
    north = h * math.cos(d)
    east = h * math.sin(d)
    return north, east, z


def main():
    """excercise our FunctionTakingMageticField code"""
    hdz_args = {'d': 90.0, 'h': 1.0, 'z': 10}
    b = FunctionTakingMageticField(xyz_from_hdz, hdz_args)
    print('constructed a magnetic field by passing a function: ', b)
    expected = [hdz_args.get(cpt) for cpt in ['h', 'd', 'z']]
    got_back = [b.h, b.d, b.z]
    np.testing.assert_allclose(got_back, expected)
    print('\nif this printed then we got back same hdz as expected')


if __name__ == '__main__':
    main()
