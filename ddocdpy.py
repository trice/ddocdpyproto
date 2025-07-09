import wx
from wx import xrc
from library.ddocdlib import class_description
from library.ddocdspend import get_ability_range, point_spender


class DdoApplication(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource('MyProjectBase.xrc')
        self.init_frame()
        self.__build_point_default = 28
        self.__build_point_balance = 28
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

        self.class_name_ctrl = xrc.XRCCTRL(self.window_frame, "m_class",
                                           wx.Choice)
        self.class_description = xrc.XRCCTRL(self.window_frame,
                                             "m_class_description",
                                             wx.StaticText)

        self.description_sizer = xrc.XRCCTRL(self.window_frame,
                                             "m_descsizer",
                                             wx.BoxSizer)

        self.Bind(wx.EVT_CHOICE, self.on_class_selected,
                  id=xrc.XRCID('m_class'))

        self.on_class_selected(None)

        # find all the ability wx.Choice and then fill them with options
        self.strength = xrc.XRCCTRL(self.window_frame, "m_strength",
                                    wx.Choice)

        self.dexterity = xrc.XRCCTRL(self.window_frame, "m_dexterity",
                                    wx.Choice)

        self.constitution = xrc.XRCCTRL(self.window_frame, "m_constitution",
                                    wx.Choice)

        self.intelligence = xrc.XRCCTRL(self.window_frame, "m_intelligence",
                                    wx.Choice)

        self.wisdom = xrc.XRCCTRL(self.window_frame, "m_wisdom",
                                    wx.Choice)

        self.charisma = xrc.XRCCTRL(self.window_frame, "m_charisma",
                                    wx.Choice)

        ability_ints = get_ability_range(28)
        ability_strings = list(map(str, ability_ints))

        if self.strength is not None:
            self.strength.Set(ability_strings)

        if self.dexterity is not None:
            self.dexterity.Set(ability_strings)

        if self.constitution is not None:
            self.constitution.Set(ability_strings)

        if self.intelligence is not None:
            self.intelligence.Set(ability_strings)

        if self.wisdom is not None:
            self.wisdom.Set(ability_strings)

        if self.charisma is not None:
            self.charisma.Set(ability_strings)

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

    def on_class_selected(self, event):
        index = self.class_name_ctrl.GetSelection()
        class_name = self.class_name_ctrl.GetString(index)
        description = class_description(class_name)
        self.class_description.SetLabel(description)
        self.class_description.GetContainingSizer().Layout()


if __name__ == '__main__':
    app = DdoApplication(False)
    app.MainLoop()
