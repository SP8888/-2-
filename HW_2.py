from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

url = 'https://hh.ru/search/vacancy'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


zapros = input('Введите требуемую професию (если несколько слов, то вводите через +) - ')
i = 0
response = requests.get(f'{url}?clusters=true&enable_snippets=true&search_field=name&text={zapros}&L_save_area=true&area=113&from=cluster_area&showClusters=true&page={i}', headers=headers)
soup = bs(response.text,'html.parser')
vacancy_list = soup.find_all('div',{'class':'vacancy-serp-item'})

vacancy = []
while len(vacancy_list) != 0:
    response = requests.get(f'{url}?clusters=true&enable_snippets=true&search_field=name&text={zapros}&L_save_area=true&area=113&from=cluster_area&showClusters=true&page={i}', headers=headers)
    soup = bs(response.text,'html.parser')
    vacancy_list = soup.find_all('div',{'class':'vacancy-serp-item'})

    for vac in vacancy_list:

            vac_data={}
            vac_link = url + vac.find('a', class_='bloko-link HH-LinkModifier').get('href')
            vac_name = vac.find('div',{'class':'g-user-content'}).getText()
            vac_site = url
            vac_zp = vac.find('div',{'class':'vacancy-serp-item__sidebar'}).getText()
            vac_data['name'] = vac_name
            vac_data['link'] = vac_link
            vac_data['site'] = vac_site
            vac_data['zp'] = vac_zp
            vacancy.append(vac_data)

    i = i + 1
    response = requests.get(f'{url}?clusters=true&enable_snippets=true&search_field=name&text={zapros}&L_save_area=true&area=113&from=cluster_area&showClusters=true&page={i}',headers=headers)
    soup = bs(response.text, 'html.parser')
    vacancy_list = soup.find_all('div', {'class': 'vacancy-serp-item'})

pprint(vacancy)


