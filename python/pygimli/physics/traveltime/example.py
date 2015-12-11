#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Example refraction script applied to an example file
    (shaly bedrock detection from Günther&Rücker (2006), EAGE Near Surface)
"""
import os

import pygimli as pg
from pygimli.physics import Refraction

# load example file explicitly from same directory (if called from elsewhere)
ra = Refraction(os.path.dirname(__file__) + '/example_topo.sgt')
print(ra)
if False:  # possible (typical) actions
    ra.showData()  # show only data (right after init)
    ra.showVA()  # show apparent velocity image
    ra.createMesh(depth=10.)  # pass non-default meshing options
    ra.createStartModel(vtop=500, vbottom=2000)

ra.createMesh(depth=25., paraDX=0.2)  # pass non-default meshing options
ra.run(lam=300, zweight=0.1)  # use vtop/vbottom for startmodel
ra.showResultAndFit()  # typical output: model and data with response
pg.wait()
