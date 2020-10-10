# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from bookroom import BookRoomThread


###########################################################################
# Class AppFrame
###########################################################################


class AppFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"SeleniumTools", pos=wx.DefaultPosition,
                          size=wx.Size(712, 560), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer_frame = wx.BoxSizer(wx.VERTICAL)

        self.m_pages = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_bookroom = wx.Panel(
            self.m_pages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer_book = wx.BoxSizer(wx.VERTICAL)

        self.m_paneltop = wx.Panel(self.m_bookroom, wx.ID_ANY,
                                   wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer_top = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(
            self.m_paneltop, wx.ID_ANY, u"开始预定时间", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer_top.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_textCtrlStartBook = wx.TextCtrl(
            self.m_paneltop, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_top.Add(self.m_textCtrlStartBook, 0, wx.ALL, 5)

        self.m_buttonStart = wx.Button(
            self.m_paneltop, wx.ID_ANY, u"开始预定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer_top.Add(self.m_buttonStart, 0, wx.ALL, 5)
        self.isStartBook = False
        self.Bind(wx.EVT_BUTTON, self.StartBookRoom, self.m_buttonStart)

        self.m_paneltop.SetSizer(bSizer_top)
        self.m_paneltop.Layout()
        bSizer_top.Fit(self.m_paneltop)
        bSizer_book.Add(self.m_paneltop, 0, wx.ALL, 5)

        self.m_bookcfg = wx.ScrolledWindow(
            self.m_bookroom, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
        self.m_bookcfg.SetScrollRate(5, 5)
        gSizer_bookcfg = wx.GridSizer(0, 4, 0, 0)

        self.m_staticText3 = wx.StaticText(
            self.m_bookcfg, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        gSizer_bookcfg.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrlUserName = wx.TextCtrl(
            self.m_bookcfg, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer_bookcfg.Add(self.m_textCtrlUserName, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(
            self.m_bookcfg, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        gSizer_bookcfg.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.m_textCtrlPasswd = wx.TextCtrl(
            self.m_bookcfg, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        gSizer_bookcfg.Add(self.m_textCtrlPasswd, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(
            self.m_bookcfg, wx.ID_ANY, u"房间名称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        gSizer_bookcfg.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrlRoomName = wx.TextCtrl(
            self.m_bookcfg, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer_bookcfg.Add(self.m_textCtrlRoomName, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(
            self.m_bookcfg, wx.ID_ANY, u"开始时间", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        gSizer_bookcfg.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_textCtrlStartTime = wx.TextCtrl(
            self.m_bookcfg, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer_bookcfg.Add(self.m_textCtrlStartTime, 0, wx.ALL, 5)

        self.m_staticText43 = wx.StaticText(
            self.m_bookcfg, wx.ID_ANY, u"截止时间", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText43.Wrap(-1)
        gSizer_bookcfg.Add(self.m_staticText43, 0, wx.ALL, 5)

        self.m_textCtrlEndTime = wx.TextCtrl(
            self.m_bookcfg, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer_bookcfg.Add(self.m_textCtrlEndTime, 0, wx.ALL, 5)

        self.m_staticText44 = wx.StaticText(
            self.m_bookcfg, wx.ID_ANY, u"预定日期", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText44.Wrap(-1)
        gSizer_bookcfg.Add(self.m_staticText44, 0, wx.ALL, 5)

        self.m_textCtrlBookDate = wx.TextCtrl(
            self.m_bookcfg, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer_bookcfg.Add(self.m_textCtrlBookDate, 0, wx.ALL, 5)

        self.m_bookcfg.SetSizer(gSizer_bookcfg)
        self.m_bookcfg.Layout()
        gSizer_bookcfg.Fit(self.m_bookcfg)
        bSizer_book.Add(self.m_bookcfg, 1, wx.EXPAND | wx.ALL, 5)

        self.m_booklog = wx.Panel(self.m_bookroom, wx.ID_ANY,
                                  wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer_booklog = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrlBookLog = wx.TextCtrl(self.m_booklog, wx.ID_ANY, wx.EmptyString,
                                             wx.DefaultPosition, wx.DefaultSize,
                                             wx.HSCROLL | wx.TE_MULTILINE | wx.TE_RICH)
        bSizer_booklog.Add(self.m_textCtrlBookLog, 0, wx.EXPAND | wx.ALL, 5)

        self.m_booklog.SetSizer(bSizer_booklog)
        self.m_booklog.Layout()
        bSizer_booklog.Fit(self.m_booklog)
        bSizer_book.Add(self.m_booklog, 1, wx.EXPAND | wx.ALL, 5)

        self.m_bookroom.SetSizer(bSizer_book)
        self.m_bookroom.Layout()
        bSizer_book.Fit(self.m_bookroom)
        self.m_pages.AddPage(self.m_bookroom, u"研究小间预定", True)
        self.m_reggmail = wx.Panel(
            self.m_pages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer_register = wx.BoxSizer(wx.VERTICAL)

        self.m_registercfg = wx.ScrolledWindow(
            self.m_reggmail, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
        self.m_registercfg.SetScrollRate(5, 5)
        gSizer_bookcfg1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText31 = wx.StaticText(
            self.m_registercfg, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        gSizer_bookcfg1.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.m_textCtrl31 = wx.TextCtrl(
            self.m_registercfg, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer_bookcfg1.Add(self.m_textCtrl31, 0, wx.ALL, 5)

        self.m_registercfg.SetSizer(gSizer_bookcfg1)
        self.m_registercfg.Layout()
        gSizer_bookcfg1.Fit(self.m_registercfg)
        bSizer_register.Add(self.m_registercfg, 1, wx.EXPAND | wx.ALL, 5)

        self.m_registerlog = wx.Panel(
            self.m_reggmail, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer_reglog = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrlRegLog = wx.TextCtrl(self.m_registerlog, wx.ID_ANY, wx.EmptyString,
                                            wx.DefaultPosition, wx.DefaultSize,
                                            wx.HSCROLL | wx.TE_MULTILINE | wx.TE_RICH)
        bSizer_reglog.Add(self.m_textCtrlRegLog, 0, wx.ALL, 5)

        self.m_registerlog.SetSizer(bSizer_reglog)
        self.m_registerlog.Layout()
        bSizer_reglog.Fit(self.m_registerlog)
        bSizer_register.Add(self.m_registerlog, 1, wx.EXPAND | wx.ALL, 5)

        self.m_reggmail.SetSizer(bSizer_register)
        self.m_reggmail.Layout()
        bSizer_register.Fit(self.m_reggmail)
        self.m_pages.AddPage(self.m_reggmail, u"谷歌账号注册", False)

        bSizer_frame.Add(self.m_pages, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer_frame)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def StartBookRoom(self, event):
        if not self.isStartBook:
            self.bookthread = BookRoomThread('预定房间')
            self.bookthread.start()
            self.m_buttonStart.SetLabelText('关闭预定')
            self.isStartBook = True
        else:
            self.bookthread.stop()
            self.m_buttonStart.SetLabelText('开始预定')
            self.isStartBook = False


if __name__ == "__main__":
    app = wx.App()
    window = AppFrame(None)
    window.Show()
    app.MainLoop()
