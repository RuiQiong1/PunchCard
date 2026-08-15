import sqlite3

import wx
import wx.xrc


class MyFrameData(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"数据库操作", pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.Size(-1, -1), wx.DefaultSize)
        gSizer1 = wx.GridSizer(0, 2, 20, 15)
        self.btnCon = wx.Button(self, wx.ID_ANY, u"连接", wx.DefaultPosition, wx.Size(100, 50), 0)
        gSizer1.Add(self.btnCon, 0, wx.ALL, 5)
        self.btnAdd = wx.Button(self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.Size(100, 50), 0)
        gSizer1.Add(self.btnAdd, 0, wx.ALL, 5)
        self.btnSearch = wx.Button(self, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.Size(100, 50), 0)
        gSizer1.Add(self.btnSearch, 0, wx.ALL, 5)
        self.btnDelete = wx.Button(self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.Size(100, 50), 0)
        gSizer1.Add(self.btnDelete, 0, wx.ALL, 5)
        self.SetSizer(gSizer1)
        self.Layout()
        gSizer1.Fit(self)
        self.Centre(wx.BOTH)

        # Connect Events
        self.btnCon.Bind(wx.EVT_BUTTON, self.btnConClick)
        self.btnAdd.Bind(wx.EVT_BUTTON, self.btnAddClick)
        self.btnSearch.Bind(wx.EVT_BUTTON, self.btnSearchClick)
        self.btnDelete.Bind(wx.EVT_BUTTON, self.btnDeleteClick)

        self.sql_name = 'PunchTest.db'  # 数据库名字
        self.c = None  # 定义游标
        self.conn = None  # 连接名

    def __del__(self):
        pass

    # 连接数据库
    def btnConClick(self, event):
        conn = sqlite3.connect(self.sql_name)
        print("Opened database successfully!")
        c = conn.cursor()
        self.c = c
        self.conn = conn

    def btnAddClick(self, event):
        c, conn = self.c, self.conn
        c.execute('''CREATE TABLE if not exists attendance
        	           (user_id CHAR(50) PRIMARY KEY     NOT NULL,
        	           user_name      CHAR(50)    NOT NULL,
        	           sign_in_time Datetime,
        	           checking_state  CHAR(10) NOT NULL,
        	           sign_out_time Datetime,
        	           working_time float);''')
        conn.commit()
        print("创建成功！")

    def btnSearchClick(self, event):
        event.Skip()

    def btnDeleteClick(self, event):
        event.Skip()



if __name__ == '__main__':
    app = wx.App()
    main_win = MyFrameData(None)
    main_win.Show()
    app.MainLoop()
