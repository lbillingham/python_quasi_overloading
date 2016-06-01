# -*- coding: utf-8 -*-
"""
Example 'overloaded' class building using the (IMHO) most pythonic
version: classmethod non-defauult initilizers
"""

import math


def xyz_from_dif(d, i, f):
    """
    north- east-, down- pointing components
    from
            * declination- `d`
            * inclination- `i`
            * total field strength- `f`
    with `d` and `i` given in degrees
    """
    d = math.radians(d)
    i = math.radians(i)
    horiz = abs(f * math.cos(i))
    north = horiz * math.cos(d)
    east = horiz * math.sin(d)
    down = f * math.sin(i)
    return north, east, down


class MagneticField(object):
    def __init__(self, x, y, z):
        """
        a magneitc field defined by:
            * north-pointing- `x` (nT)
            * east-pointing- `y` (nT)
            * down-pointing- `z` (nT)
        components
        """
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_dif(cls, d, i, f):
        """
        construct a MagneticField by giving:
            * declination- `d` (degrees)
            * inclination- `i` (degrees)
            * total field strength- `f` (nT)
        not the usual xyz components
        """
        north, east, down = xyz_from_dif(d, i, f)
        return cls(x=north, y=east, z=down)

    def __repr__(self):
        """let us print ourselves"""
        outy = 'MagneticField(x={}, y={}, z={})'.format(self.x, self.y, self.z)
        return outy

    @property
    def d(self):
        """declination (degrees)... added so looks like attribute not method"""
        decln = math.degrees(math.atan2(self.y, self.x))
        return decln

    @property
    def i(self):
        """inclination (degrees)"""
        incln = math.degrees(math.atan2(self.z, self.h))
        return incln

    @property
    def f(self):
        """total field strength (nT)"""
        l2norm = math.sqrt(self.y**2 + self.x**2 + self.z**2)
        return l2norm

    @property
    def h(self):
        """horizontal field strength (nT)"""
        horiz = math.sqrt(self.y**2 + self.x**2)
        return horiz


def main():
    """
    excercise our MagneticField class
    """
    bxyz = MagneticField(1.0, 0.0, 10)
    print('bxyz =', bxyz)
    print("bxyz's declination =", bxyz.d)
    print("bxyz's inclination =", bxyz.i)

    bdif = MagneticField.from_dif(30, 60, 100)
    print('ran MagneticField.from_dif({}, {}, {})'.format(
        bdif.d, bdif.i, bdif.f)
    )
    print('got: bdif =', bdif)
    print("bdif's north component =", bdif.x)


if __name__ == '__main__':
    main()
