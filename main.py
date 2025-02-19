from rss_reader.rss_fetcher import RSSFetcher
from rss_reader.feed_processor import FeedProcessor
from rss_reader.file_manager import FileManager

rss_urls = [
    'https://www.ntv.com.tr/son-dakika.rss',
    'https://www.ntv.com.tr/gundem.rss',
    'https://www.ntv.com.tr/ekonomi.rss',
    'https://www.ntv.com.tr/spor.rss',
    'https://www.ntv.com.tr/sanat.rss',
    'https://www.ntv.com.tr/saglik.rss',
    'https://www.ntv.com.tr/seyahat.rss',
    'https://www.ntv.com.tr/foto-galeri.rss',
    'https://www.ntv.com.tr/video-galeri.rss',
    'https://www.ntv.com.tr/turkiye.rss',
    'https://www.ntv.com.tr/egitim.rss',
    'https://www.ntv.com.tr/ntvpara.rss',
    'https://www.ntv.com.tr/n-life.rss',
    'https://www.ntv.com.tr/dunya.rss',
    'https://www.ntv.com.tr/yasam.rss',
    'https://www.ntv.com.tr/spor-skor.rss',
    'https://www.ntv.com.tr/teknoloji.rss',
    'https://www.ntv.com.tr/otomobil.rss'

]

for rss_url in rss_urls:
    fetcher = RSSFetcher(rss_url)  # RSS verisini çek
    feed = fetcher.fetch()

    processor = FeedProcessor()  # Veriyi işle
    processed_entries = [processor.process_entry(entry) for entry in feed.entries]

    manager = FileManager(rss_url)  # Dosyayı kaydet
    rss_filename = manager.get_rss_filename()
    folder_name = manager.get_folder_name(rss_filename)
    file_path = manager.save_feed(folder_name, rss_filename, processed_entries)

    print(f"Veriler {file_path} dosyasına başarıyla yazıldı.")
