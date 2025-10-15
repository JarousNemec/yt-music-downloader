import os
import re
import tkinter as tk
from tkinter import scrolledtext, filedialog
import threading
import sys
import queue
import yt_dlp
from ytmusicapi import YTMusic

from app.ConsoleRedirector import ConsoleRedirector

class App:
    def __init__(self, root):
        self.text_area = None
        self.start_button = None
        self.output_path_button = None
        self.output_path = None
        self.path_label = None
        self.url_entry = None
        self.root = root
        self.root.title("My Playlist Downloader")

        self._init_gui(root)

        self.queue = queue.Queue()
        self.update_output()

        sys.stdout = ConsoleRedirector(self.text_area, self.queue)
        sys.stderr = ConsoleRedirector(self.text_area, self.queue)

    def _init_gui(self, root):
        # URL entry
        url_frame = tk.Frame(root)
        url_frame.pack(padx=10, pady=5, fill="x")
        tk.Label(url_frame, text="Playlist URL:").pack(side="left")
        self.url_entry = tk.Entry(url_frame, width=50)
        self.url_entry.pack(side="left", padx=5, fill="both", expand=True)

        # Output path entry
        output_path_frame = tk.Frame(root)
        output_path_frame.pack(padx=10, pady=5, fill="x")
        output_path_frame_container = tk.Frame(output_path_frame)
        output_path_frame_container.pack(side="left", fill="x")
        self.path_label = tk.Label(output_path_frame_container, text="Output Path: ./songs")
        self.path_label.pack()
        output_path_frame_container_button = tk.Frame(output_path_frame_container)
        output_path_frame_container_button.pack(side="left", fill="x")
        self.output_path = tk.StringVar(value="./songs")
        self.output_path_button = tk.Button(output_path_frame_container_button, text="Browse",
                                            command=self._select_output_folder)
        self.output_path_button.pack()

        # Actions
        actions_frame = tk.Frame(root)
        actions_frame.pack(padx=10, pady=5, fill="x")
        self.start_button = tk.Button(actions_frame, text="Run", command=self.start_task, bg="green", fg="white")
        self.start_button.pack(side="left")
        self.text_area = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled', wrap='none')
        self.text_area.pack(padx=10, pady=50, fill="both", expand=True)

    def _select_output_folder(self):
        folder = filedialog.askdirectory(title="Choose target directory")
        if folder:
            self.output_path.set(folder)
            self.path_label.config(text=f"Output Path: {folder}")

    def start_task(self):
        thread = threading.Thread(target=self.long_running_task)
        thread.daemon = True
        thread.start()

    def long_running_task(self):
        url = self.url_entry.get().strip()
        output_path = self.output_path.get()

        success, playlist_id = self._validate_inputs(url, output_path)
        if not success:
            return

        print("Download started...")
        self._download_playlist(playlist_id, output_path)
        print("✅ Done!")


    def _validate_inputs(self, url, output_path) -> tuple[bool, str]:
        playlist_id = ''
        print("Inputs validation in progress...")
        if not url:
            print("❌ Please enter playlist url.")
            return False, playlist_id
        if output_path and os.path.exists(output_path):
            print("✅ Output path:", output_path)
        else:
            print("❌ Please enter valid output path.")
            return False, playlist_id

        if not self.__is_valid_yt_playlist_url(url):
            print("❌ URL is not a valid YouTube playlist.")
            return False, playlist_id

        match = re.search(r"[?&]list=([A-Za-z0-9_-]+)", url)

        if match:
            playlist_id = match.group(1)
            print("✅ Playlist ID:", playlist_id)
        else:
            print("❌ Playlist ID not found.")
            return False, playlist_id

        print("Inputs are valid!")
        return True, playlist_id

    def _download_yt_mp3(self, url, output_path="."):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
            'noprogress': False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def _download_playlist(self, playlist_id, output_path):
        ytmusic = YTMusic()
        playlist = ytmusic.get_playlist(playlist_id, limit=None)

        print(f"Playlist name: {playlist['title']}")
        print("Songs:")

        for i, track in enumerate(playlist['tracks'], start=1):
            title = track['title']
            artist = track['artists'][0]['name']
            video_id = track['videoId']
            url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"{i}. {title} - {artist}")
            print(f"   {url}")
            self._download_yt_mp3(url, output_path=output_path)

    def __is_valid_yt_playlist_url(self, url: str) -> bool:
        pattern = re.compile(
            r"^(https?://)?(www\.)?"
            r"(youtube\.com|music\.youtube\.com)/playlist\?list="
            r"([A-Za-z0-9_-]+)"
        )
        return bool(pattern.match(url))

    def update_output(self):
        try:
            while True:
                message = self.queue.get_nowait()
                self.text_area.config(state='normal')
                self.text_area.insert(tk.END, message)
                self.text_area.yview(tk.END)
                self.text_area.config(state='disabled')
        except queue.Empty:
            pass
        self.root.after(100, self.update_output)


