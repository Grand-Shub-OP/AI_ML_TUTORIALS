#example 3
#------------------
#g- = green solid line
#ro = red circle dot

import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[1,4,9,16],'k^')
plt.xlabel("----some numbers---->")
plt.ylabel("----Squared Values------->")

plt.axis([0,5,0,17])

plt.show()


#character	color
#  'b'	blue
#  'g'	green
#  'r'	red
#  'c'	cyan
#  'm'	magenta
#  'y'	yellow
#  'k'	black
#  'w'	white

#character	description
#  '-'	solid line style
#  '--'	dashed line style
#  '-.'	dash-dot line style
#  ':'	dotted line style
#  'o'	circle marker
#  'v'	triangle_down marker
#  '^'	triangle_up marker
#  '<'	triangle_left marker
#  '>'	triangle_right marker
#  '1'	tri_down marker
#  '2'	tri_up marker
#  '3'	tri_left marker
#  '4'	tri_right marker
#  's'	square marker
#  'p'	pentagon marker
#  '*'	star marker
#  'h'	hexagon1 marker
#  'H'	hexagon2 marker
#  '+'	plus marker
#  'x'	x marker
#  'd'	thin_diamond marker
#  '|'	vline marker
#  '_'	hline marker