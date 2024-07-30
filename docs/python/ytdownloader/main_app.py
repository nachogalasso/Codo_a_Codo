# YOTUBE DOWNLOADER with PYTUBE and STREAMLIT

import pytube
from pytube import YouTube
import streamlit as st
import os

class YouTubeDownloader:
    def __init__(self, url):
        self.url = url
        try:
            self.youtube = pytube.YouTube(self.url, on_progress_callback=YouTubeDownloader.onProgress)
            self.stream = None
        except pytube.exceptions.PytubeError as e:
            st.error(f"Error al procesar el video: {str(e)}")
        except Exception as e:
            st.error(f"Un error inesperado ocurrió: {str(e)}")
        self.youtube = pytube.YouTube(self.url, on_progress_callback=YouTubeDownloader.onProgress)
        self.stream = None
        
    # Creamos una function para el título
    def showTitle(self):
        st.write(f"**Título:** {self.youtube.title}")
        self.showStreams()
        
    
    # Ahora veremos los tipos de formatos a descargar
    def showStreams(self):
        streams = self.youtube.streams
        stream_options = [
            f"Resolución: {stream.resolution or 'N/A'} / FPS: {getattr(stream, 'fps', 'N/A')} / Tipo: {stream.mime_type}" for stream in streams
        ]
        choice = st.selectbox("Elije una opción de stream:", stream_options)
        self.stream = streams[stream_options.index(choice)]
        
    
    # Traemos el tamaño del archivo
    def getFileSize(self):
        file_size = self.stream.filesize / 1000000
        return file_size
    
        
    # Seleccionar dónde lo queremos almacenar
    def getPermissionToContinue(self, file_size):
        st.write(f"*Título:** {self.youtube.title}")
        st.write(f"*Autor:** {self.youtube.author}")
        st.write(f"*Size:** {file_size:.2f} MB")
        st.write(f"*Resolution:** {self.stream.resolution or 'N/A'} ")
        st.write(f"*FPS:** {getattr(self.stream, 'fps', 'N/A')}")
        
        download_folder = st.text_input('Save to:')
        
        if download_folder:
            self.download_folder = download_folder
            
        if st.button("Download"):
            self.download()
            
    def download(self):
        if not os.path.isdir(self.download_folder):
            st.error("Invalid download folder")
            return
        
        self.stream.download(output_path = self.download_folder)
        st.success('Download Complete!')
            
    # Progress Bar
    @staticmethod
    def onProgress(stream = None, chuck = None, remaining = None):
        file_size = stream.filesize / 1000000
        filedownloaded = file_size - (remaining / 1000000)
        st.progress(filedownloaded / file_size)
        
        
if __name__ == "__main__":
    st.title("YouTube Video Downloader")
    url = st.text_input("Insert or Paste video url:")
    
    if url:
        # downloader = YouTubeDownloader(url)
        downloader = YouTube(url)
        downloader.showTitle()
        if downloader.stream:
            file_size = downloader.getFileSize()
            downloader.getPermissionToContinue(file_size)