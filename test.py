from boilerpipe.extract import Extractor
import requests
url = 'https://www.theverge.com/2018/5/31/17377964/coca-cola-water-sustainability-recycling-controversy-investigation'
headers = {
    'User-agent': 'AppleTV6,2/11.1'
}
response = requests.get(url, headers=headers)
html_str = response.text
extractor = Extractor(html=html_str, extractor='ArticleExtractor')
print(extractor.get_html())
print(extractor.get_text())