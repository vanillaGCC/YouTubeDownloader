import wx
import YouTubeDownloader
import os
from yt_dlp import YoutubeDL
from MyProject1MyFrame1 import MyProject1MyFrame1

folder_path = ""
filetype = "mp4"
quality = "high"
Title = ""


class MyProject1MyFrame1Child(MyProject1MyFrame1):
    def __init__(self, parent):
        MyProject1MyFrame1.__init__(self, parent)

    def GetInfomation(self, url):
        try:
            ydl = YoutubeDL()
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get("title", None)
            return video_title
        except Exception:
            return False  # If error, the video_id is not valid

    def download(self, url, option):
        # インスタンスの生成
        ydl = YoutubeDL(option)
        try:
            # ダウンロードの実行
            result = ydl.download([url])
            return 1
        except Exception:
            return -1

    def optionGenerator(self, path):
        global filetype
        global quality
        if filetype == "mp4":
            if quality == "high":
                option = {
                    "outtmpl": path + "/" + Title,
                    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
                }
            else:
                option = {
                    "outtmpl": path + "/" + Title,
                    "format": "bestvideo[ext=mp4][height<=480]+bestaudio[ext=m4a]/best[ext=mp4][height<=480]",
                }
        else:
            if quality == "high":
                option = {
                    "format": "bestaudio/best",  # 最高品質の音声/動画を指定
                    "outtmpl": path + "/" + Title,  # デスクトップに動画タイトルで保存
                    "postprocessors": [
                        {
                            "key": "FFmpegExtractAudio",  # FFmpegを使ってオーディオを抽出
                            "preferredcodec": "mp3",  # mp3形式に変換
                            "preferredquality": "192",  # オーディオの品質を192kbpsに指定
                        }
                    ],
                }
            else:
                option = {
                    "outtmpl": path + "/" + Title,
                    "format": "bestaudio/best",
                    "postprocessors": [
                        {
                            "key": "FFmpegExtractAudio",
                            "preferredcodec": "mp3",  # 変換したい形式を指定
                            "preferredquality": "96",  # ビットレートを指定
                        }
                    ],
                }
        return option

    def GetInfoOnButtonClick(self, event):
        title=self.GetInfomation(self.URL.GetValue())
        if title is False:
            self.FileName1.SetLabel("無効なURLです")
        else:
            self.FileName1.SetLabel(title)

    def MyFrame1OnClose(self, event):
        """ダイアログボックス選択式のウィンドウクローズ"""
        # Yes/Noダイアログを使ってユーザに選択させる。
        dialog = wx.MessageDialog(
            None,
            "終了しますか？",
            "Window close dialog",
            wx.YES_NO,
        )
        ans = dialog.ShowModal()

        # YES=5103, NO=5104
        if ans == 5103:
            print("User selected YES button to close window.")
            self.Destroy()

    def CancelOnButtonClick(self, event):
        """ダイアログボックス選択式のウィンドウクローズ"""
        # Yes/Noダイアログを使ってユーザに選択させる。
        dialog = wx.MessageDialog(
            None,
            "終了しますか？",
            "Window close dialog",
            wx.YES_NO,
        )
        ans = dialog.ShowModal()

        # YES=5103, NO=5104
        if ans == 5103:
            print("User selected YES button to close window.")
            self.Destroy()

    def Rename(self):
        global Title
        if self.FileName.GetValue():
            Title = self.FileName.GetValue()
        else:
            Title = self.GetInfomation(self.URL.GetValue())

    def SaveDirectoryOnButtonClick(self, event):
        folder = wx.DirDialog(self, style=wx.DD_CHANGE_DIR, message="保存先フォルダ")

        if folder.ShowModal() == wx.ID_OK:
            global folder_path
            folder_path = folder.GetPath()
        folder.Destroy()
        self.DownloadPath.SetLabel(folder_path)

    def GetFileName(self):
        return self.FileName.GetValue()

    def VideoOnRadioButton(self, event):
        global filetype
        filetype = "mp4"

    def AudioOnRadioButton(self, event):
        global filetype
        filetype = "mp3"

    def HighOnRadioButton(self, event):
        global quality
        quality = "high"

    def LowOnRadioButton(self, event):
        global quality
        quality = "low"

    def SaveOnButtonClick(self, event):
        self.Rename()
        url = self.URL.GetValue()
        normalized_path = os.path.normpath(folder_path)
        option = self.optionGenerator(normalized_path)
        result = self.download(url, option)
        if result == 1:
            dialog = wx.MessageDialog(
                None,
                "保存しました",
                "完了",
                wx.OK,
            )
            dialog.ShowModal()
        else:
            dialog = wx.MessageDialog(
                None,
                "保存に失敗しました",
                "エラー",
                wx.OK,
            )
            dialog.ShowModal()
