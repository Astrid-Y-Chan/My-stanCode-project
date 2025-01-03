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
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
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
        tokens = tags[0].text.split()  # Only one <tbody> tag in the HTML

        male_num = 0
        female_num = 0

        # Data order: Rank / Male name / Male number / Female name / Female number (Only the top 200 names are shown)
        for i in range(5 * 200):
            if i % 5 == 2:  # Male number (index 2)
                male_num += int(''.join(tokens[i].split(',')))  # Remove commas and convert to integer
            elif i % 5 == 4:  # Female number (index 4)
                female_num += int(''.join(tokens[i].split(',')))

        # Print the result
        print(f'Male Number: {male_num}')
        print(f'Female Number: {female_num}')


if __name__ == '__main__':
    main()
