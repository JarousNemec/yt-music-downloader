# 🎵 YouTube Music Playlist Downloader (GUI)

A simple desktop application built with **Python + Tkinter** that allows you to download entire **YouTube Music playlists** as `.mp3` files.  
It uses `ytmusicapi` to fetch playlist data and `yt_dlp` to handle the actual downloading and conversion to audio.

---

## ✨ Features

- ✅ Paste any YouTube or YouTube Music playlist URL  
- ✅ Downloads all tracks as high-quality `.mp3` files  
- ✅ Built-in GUI (Tkinter) — no need to use the console  
- ✅ Real-time console output inside the app  
- ✅ Can be compiled into a standalone `.exe`

---

## 🧩 Requirements

- Python **3.10+**
- The following Python libraries:

```javascript
pip install yt-dlp ytmusicapi mutagen tkinter
```
(Tkinter is usually included with Python on Windows.)

## 🚀 Run from Source
Clone or download this repository:

```javascript
git clone https://github.com/yourusername/ytmusic-downloader-gui.git
cd ytmusic-downloader-gui
```
(Optional but recommended) Create a virtual environment:

```javascript
python -m venv venv
venv\Scripts\activate
```
Install dependencies:

```javascript
pip install -r requirements.txt
```
(Or use the list above.)

Run the app:

```javascript
python main.py
```
## 🧱 Build a Standalone .exe
To package the app as a standalone Windows executable, use PyInstaller:

Install Nuitka:

```javascript
pip install nuitka
```
Build the app:

```javascript
python -m nuitka --onefile --lto=no --remove-output --nofollow-import-to=yt_dlp.extractor.lazy_extractors --assume-yes-for-downloads --enable-plugin=tk-inter --windows-console-mode=disable --include-data-dir=venv/Lib/site-packages/ytmusicapi=ytmusicapi --include-data-dir=venv/Lib/site-packages/yt_dlp=yt_dlp --output-filename=ytmusic-downloader.exe main.py
```
⚠️ On Linux/Mac, replace ; with : in --add-data paths.

Your compiled .exe will appear in:

```javascript
dist/ytmusic-downloader.exe
```
You can now run it directly without Python installed:

```javascript
dist/ytmusic-downloader.exe
```