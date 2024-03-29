import pandas as pd
import uuid
import requests
from bs4 import BeautifulSoup

# team = 'houston_2'

def simple_web_scraper(url):
    response = requests.get(url)
    count = 1
    if response.status_code == 200:
        df = pd.DataFrame()
        soup = BeautifulSoup(response.text, 'html.parser')
        r = soup.find_all("td", class_="hide-on-large text-center")
        sum = 1000
        my = [0]
        opp = [0]
        for i in r:
            x = i.text.strip()
            if '-' in x:
                x = x.split('-')
                if int(x[0]) + int(x[1]) < sum:
                    if len(my) > 2:
                        df['my_score'] = my
                        df['opponent_score'] = opp
                        if my[-1] > opp[-1]:
                            df['win'] = True
                        else:
                            df['win'] = False
                        random_filename = str(uuid.uuid4())[:8] + '.csv'
                        # random_filename = team + str('_') + str(count) + '.csv'
                        df.to_csv(random_filename, index=False)
                        df = pd.DataFrame()
                        count += 1
                        my = [0]
                        opp = [0]
                my.append(int(x[0]))
                opp.append(int(x[1]))
                sum = int(x[0]) + int(x[1])
            
        df['my_score'] = my
        df['opponent_score'] = opp
        if my[-1] > opp[-1]:
            df['win'] = True
        else:
            df['win'] = False
        random_filename = str(uuid.uuid4())[:8] + '.csv'
        # random_filename = team + str('_') + str(count) + '.csv'
        df.to_csv(random_filename, index=False)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
if __name__ == "__main__":
    
    url_list = ['https://bupilots.com/sports/mens-volleyball/stats/2022-23/lawrence-tech-mich-/boxscore/7483',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/siena-heights-mich-/boxscore/7484',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/mount-vernon-nazarene-ohio-/boxscore/7548',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/mount-vernon-nazarene-ohio-/boxscore/7485',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/lourdes-ohio-/boxscore/7486',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/olivet-nazarene-university-ill-/boxscore/7549',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/trinity-international-university-ill-/boxscore/7846',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/goshen-ind-/boxscore/7487',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/aquinas-mich-/boxscore/7488',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/cornerstone-mich-/boxscore/7489',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/indiana-tech/boxscore/7550',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/indiana-tech/boxscore/7490',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/trinity-christian-ill-/boxscore/7551',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/trine-ind-/boxscore/7552',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/aquinas-mich-/boxscore/7492',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/cornerstone-mich-/boxscore/7493',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/goshen-ind-/boxscore/7553',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/adrian-college/boxscore/7554',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/trinity-christian-ill-/boxscore/7555',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/lourdes-ohio-/boxscore/7496',
                'https://bupilots.com/sports/mens-volleyball/stats/2022-23/siena-heights-mich-/boxscore/7498',
                ]
    
    # url_list = ["https://cctigers.com/sports/womens-volleyball/stats/2023/augustana-college/boxscore/9412"]
    for url in url_list:
        simple_web_scraper(url)
    
    
    # page = requests.get(url)
    # # Check if the request was successful (status code 200)
    # if page.status_code == 200:
    #     # Open a file in write mode and write the content of the page
    #     with open('output.txt', 'w', encoding='utf-8') as file:
    #         file.write(page.text)
    #     print('Page content written to output.txt')
    # else:
    #     print(f'Error: Failed to retrieve the page. Status code: {page.status_code}')


    