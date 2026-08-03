import wx
import wx.xrc

###########################################################################
## Class MySignFrame
###########################################################################

class MySignFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"人脸打卡识别系统", pos = wx.DefaultPosition, size = wx.Size( 1000,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.init_data()
		self.initMenu()

	def init_data(self):
		self.on = True  # 注册标识变量
		self.reg_msg = None  # 注册时显示信息
		self.del_msg = None  # 删除时显示信息
		self.search_msg = None  # 查询时显示信息
		self.command = None  # 当前执行的命令
		self.sql_name = 'my_Punch.db'  # 数据库名字
		self.recognize = True  # 打卡
		self.registration = False  # 注册
		self.search = True  # 查询
		self.c = None  # 定义游标
		self.conn = None  # 连接名
		self.user_id = []  # 用户ID
		self.user_name = []  # 用户名
		self.time_1 = []  # 上班时间
		self.logcat_late = []  # 打卡时间
		self.time_2 = []  # 下班时间
		self.dur_time = []  # 持续时间

	def initMenu(self):
		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_panel1 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer2 = wx.BoxSizer(wx.VERTICAL)

		self.btnSign = wx.Button(self.m_panel1, wx.ID_ANY, u"打卡", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer2.Add(self.btnSign, 0, wx.ALL, 5)

		# 使用wx.Image()添加背景图片
		self.imageBackgroud = wx.Image('background.jpg', wx.BITMAP_TYPE_ANY).Scale(500, 400)
		# 当id的值为-1或者wx.ID_ANY时，系统会随机分配一个id
		self.bmpSign = wx.StaticBitmap(self.m_panel1, wx.ID_ANY, wx.Bitmap(self.imageBackgroud), wx.Point(0, 40))
		bSizer2.Add(self.bmpSign, 0, wx.ALL, 5)

		self.m_panel1.SetSizer(bSizer2)
		self.m_panel1.Layout()
		bSizer2.Fit(self.m_panel1)
		self.m_notebook1.AddPage(self.m_panel1, u"员工打卡", True)
		self.m_panel2 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer3 = wx.BoxSizer(wx.VERTICAL)

		self.txtRegisterNum = wx.TextCtrl(self.m_panel2, wx.ID_ANY, u"工号", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer3.Add(self.txtRegisterNum, 0, wx.ALL, 5)

		self.txtName = wx.TextCtrl(self.m_panel2, wx.ID_ANY, u"姓名", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer3.Add(self.txtName, 0, wx.ALL, 5)

		self.btnRegister = wx.Button(self.m_panel2, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer3.Add(self.btnRegister, 0, wx.ALL, 5)

		# 使用wx.Image()添加背景图片
		self.imageBackgroud1 = wx.Image('background.jpg', wx.BITMAP_TYPE_ANY).Scale(500, 400)
		self.bmpRegister = wx.StaticBitmap(self.m_panel2, -1, wx.Bitmap(self.imageBackgroud1), wx.Point(0, 60))
		bSizer3.Add(self.bmpRegister, 0, wx.ALL, 5)

		self.m_panel2.SetSizer(bSizer3)
		self.m_panel2.Layout()
		bSizer3.Fit(self.m_panel2)
		self.m_notebook1.AddPage(self.m_panel2, u"人脸注册", False)
		self.m_panel3 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer4 = wx.BoxSizer(wx.VERTICAL)

		self.txtDeleteNum = wx.TextCtrl(self.m_panel3, wx.ID_ANY, u"工号", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer4.Add(self.txtDeleteNum, 0, wx.ALL, 5)

		self.btnDelete = wx.Button(self.m_panel3, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer4.Add(self.btnDelete, 0, wx.ALL, 5)

		self.m_panel3.SetSizer(bSizer4)
		self.m_panel3.Layout()
		bSizer4.Fit(self.m_panel3)
		self.m_notebook1.AddPage(self.m_panel3, u"人脸删除", False)
		self.m_panel4 = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		bSizer5 = wx.BoxSizer(wx.VERTICAL)

		self.btnSearch = wx.Button(self.m_panel4, wx.ID_ANY, u"查询", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer5.Add(self.btnSearch, 0, wx.ALL, 5)

		self.m_panel4.SetSizer(bSizer5)
		self.m_panel4.Layout()
		bSizer5.Fit(self.m_panel4)
		self.m_notebook1.AddPage(self.m_panel4, u"信息查询", False)

		bSizer1.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

		self.SetSizer(bSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

		# 按钮事件绑定
		self.btnSign.Bind(wx.EVT_BUTTON, self.sign_face)
		self.btnRegister.Bind(wx.EVT_BUTTON, self.register_face)
		self.btnDelete.Bind(wx.EVT_BUTTON, self.delete_face)
		self.btnSearch.Bind(wx.EVT_BUTTON, self.search_info)

	# Virtual event handlers, override them in your derived class
	def sign_face( self, event ):
		event.Skip()

	def register_face( self, event ):
		event.Skip()

	def delete_face( self, event ):
		event.Skip()

	def search_info( self, event ):
		event.Skip()


if __name__ == '__main__':
    app=wx.App()
    frame=MySignFrame(parent=None)
    frame.Show()
    app.MainLoop()
