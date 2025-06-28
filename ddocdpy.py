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


if __name__ == '__main__':
    app = DdoApplication(False)
    app.MainLoop()

