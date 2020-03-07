import wx
import wx.adv


class CalendarFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='请输入查询日期', pos=(700, 200))
        cal = wx.adv.GenericCalendarCtrl(self, -1, wx.DateTime(), pos=(0, 0),
                                         style=wx.adv.CAL_SHOW_HOLIDAYS | wx.adv.CAL_SUNDAY_FIRST |
                                               wx.adv.CAL_SEQUENTIAL_MONTH_SELECTION | wx.adv.CAL_SEQUENTIAL_MONTH_SELECTION)
        self.cal = cal
        self.holidays = [(10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6)]  # (设置休息日)
        self.set_holiday()
        self.sel_days = []
        self.Bind(wx.adv.EVT_CALENDAR, self.on_sel_date, cal)
        # self.Bind(wx.adv.EVT_CALENDAR_SEL_CHANGED,self.on_sel_date,cal)
        self.Bind(wx.adv.EVT_CALENDAR_PAGE_CHANGED, self.on_change_month, cal)
        button_1 = wx.Button(self, -1, label='提交', pos=(250, 150), name='button_1')
        self.Bind(wx.EVT_BUTTON, self.on_submit, button_1)

    def set_holiday(self):
        # 1.设置休息日
        cur_month = self.cal.GetDate().GetMonth() + 1  # convert wxDateTime 0-11 => 1-12
        [self.cal.SetHoliday(i[1]) for i in self.holidays if i[0] == cur_month]

    def on_sel_date(self, evt):
        sel_day = evt.GetDate().Format('%F')
        day_int = evt.GetDate().GetDay()
        attr2 = wx.adv.CalendarDateAttr()
        if self.cal.GetAttr(day_int) and self.cal.GetAttr(day_int).IsHoliday():
            return
        if sel_day not in self.sel_days:
            self.sel_days.append(sel_day)
            attr1 = wx.adv.CalendarDateAttr()
            attr1.SetBackgroundColour(wx.Colour(64, 224, 205))
            self.cal.SetAttr(day_int, attr1)
        else:
            self.sel_days.remove(sel_day)
            attr1 = wx.adv.CalendarDateAttr()
            attr1.SetBackgroundColour(wx.Colour(255, 255, 255))
            self.cal.SetAttr(day_int, attr1)

    def on_change_month(self, evt=None):
        # 1.设置休息日
        cur_month = self.cal.GetDate().GetMonth() + 1  # convert wxDateTime 0-11 => 1-12
        [self.cal.SetHoliday(i[1]) for i in self.holidays if i[0] == cur_month]

        # 2.清除last_month bg_colour
        day_list = list(set([int(i[-2:]) for i in self.sel_days]))
        for i in day_list:
            if self.cal.GetAttr(i):
                attr1 = wx.adv.CalendarDateAttr()
                attr1.SetBackgroundColour(wx.Colour(255, 255, 255))
                if self.cal.GetAttr(i).IsHoliday():
                    attr1.SetTextColour(wx.Colour(255, 0, 0))
                    attr1.SetHoliday(1)
                self.cal.SetAttr(i, attr1)

        # 3.设置sel_days  bg_colour
        sel_col = [i for i in self.sel_days if int(i[5:7]) == cur_month]
        day_list = list(set([int(i[-2:]) for i in sel_col]))
        for i in day_list:
            attr2 = wx.adv.CalendarDateAttr()
            attr2.SetBackgroundColour(wx.Colour(64, 224, 205))
            self.cal.SetAttr(i, attr2)

    def on_submit(self, evt):
        print(self.sel_days)
        self.Close()
        self.Destroy()


def get_date():
    app = wx.App()
    frame = CalendarFrame()
    frame.Show()
    app.MainLoop()
    return frame.sel_days


if __name__ == '__main__':
    sel_days = get_date()
    print(sel_days)