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

# IntProgress
widgets.IntProgress(
    value=7,
    min=0,
    max=10,
    description='Loading:',
    bar_style='', # 'success', 'info', 'warning', 'danger' or ''
    style={'bar_color': 'maroon'},
    orientation='horizontal'
)

# FloatProgress
widgets.FloatProgress(
    value=7.5,
    min=0,
    max=10.0,
    description='Loading:',
    bar_style='info',
    style={'bar_color': '#ffff00'},
    orientation='horizontal'
)

# BoundedIntText
widgets.BoundedIntText(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Text:',
    disabled=False
)


# BoundedFloatText
widgets.BoundedFloatText(
    value=7.5,
    min=0,
    max=10.0,
    step=0.1,
    description='Text:',
    disabled=False
)

# IntText
widgets.IntText(
    value=7,
    description='Any:',
    disabled=False
)

# FloatText
widgets.FloatText(
    value=7.5,
    description='Any:',
    disabled=False
)

# ToggleButton
widgets.ToggleButton(
    value=False,
    description='Click me',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Description',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)

# Checkbox
widgets.Checkbox(
    value=False,
    description='Check me',
    disabled=False,
    indent=False
)

# Valid
# The valid widget provides a read-only indicator. !!!
widgets.Valid(
    value=False,
    description='Valid!',
)


# Dropdown

widgets.Dropdown(
    options=['1', '2', '3'],
    value='2',
    description='Number:',
    disabled=False,
)

# The following is also valid, displaying the words 'One', 'Two', 'Three' as the dropdown choices but returning the values 1, 2, 3.
widgets.Dropdown(
    options=[('One', 1), ('Two', 2), ('Three', 3)],
    value=2,
    description='Number:',
)

# RadioButtons
widgets.RadioButtons(
    options=['pepperoni', 'pineapple', 'anchovies'],
#    value='pineapple', # Defaults to 'pineapple'
#    layout={'width': 'max-content'}, # If the items' names are long
    description='Pizza topping:',
    disabled=False
)

# With dynamic layout and very long labels
widgets.Box(
    [
        widgets.Label(value='Pizza topping with a very long label:'),
        widgets.RadioButtons(
            options=[
                'pepperoni',
                'pineapple',
                'anchovies',
                'and the long name that will fit fine and the long name that will fit fine and the long name that will fit fine '
            ],
            layout={'width': 'max-content'}
        )
    ]
)


# Select
widgets.Select(
    options=['Linux', 'Windows', 'macOS'],
    value='macOS',
    # rows=10,
    description='OS:',
    disabled=False
)


# SelectionSlider
widgets.SelectionSlider(
    options=['scrambled', 'sunny side up', 'poached', 'over easy'],
    value='sunny side up',
    description='I like my eggs ...',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True
)






# Widget Events

# Special events
# Imports for JupyterLite
# %pip install -q ipywidgets

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
