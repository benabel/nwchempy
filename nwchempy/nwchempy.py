#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import numpy as np


class NWChem:
    """" Parse nwchem output files. """
    def __init__(self, file):
        self.file = file
        self.nwo = open('{}.nwo'.format(self.file)).read()

    def print_output(self):
        """Print nwchem output to stdout"""
        print(self.nwo)


class NWChemFreq(NWChem):
    """Handle vibrationnals informations."""
    def get_freq(self):
        """Return array of frequencies and intensities"""
        FIND = r'-*\n.*Projected Infra Red Intensities.*(.*||.*\n)+^-*$'
        pattern = re.compile(FIND, re.MULTILINE)
        match = pattern.search(self.nwo)
        if match:
            parsed = match.group()
        else:
            raise ValueError("Aucune donnée vibrationnelle trouvée")
        data = np.loadtxt(parsed.replace('||', '').splitlines(),
                          skiprows=4, comments='--')
        return data
