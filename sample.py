import os
from yt_dlp import YoutubeDL

# ffmpegのbinフォルダを環境変数に登録する（既に環境変数に登録済みなら、この処理は不要）
path = "C:/Users/nyous/ffmpeg-master-latest-win64-gpl-shared/bin"
os.environ["PATH"] += "" if path in os.environ["PATH"] else ";" + path

# オプションを指定（最高画質の動画と最高音質の音声を取り出し結合するためのオプション）


# インスタンスの生成


ydl = YoutubeDL()
info_dict = ydl.extract_info(
    "https://www.youtube.com/watch?v=IDBj6RUHDRA", download=False
)
video_title = info_dict.get("title", None)
print(video_title)
# ダウンロードの実行
# result = ydl.download(["https://www.youtube.com/watch?v=lLvOpIF8xwU"])
