import wx


class MyFrame(wx.MDIParentFrame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        
        menu_bar = wx.MenuBar()
        f_menu = wx.Menu()
        item = f_menu.Append(wx.ID_EXIT, "Exit", "Exit from App")
        
app = wx.App()
frame = MyFrame(None, "Project 1")
frame.Show()
app.MainLoop()
        
