#  Cross platform GUI toolkit for Python, "Phoenix" version

#  PyPi: https://pypi.org/project/wxPython/
#  Docs: https://wxpython.org/

#  pip install wxPython


import wx

# create an application object.
app = wx.App()

frm = wx.Frame(None, title="Hello World")
frm.Show()
app.MainLoop()

