import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup


class Animal:
    def getData(self, link):
        global df
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        data = soup.findAll(attrs={'class': 'trackLink'})

        finalResult = list()
        list1 = list()
        list2 = list()
        list3 = list()

        # get name
        for para in soup.findAll(attrs={'class': 'trackLink'}):
            if para.text != "":
                list1.append(para.text)
        # get image link
        for para in soup.find_all('img', 'card-image'):
                list2.append(para['src'])
        # get fact
        for para in soup.findAll(attrs={'class': 'card-fun-fact'}):
                list3.append(para.text)

        #add data on single map
        for i in range(len(list1)):
            finalResult.append({
                "id": i,
                'name': list1[i],
                'link': list2[i],
                'fun-fact': list3[i],

            },
            )
        print(finalResult[0])
        df = pd.DataFrame(finalResult)

        df.to_csv('animal_data.csv', mode='a', index=False, header=False)


url = "https://a-z-animals.com/animals/scientific"
animal = Animal()
animal.getData(url)
