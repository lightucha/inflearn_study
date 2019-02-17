from urllib.parse import urljoin

# 절대경로 and 상대경로
baseUrl = "http://test.com/html/a.html"
print('>>', urljoin(baseUrl, 'b.html')) # >> http://test.com/html/b.html
print('>>', urljoin(baseUrl, 'sub/b.html')) # >> http://test.com/html/sub/b.html
print('>>', urljoin(baseUrl, '../index.html')) # >> http://test.com/index.html
print('>>', urljoin(baseUrl, '../img/img.jpg')) # >> http://test.com/img/img.jpg
print('>>', urljoin(baseUrl, '../css/img.css')) # >> http://test.com/css/img.css
