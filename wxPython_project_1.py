import wx


class MyFrame(wx.MDIParentFrame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        
app = wx.App()
frame = MyFrame(None, "Project 1")
frame.Show()
app.MainLoop()
        
