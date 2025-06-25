import wx

class DdoFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        self.makeMenuBar()

    def makeMenuBar(self):
        fileMenu = wx.Menu()

        newCharacterMenuItem = fileMenu.Append(-1, "&New Character...\tCtrl-N",
                                               "Create a new character")

        fileMenu.AppendSeparator()

        exitMenuItem = fileMenu.Append(wx.ID_EXIT)

        theMenu = wx.MenuBar()
        theMenu.Append(fileMenu, "&File")

        self.SetMenuBar(theMenu)

        self.Bind(wx.EVT_MENU, self.onNewCharacter, newCharacterMenuItem)
        self.Bind(wx.EVT_MENU, self.onExit, exitMenuItem)


    def onNewCharacter(self, event):
        wx.MessageBox("Coming soon...")

    def onExit(self, event):
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frm = DdoFrame(None, title="DDO CD (Prototype)")
    frm.Show()
    app.MainLoop()

