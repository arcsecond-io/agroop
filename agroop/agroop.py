# -*- coding: utf-8 -*-

import click
import json
from astropy.coordinates import SkyCoord

from agroop.options import State

ECHO_PREFIX = u' • '

__all__ = [""]


def parse_coord_string(s, state):
    try:
        if state.verbose:
            click.echo(ECHO_PREFIX + 'Parsing REF coordinates input "{}"...'.format(s))
        return SkyCoord(s.replace(',', ' '), frame='icrs', unit='deg')
    except ValueError:
        if state.verbose:
            click.echo(ECHO_PREFIX + 'REF coordinates can be parsed. Looking for an object with name "{}"...'.format(s))
        from arcsecond import ArcsecondAPI
        obj = ArcsecondAPI(ArcsecondAPI.ENDPOINT_OBJECTS).read(s)
        coords = obj.get('ICRS_coordinates')
        return SkyCoord(coords.get('right_ascension'), coords.get('declination'), frame='icrs', unit='deg')
