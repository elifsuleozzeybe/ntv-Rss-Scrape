import os
import json
import requests
from bs4 import BeautifulSoup

# RSS verilerini çekme fonksiyonu
def fetch_rss_data(rss_url):
    response = requests.get(rss_url)
    if response.status_code == 200:
        return response.text
    return None

# Görsel indirme fonksiyonu
def download_image(image_url, save_path):
    img_data = requests.get(image_url).content
    with open(save_path, 'wb') as handler:
        handler.write(img_data)

# Ana işlev
def process_rss_and_save_images(rss_url):
    # RSS verilerini çek
    rss_data = fetch_rss_data(rss_url)
    
    if rss_data:
        # BeautifulSoup ile RSS verisini parse et
        soup = BeautifulSoup(rss_data, 'lxml')  # 'lxml' parser kullanıldı
        items = soup.find_all('item')
        
        # Data ve Images dizinlerini oluştur
        data_directory = 'data'
        images_directory = 'images'
        os.makedirs(data_directory, exist_ok=True)
        os.makedirs(images_directory, exist_ok=True)
        
        for item in items:
            title = item.title.text.strip()  # Başlığı al ve boşlukları temizle
            link = item.link.text
            
            # JSON formatında veriyi kaydet
            json_file_path = os.path.join(data_directory, f"{link.split('/')[-1]}.json")
            with open(json_file_path, 'w') as json_file:
                json.dump({'title': title, 'link': link}, json_file)
            
            # Başlık için geçerli bir klasör adı oluştur
            folder_name = title.replace(" ", "_").replace("/", "_")  # Klasör adında geçersiz karakterleri temizle
            folder_path = os.path.join(images_directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            
            # İçerik sayfasından görselleri çek
            content_response = requests.get(link)
            content_soup = BeautifulSoup(content_response.text, 'lxml')
            images = content_soup.find_all('img')

            # Görselleri kaydet
            image_list = []
            for img in images:
                img_url = img['src']
                if img_url.startswith('http'):
                    img_filename = f"{folder_name}.jpg"  # Görsel dosya adı
                    img_save_path = os.path.join(folder_path, img_filename)
                    download_image(img_url, img_save_path)
                    image_list.append(img_filename)
            
            # Görsel listesini JSON dosyasına ekle
            with open(json_file_path, 'r+') as json_file:
                data = json.load(json_file)
                data['images'] = image_list
                json_file.seek(0)
                json.dump(data, json_file)
                json_file.truncate()

# Örnek kullanım
rss_url = 'https://www.ntv.com.tr/son-dakika.rss'  # Geçerli bir RSS URL'si girin
process_rss_and_save_images(rss_url)
