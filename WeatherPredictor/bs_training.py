from bs4 import BeautifulSoup
import requests as req

request = req.get('https://python-scripts.com/pathlib')
assert request.status_code == 200, f'{request.status_code}'

soup = BeautifulSoup(request.text, 'lxml')
print(soup.prettify(), end='\n\n')

print(*[i.getText() for i in soup.select('div.entry-content > h2')], sep='\n')
