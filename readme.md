pyinstaller --onefile --noconsole --add-data "venv/Lib/site-packages/ytmusicapi;ytmusicapi" --add-data "venv/Lib/site-packages/yt_dlp;yt_dlp" --name "ytmusic-downloader" main.py
