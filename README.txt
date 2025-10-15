🎵 YouTube Music Playlist Downloader (GUI)

A simple desktop application built with Python + Tkinter that allows you
to download entire YouTube Music playlists as .mp3 files.
It uses ytmusicapi to fetch playlist data and yt_dlp to handle the
actual downloading and conversion to audio.

------------------------------------------------------------------------

✨ Features

-   ✅ Paste any YouTube or YouTube Music playlist URL
-   ✅ Downloads all tracks as high-quality .mp3 files
-   ✅ Built-in GUI (Tkinter) — no need to use the console
-   ✅ Real-time console output inside the app
-   ✅ Can be compiled into a standalone .exe

------------------------------------------------------------------------

🧩 Requirements

-   Python 3.10+
-   The following Python libraries:

    pip install yt-dlp ytmusicapi mutagen tkinter

(Tkinter is usually included with Python on Windows.)

🚀 Run from Source

Clone or download this repository:

    git clone https://github.com/yourusername/ytmusic-downloader-gui.git
    cd ytmusic-downloader-gui

(Optional but recommended) Create a virtual environment:

    python -m venv venv
    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

(Or use the list above.)

Run the app:

    python main.py

🧱 Build a Standalone .exe

To package the app as a standalone Windows executable, use PyInstaller:

Install PyInstaller:

    pip install pyinstaller

Build the app:

    pyinstaller --onefile --noconsole --add-data "venv/Lib/site-packages/ytmusicapi;ytmusicapi" --add-data "venv/Lib/site-packages/yt_dlp;yt_dlp" --name "ytmusic-downloader" main.py

⚠️ On Linux/Mac, replace ; with : in –add-data paths.

Your compiled .exe will appear in:

    dist/ytmusic-downloader.exe

You can now run it directly without Python installed:

    dist/ytmusic-downloader.exe
