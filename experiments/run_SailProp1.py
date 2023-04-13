 # -*- coding: utf-8 -*-

import matplotlib.pyplot as pl
import pandas as pd
from math import pi

from pybemt.solver import Solver

s = Solver('SailProp1.ini')

df, sections = s.run_sweep('rpm', 1, 100, 100)
pitches = s.optimize_pitch()
print("Pitches:")
print(pitches)
print("END")