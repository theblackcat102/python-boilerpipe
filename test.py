from boilerpipe.extract import Extractor
import requests
from tqdm import tqdm
url = 'https://www.theverge.com/2018/5/31/17377964/coca-cola-water-sustainability-recycling-controversy-investigation'
headers = {
    'User-agent': 'AppleTV6,2/11.1'
}
response = requests.get(url, headers=headers)
html_str = response.text

print('ArticleExtractor performance')
for i in tqdm(range(2000)):
    extractor = Extractor(html=html_str, extractor='ArticleExtractor')
    html_result = extractor.get_html()
    html_text = extractor.get_text()

print('DefaultExtractor performance')
for i in tqdm(range(2000)):
    extractor = Extractor(html=html_str, extractor='DefaultExtractor')
    html_result = extractor.get_html()
    html_text = extractor.get_text()

print('ArticleSentencesExtractor performance')
for i in tqdm(range(2000)):
    extractor = Extractor(html=html_str, extractor='ArticleSentencesExtractor')
    html_result = extractor.get_html()
    html_text = extractor.get_text()

print('LargestContentExtractor performance')
for i in tqdm(range(2000)):
    extractor = Extractor(html=html_str, extractor='LargestContentExtractor')
    html_result = extractor.get_html()
    html_text = extractor.get_text()