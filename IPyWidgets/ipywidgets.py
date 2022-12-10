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


# Unlinking widgets
"""
Unlinking the widgets is simple. All you have to do is call .unlink on the link object. 
Try changing one of the widgets above after unlinking to see that they can be independently changed.
"""
# mylink.unlink()


# Widget List

# Imports for JupyterLite
%pip install -q ipywidgets
# Note: you may need to restart the kernel to use updated packages.

import ipywidgets as widgets

# IntSlider
widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

# FloatSlider
widgets.FloatSlider(
    value=7.5,
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)

#  displayed vertically.

widgets.FloatSlider(
    value=7.5,
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='vertical',
    readout=True,
    readout_format='.1f',
)


# FloatLogSlider
widgets.FloatLogSlider(
    value=10,
    base=10,
    min=-10, # max exponent of base
    max=10, # min exponent of base
    step=0.2, # exponent step
    description='Log Slider'
)


# IntRangeSlider
widgets.IntRangeSlider(
    value=[5, 7],
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d',
)

# FloatRangeSlider

widgets.FloatRangeSlider(
    value=[5, 7.5],
    min=0,
    max=10.0,
    step=0.1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)




# Widget Events

# Special events
# Imports for JupyterLite
%pip install -q ipywidgets

import ipywidgets as widgets
print(widgets.Button.on_click.__doc__)

# Example
from IPython.display import display
button = widgets.Button(description="Click Me!")
output = widgets.Output()

display(button, output)

def on_button_clicked(b):
    with output:
        print("Button clicked.")

button.on_click(on_button_clicked)
