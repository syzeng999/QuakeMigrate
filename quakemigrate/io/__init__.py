# -*- coding: utf-8 -*-
"""
The :mod:`quakemigrate.io` module handles the various input/output operations
performed by QuakeMigrate. This includes:

    * Reading waveform data - The submodule data.py can handle any waveform \
    data archives with regular directory structures.
    * Writing results - The submodule quakeio.py provides a suite of \
    functions to output QuakeMigrate results in the QuakeMigrate format.
    * Parse QuakeMigrate results into the ObsPy Catalog structure.
    * Various parsers to input files for different pieces of software. Feel \
    free to contribute more!

:copyright:
    2020, QuakeMigrate developers.
:license:
    GNU General Public License, Version 3
    (https://www.gnu.org/licenses/gpl-3.0.html)

"""

from .amplitudes import write_amplitudes  # NOQA
from .availability import read_availability, write_availability  # NOQA
from .cut_waveforms import write_cut_waveforms  # NOQA
from .data import Archive  # NOQA
from .event import Event  # NOQA
from .core import (read_lut, read_response_inv, read_stations,  # NOQA
                   read_vmodel, stations, Run)
from .scanmseed import ScanmSEED, read_scanmseed  # NOQA
from .triggered_events import (read_triggered_events,  # NOQA
                               write_triggered_events)