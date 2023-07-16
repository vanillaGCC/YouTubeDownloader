import wx
import logging

class LogFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(LogFrame, self).__init__(*args, **kwargs)

        self.log_textctrl = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_READONLY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.log_textctrl, 1, wx.EXPAND)
        self.SetSizer(sizer)

        # Logger setup
        logger = logging.getLogger()
        logger.addHandler(LogHandler(self.log_textctrl))

class LogHandler(logging.Handler):
    def __init__(self, log_output):
        super(LogHandler, self).__init__()
        self.log_output = log_output

    def emit(self, record):
        msg = self.format(record)
        self.log_output.AppendText(f'{msg}\n')