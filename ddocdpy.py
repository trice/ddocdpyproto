import wx
from wx import xrc


class DdoApplication(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource('MyProjectBase.xrc')
        self.init_frame()
        return True

    def init_frame(self):
        self.window_frame = self.res.LoadFrame(None, 'DdoCdFrame')
        self.window_frame.Show()
        self.Bind(wx.EVT_MENU, self.on_new_character,
                  id=xrc.XRCID('new_character_menu'))
        self.Bind(wx.EVT_MENU, self.on_save_character,
                  id=xrc.XRCID('save_character_menu'))
        self.Bind(wx.EVT_MENU, self.on_about, id=xrc.XRCID('about_menu_item'))
        self.Bind(wx.EVT_MENU, self.on_exit, id=xrc.XRCID('exit_menu_item'))

    def on_about(self, event):
        # Load the dialog from XRC
        about_dlg = self.res.LoadDialog(self.GetTopWindow(), "AboutDialog")
        about_dlg.ShowModal()
        about_dlg.Destroy()

    def on_new_character(self, event):
        wx.MessageBox("Coming Soon...")

    def on_save_character(self, event):
        wx.MessageBox("Saving Character...")

    def on_exit(self, event):
        self.window_frame.Close()


if __name__ == '__main__':
    app = DdoApplication(False)
    app.MainLoop()
