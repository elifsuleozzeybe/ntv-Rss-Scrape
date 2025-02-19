import os
import json

class FileManager:
    def __init__(self, rss_url):
        self.rss_url = rss_url

    def get_rss_filename(self):
        return self.rss_url.split('/')[-1].replace('.rss', '.json')

    def get_folder_name(self, filename):
        return filename.replace('.json', '')

    def save_feed(self, folder_name, filename, entries):
        os.makedirs(folder_name, exist_ok=True)
        file_path = os.path.join(folder_name, filename)

        with open(file_path, 'w') as f:
            json.dump(entries, f, indent=4)

        self.save_images(entries)  # Görselleri kaydet

        return file_path

    def save_images(self, entries):
        # Görselleri başlıklarla birlikte JSON formatında kaydedelim
        images_data = []
        for entry in entries:
            title = entry['title']
            for img_url in entry['images']:
                images_data.append({'title': title, 'image_url': img_url})

        # Görselleri ayrı bir JSON dosyasına kaydet
        images_file_path = 'images_data.json'
        with open(images_file_path, 'w') as img_file:
            json.dump(images_data, img_file, indent=4)
