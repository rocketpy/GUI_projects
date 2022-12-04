# ipywidgets: Jupyter interactive widgets

# https://github.com/jupyter-widgets/ipywidgets/
# Docs: https://ipywidgets.readthedocs.io/en/latest/index.html

# Install

# pip:  pip install ipywidgets
# conda:  conda install -c conda-forge ipywidgets

# use widgets to build interactive GUIs for your notebooks

import ipywidgets as widgets

widgets.IntSlider()

from IPython.display import display
w = widgets.IntSlider()
display(w)

w = widgets.IntSlider()
display(w)

w.value

w.value = 100


# Keys

# In addition to value, most widgets share keys, description, and disabled.
# To see the entire list of synchronized, stateful properties of any specific widget, you can query the keys property.

w.keys


# Shorthand for setting the initial values of widget properties
widgets.Text(value='Hello World!', disabled=True)

# Linking two similar widgets
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))
