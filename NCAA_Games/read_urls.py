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
    
    url_list = ['https://athletics.apu.edu/sports/womens-volleyball/stats/2021/simon-fraser/boxscore/15559',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/regis/boxscore/15562',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/cal-state-los-angeles/boxscore/15563',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/cal-state-san-bernardino/boxscore/15564',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/northwest-nazarene/boxscore/15565',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/stanislaus-state/boxscore/15566',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/cal-state-san-marcos/boxscore/15567',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/westminster/boxscore/15568',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/academy-of-art/boxscore/15238',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/fresno-pacific/boxscore/15239',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/holy-names/boxscore/15240',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/dominican/boxscore/15241',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/concordia/boxscore/15242',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/biola/boxscore/15243',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/academy-of-art/boxscore/15245',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/fresno-pacific/boxscore/15244',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/point-loma/boxscore/15408',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/dominican/boxscore/15246',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/holy-names/boxscore/15247',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/point-loma/boxscore/15251',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/chaminade/boxscore/15250',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/hawaii-pacific/boxscore/15248',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/chaminade/boxscore/15252',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/hawai-i-hilo/boxscore/15249',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/hawai-i-hilo/boxscore/15254',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/biola/boxscore/15255',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2021/concordia/boxscore/15410',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/rollins/boxscore/18681',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/texas-am-international/boxscore/18682',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/northwest-nazarene/boxscore/18684',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/emory-henry/boxscore/18683',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/west-florida/boxscore/18744',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/wayne-state/boxscore/18745',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/central-missouri/boxscore/18837',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/lewis/boxscore/18836',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/biola/boxscore/18685',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/cal-poly-pomona/boxscore/18746',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/dominican/boxscore/18686',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/holy-names/boxscore/18687',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/concordia/boxscore/18688',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/hawai-i-hilo/boxscore/18689',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/hawaii-pacific/boxscore/18690',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/chaminade/boxscore/18691',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/holy-names/boxscore/18692',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/dominican/boxscore/18693',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/academy-of-art/boxscore/18694',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/biola/boxscore/18697',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/fresno-pacific/boxscore/18698',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/hawai-i-hilo/boxscore/18699',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/chaminade/boxscore/18700',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/hawaii-pacific/boxscore/18701',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/academy-of-art/boxscore/18702',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/concordia/boxscore/18703',
                'https://athletics.apu.edu/sports/womens-volleyball/stats/2022/point-loma/boxscore/18704',
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


    