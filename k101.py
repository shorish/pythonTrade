#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-30 01:08:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

def sta001(k, nyear, xd):
	d2 = np.fv(k, nyear, -xd, -xd)
	d2 = round(d2)
	return d2

d40 = 1.4 * 40
print "d40 1.4 x 40 = " ,d40
d1 = sta001(0.05, 40-1, 1.4)
print "01保守投资模式，", d1, round(d1/d40)

d2 = sta001(0.2, 40-1, 1.4)
print "02激进投资模式，", d2, round(d2/d40)

dk = round(d2/d1)
print "dk, 两者差别（xx倍）：", dk