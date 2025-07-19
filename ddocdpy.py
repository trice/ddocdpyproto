import wx
from wx import xrc
from library.ddocdlib import class_description, look_up_hp
from library.ddocdspend import get_ability_range, point_spender
from library.ddocdtype import AbilityType


class DdoApplication(wx.App):
    def OnInit(self):
        self.res = xrc.XmlResource('MyProjectBase.xrc')
        self.build_point_default = 28
        self.build_point_balance = 28
        self.ability_default = 8
        self.selected_abilities = [8, 8, 8, 8, 8, 8]
        self.class_name = ""
        self.hp = 0
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

        self.class_name_ctrl = xrc.XRCCTRL(self.window_frame, "m_class",
                                           wx.Choice)
        self.class_description = xrc.XRCCTRL(self.window_frame,
                                             "m_class_description",
                                             wx.StaticText)

        self.description_sizer = xrc.XRCCTRL(self.window_frame,
                                             "m_descsizer",
                                             wx.BoxSizer)

        self.hp_ctrl = xrc.XRCCTRL(self.window_frame, "m_hp", wx.StaticText)

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

        ability_ints = get_ability_range(self.build_point_default)
        ability_strings = list(map(str, ability_ints))

        if self.strength is not None:
            self.strength.Set(ability_strings)
            self.strength.SetSelection(0)
            self.Bind(wx.EVT_CHOICE, self.on_strength_changed,
                      id=xrc.XRCID('m_strength'))

        if self.dexterity is not None:
            self.dexterity.Set(ability_strings)
            self.dexterity.SetSelection(0)
            self.Bind(wx.EVT_CHOICE, self.on_dexterity_changed,
                      id=xrc.XRCID('m_dexterity'))

        if self.constitution is not None:
            self.constitution.Set(ability_strings)
            self.constitution.SetSelection(0)
            self.Bind(wx.EVT_CHOICE, self.on_constitution_changed,
                      id=xrc.XRCID('m_constitution'))

        if self.intelligence is not None:
            self.intelligence.Set(ability_strings)
            self.intelligence.SetSelection(0)
            self.Bind(wx.EVT_CHOICE, self.on_intelligence_changed,
                      id=xrc.XRCID('m_intelligence'))

        if self.wisdom is not None:
            self.wisdom.Set(ability_strings)
            self.wisdom.SetSelection(0)
            self.Bind(wx.EVT_CHOICE, self.on_wisdom_changed,
                      id=xrc.XRCID('m_wisdom'))

        if self.charisma is not None:
            self.charisma.Set(ability_strings)
            self.charisma.SetSelection(0)
            self.Bind(wx.EVT_CHOICE, self.on_charisma_changed,
                      id=xrc.XRCID('m_charisma'))

    def on_about(self, event):
        # Load the dialog from XRC
        about_dlg = self.res.LoadDialog(self.GetTopWindow(), "AboutDialog")
        about_dlg.ShowModal()
        about_dlg.Destroy()

    def on_new_character(self, event):
        wx.MessageBox("Coming Soon...")
        # reset points
        # reset wxChoices to defaults
        # reset class

    def on_save_character(self, event):
        wx.MessageBox("Saving Character...")

    def on_exit(self, event):
        self.window_frame.Close()

    def on_class_selected(self, event):
        index = self.class_name_ctrl.GetSelection()
        class_name = self.class_name_ctrl.GetString(index)
        self.class_name = class_name
        description = class_description(class_name)
        self.class_description.SetLabel(description)
        self.class_description.GetContainingSizer().Layout()

    def on_strength_changed(self, event):
        strength = int(event.String)
        self.build_point_balance = point_spender(8, strength,
                                                 self.build_point_balance)
        self.update_build_points_view()
        self.update_ability_choices_except_for(AbilityType.Strength)
        self.selected_abilities[0] = strength

    def on_dexterity_changed(self, event):
        dexterity = int(event.String)
        self.build_point_balance = point_spender(8, dexterity,
                                                 self.build_point_balance)
        self.update_build_points_view()
        self.update_ability_choices_except_for(AbilityType.Dexterity)
        self.selected_abilities[1] = dexterity

    def on_constitution_changed(self, event):
        constitution = int(event.String)
        self.build_point_balance = point_spender(8, constitution,
                                                 self.build_point_balance)
        self.update_build_points_view()
        self.update_ability_choices_except_for(AbilityType.Constitution)
        self.selected_abilities[2] = constitution
        self.hp = look_up_hp(constitution, self.class_name)
        self.hp_ctrl.SetLabel(str(self.hp))

    def on_intelligence_changed(self, event):
        intelligence = int(event.String)
        self.build_point_balance = point_spender(8, intelligence,
                                                 self.build_point_balance)
        self.update_build_points_view()
        self.update_ability_choices_except_for(AbilityType.Intelligence)
        self.selected_abilities[3] = intelligence

    def on_wisdom_changed(self, event):
        wisdom = int(event.String)
        self.build_point_balance = point_spender(8, wisdom,
                                                 self.build_point_balance)
        self.update_build_points_view()
        self.update_ability_choices_except_for(AbilityType.Wisdom)
        self.selected_abilities[4] = wisdom

    def on_charisma_changed(self, event):
        charisma = int(event.String)
        self.build_point_balance = point_spender(8, charisma,
                                                 self.build_point_balance)
        self.update_build_points_view()
        self.update_ability_choices_except_for(AbilityType.Charisma)
        self.selected_abilities[5] = charisma

    def update_build_points_view(self):
        bp_label = xrc.XRCCTRL(self.window_frame, "m_build_points",
                               wx.StaticText)
        bp_label.SetLabel(f"{self.build_point_balance} pts")

    def update_ability_choices_except_for(self, ability):
        ability_ints = get_ability_range(self.build_point_balance)
        ability_strs = list(map(str, ability_ints))

        local_str = self.strength.GetSelection()
        local_dex = self.dexterity.GetSelection()
        local_con = self.constitution.GetSelection()
        local_int = self.intelligence.GetSelection()
        local_wis = self.wisdom.GetSelection()
        local_cha = self.charisma.GetSelection()

        if ability != AbilityType.Strength and local_str == 0:
            self.strength.Set(ability_strs)
            self.strength.SetSelection(0)

        if ability != AbilityType.Dexterity and local_dex == 0:
            self.dexterity.Set(ability_strs)
            self.dexterity.SetSelection(0)

        if ability != AbilityType.Constitution and local_con == 0:
            self.constitution.Set(ability_strs)
            self.constitution.SetSelection(0)

        if ability != AbilityType.Intelligence and local_int == 0:
            self.intelligence.Set(ability_strs)
            self.intelligence.SetSelection(0)

        if ability != AbilityType.Wisdom and local_wis == 0:
            self.wisdom.Set(ability_strs)
            self.wisdom.SetSelection(0)

        if ability != AbilityType.Charisma and local_cha == 0:
            self.charisma.Set(ability_strs)
            self.charisma.SetSelection(0)


if __name__ == '__main__':
    app = DdoApplication(False)
    app.MainLoop()
