import requests, json, os, datetime as dt

url = 'https://prod-noticeindex.bluearchiveyostar.com/prod/index.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

rs = requests.get(url, headers=headers, timeout=30)
rs.raise_for_status()

date_str = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_path  = f'data/{date_str}.json'

os.makedirs('data', exist_ok=True)
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(rs.json(), f, ensure_ascii=False, indent=2)

print(f'saved -> {file_path}')