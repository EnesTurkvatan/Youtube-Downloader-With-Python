import click
import yt_dlp
from pathlib import Path
from tqdm import tqdm
import sys

# İlerleme çubuğu için hook
def progress_hook(d):
    if d['status'] == 'downloading':
        p = d.get('_percent_str', '0%').replace('%', '')
        try:
            tqdm.write(f"İndiriliyor: {p}%")
        except:
            pass
    elif d['status'] == 'finished':
        tqdm.write("İndirme tamamlandı, dosya işleniyor...")

# Video veya playlist bilgilerini çekme
def get_video_info(url):
    ydl_opts = {'quiet': True, 'no_warnings': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:  # Playlist
                return info['entries']
            return [info]  # Tek video
    except Exception as e:
        click.echo(f"Hata: Geçerli bir YouTube linki girin. ({e})")
        sys.exit(1)

# Mevcut formatları listeleme (kullanıcıya bilgi)
def list_formats(url):
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        available_formats = []
        for f in formats:
            ext = f.get('ext')
            resolution = f.get('resolution', 'Audio only')
            bitrate = f.get('abr', 'N/A')
            format_id = f.get('format_id')
            if ext in ['mp4', 'avi', 'mp3', 'aac', 'wav']:  # Desteklenen formatlar
                available_formats.append({
                    'format_id': format_id,
                    'ext': ext,
                    'resolution': resolution,
                    'bitrate': bitrate
                })
        return available_formats

# Dosya indirme fonksiyonu
def download_file(url, format_id, output_path, file_format, quality):
    ydl_opts = {
        'format': format_id,
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'quiet': True,
        'no_warnings': True,
    }
    
    # Ses formatları için FFmpeg postprocessor
    if file_format in ['mp3', 'aac', 'wav']:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': file_format,
            'preferredquality': quality,  # Ör. 192kbps
        }]
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        click.echo(f"Dosya kaydedildi: {output_path}")
    except Exception as e:
        click.echo(f"İndirme hatası: {e}")

# Çıkış yolunu alma
def get_output_path():
    default_path = Path.home() / "Downloads" / "YT_Downloads"
    default_path.mkdir(parents=True, exist_ok=True)
    user_path = click.prompt(f"Kayıt yeri (varsayılan: {default_path})", default=default_path, show_default=False)
    output_path = Path(user_path)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path

# Ana CLI fonksiyonu
@click.command()
@click.option('--url', prompt='Video/Playlist URL', help='YouTube video veya playlist linki')
@click.option('--format', prompt='Format (mp3, mp4, aac, wav, avi)', help='Dosya formatı')
@click.option('--quality', prompt='Kalite (ör. 720p, 480p, 192kbps, 128kbps)', help='Dosya kalitesi')
def main(url, format, quality):
    # Desteklenen formatları kontrol et
    supported_formats = ['mp3', 'mp4', 'aac', 'wav', 'avi']
    if format not in supported_formats:
        click.echo(f"Hata: Desteklenen formatlar: {supported_formats}")
        return

    # Çıkış yolunu al
    output_path = get_output_path()

    # Video/playlist bilgilerini çek
    videos = get_video_info(url)
    
    for video in videos:
        click.echo(f"İşleniyor: {video['title']}")
        
        # Mevcut formatları al
        available_formats = list_formats(video['webpage_url'])
        
        # Kullanıcı kalitesine uygun format ID'yi bul
        selected_format_id = None
        for f in available_formats:
            if f['ext'] == format and (quality in f['resolution'] or quality in str(f['bitrate'])):
                selected_format_id = f['format_id']
                break
        
        if not selected_format_id:
            click.echo(f"Hata: {quality} kalitesinde {format} formatı bulunamadı.")
            continue
        
        # Dosyayı indir
        download_file(video['webpage_url'], selected_format_id, output_path, format, quality)

if __name__ == '__main__':
    main()
