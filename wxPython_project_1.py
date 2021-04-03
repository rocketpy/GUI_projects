import wx


class MyFrame(wx.MDIParentFrame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        
        menu_bar = wx.MenuBar()
        f_menu = wx.Menu()
        item = wx.MenuItem(f_menu, "Exit", "Exit from App")
        item.SetBitmap(wx.Bitmap(file_name.png))  # add image
        f_menu.Append(item)
        # or
        # item = f_menu.Append(wx.ID_EXIT, "Exit", "Exit from App")
        menu_bar.Append(f_menu, "File")
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.exit_from_menu, item)
        
    def exit_from_menu(self, event):
        self.Close()
        
        
app = wx.App()
frame = MyFrame(None, "Project 1")
frame.Show()
app.MainLoop()
        
