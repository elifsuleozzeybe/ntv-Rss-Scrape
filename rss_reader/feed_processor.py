from bs4 import BeautifulSoup

class FeedProcessor:
    def __init__(self):
        pass

    def process_entry(self, entry):
        # Başlık, bağlantı ve içerik gibi temel bilgileri al
        title = entry.title
        link = entry.link
        
        # content'in bir liste olabileceğini göz önünde bulunduruyoruz, ilk elemanı alıyoruz
        content = entry.content[0].value if isinstance(entry.content, list) else entry.content
        
        images = self.extract_images(content)  # Görselleri çıkart
        
        return {
            'title': title,
            'link': link,
            'images': images,
            'content': content
        }
    
    def extract_images(self, content):
        # İçerikten img linklerini çıkartacak bir yöntem
        soup = BeautifulSoup(content, 'html.parser')
        img_tags = soup.find_all('img')
        return [img['src'] for img in img_tags if 'src' in img.attrs]
