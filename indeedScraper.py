#! python3
# Used to scrape Indeed for latest job postings
import requests, bs4

url = 'https://www.indeed.com/jobs?as_and=technical+support&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=15&l=Oakland+County%2C+MI&fromage=7&limit=20&sort=date&psf=advsrch&from=advancedsearch'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
jobCard = soup.select('.result')  # Each Job posting 'card' in Indeed search
pageDirectory = soup.select('.pagination a')
for i in len(range(pageDirectory)):  # Trying to get the next page's link of results
    print(pageDirectory[i].get('href'))

'''
for job in range(len(jobCard)):
    jobTitle = jobCard[job].select('.title')  # Title of position
    jobPosted = jobCard[job].select('.date')  # Date position was posted
    jobLocation = jobCard[job].select('.location')  # City job is located in
    for i in range(len(jobTitle)):
        print(jobTitle[0].text.strip(),end=': ')
        print(jobPosted[0].text.strip(),end=': ')
        print(jobLocation[0].text.strip())
'''
