# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"YouTubeDownloader", pos = wx.DefaultPosition, size = wx.Size( 503,290 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"ダウンロードしたい動画のURLを入力" ), wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.URL = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		self.URL.SetMaxSize( wx.Size( 500,-1 ) )

		bSizer5.Add( self.URL, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.GetInfo = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"GO!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.GetInfo, 0, wx.ALL|wx.EXPAND, 5 )


		sbSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		self.FileName1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FileName1.Wrap( -1 )

		sbSizer1.Add( self.FileName1, 0, wx.ALL, 5 )


		bSizer2.Add( sbSizer1, 0, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"出力先" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.SaveDirectory = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"保存先", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		bSizer11.Add( self.SaveDirectory, 0, wx.ALL|wx.EXPAND, 5 )

		self.DownloadPath = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DownloadPath.Wrap( -1 )

		bSizer11.Add( self.DownloadPath, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizer2.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"ファイル名", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer9.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.FileName = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer10.Add( self.FileName, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )


		sbSizer2.Add( bSizer8, 1, wx.EXPAND, 5 )


		bSizer2.Add( sbSizer2, 0, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"出力形式" ), wx.VERTICAL )

		self.Video = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Video(mp4)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.Video, 0, wx.ALL, 5 )

		self.Audio = wx.RadioButton( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Audio(mp3)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.Audio, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( sbSizer3, 0, wx.RIGHT, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"品質" ), wx.VERTICAL )

		self.High = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"High", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.High, 0, wx.ALL, 5 )

		self.Low = wx.RadioButton( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Low", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.Low, 0, wx.ALL, 5 )


		bSizer13.Add( sbSizer4, 0, 0, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.Save = wx.Button( self.m_panel3, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.Save, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer14.Add( bSizer15, 1, wx.ALIGN_BOTTOM, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.Cancel = wx.Button( self.m_panel3, wx.ID_ANY, u"キャンセル", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.Cancel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer14.Add( bSizer17, 0, wx.ALIGN_BOTTOM, 5 )


		bSizer13.Add( bSizer14, 1, wx.ALIGN_BOTTOM, 5 )


		bSizer2.Add( bSizer13, 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer2 )
		self.m_panel3.Layout()
		bSizer2.Fit( self.m_panel3 )
		bSizer25.Add( self.m_panel3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer25 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyFrame1OnClose )
		self.GetInfo.Bind( wx.EVT_BUTTON, self.GetInfoOnButtonClick )
		self.SaveDirectory.Bind( wx.EVT_BUTTON, self.SaveDirectoryOnButtonClick )
		self.Video.Bind( wx.EVT_RADIOBUTTON, self.VideoOnRadioButton )
		self.Audio.Bind( wx.EVT_RADIOBUTTON, self.AudioOnRadioButton )
		self.High.Bind( wx.EVT_RADIOBUTTON, self.HighOnRadioButton )
		self.Low.Bind( wx.EVT_RADIOBUTTON, self.LowOnRadioButton )
		self.Save.Bind( wx.EVT_BUTTON, self.SaveOnButtonClick )
		self.Cancel.Bind( wx.EVT_BUTTON, self.CancelOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def MyFrame1OnClose( self, event ):
		event.Skip()

	def GetInfoOnButtonClick( self, event ):
		event.Skip()

	def SaveDirectoryOnButtonClick( self, event ):
		event.Skip()

	def VideoOnRadioButton( self, event ):
		event.Skip()

	def AudioOnRadioButton( self, event ):
		event.Skip()

	def HighOnRadioButton( self, event ):
		event.Skip()

	def LowOnRadioButton( self, event ):
		event.Skip()

	def SaveOnButtonClick( self, event ):
		event.Skip()

	def CancelOnButtonClick( self, event ):
		event.Skip()


