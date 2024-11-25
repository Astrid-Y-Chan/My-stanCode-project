"""
File: webcrawler.py
Name: Astrid Chen
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all('tbody')
        for tag in tags:
            tag = tag.text
            tokens = tag.split()
            male_list = []
            female_list = []
            # data order -> rank/ male_name/ male_number/ female_name/ female_number (only shows top 200)
            for i in range(1000):
                if i % 5 == 2:
                    male_list.append(tokens[i])
                elif i % 5 == 4:
                    female_list.append(tokens[i])

            print(f"Male Number: {calculation(male_list)}")
            print(f"Female Number: {calculation(female_list)}")


def calculation(number_list):
    number_sum = 0
    for number in number_list:
        ans = ''
        for ch in number:
            if ch.isdigit():
                ans += ch
        number_sum += int(ans)
    return number_sum


if __name__ == '__main__':
    main()
