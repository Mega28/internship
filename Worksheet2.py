Q.1. Write a python program to display all the header tags from 'en.wikipedia.org/wiki/Main_Page'?
Ans:
from bs4 import BeautifulSoup
import requests
req = requests.get('https://en.wikipedia.org/wiki/Main_Page')
Soup = BeautifulSoup(html.content)
titles = Soup.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List of header tags :', *titles, sep='\n\n')

Q.2. Write a python program to display IMDB's top rated 100 movies data(i.e. Name,IMDB rating,Year of release)?
Ans:
from bs4 import BeautifulSoup
import requests
import pandas as pd
#to collect the english translation of datas
headers={'Accept-Language':'en-US,en;q=0.5'}
#data of 50 movies in each page,hence each request fetches 50 movies data making it a total of 100 movies.
request=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc',headers=headers)
request1=requests.get('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt',headers=headers)
Soup=BeautifulSoup(request.content)
Soup1=BeautifulSoup(request1.content)
#append data of both Soup and Soup1
Soup.append(Soup1)
MoviesName=[]
Year=[]
Rating=[]
movies=Soup.find_all("div",class_='lister-item mode-advanced')
for m in movies:
    name=m.h3.a.text
    year=m.h3.find('span',class_='lister-item-year text-muted unbold').text
    rate=m.strong.text
    MoviesName.append(name)
    Year.append(year)
    Rating.append(rate)
Movies=pd.DataFrame({'Movie':MoviesName,'Year of Release':Year,'Rating':Rating},index=range(1,101))
Movies.head(20)

Q.3. Write a python program to display IMDB's top rated 100 Indian movies data(i.e. Name,IMDB rating,Year of release)?
Ans:
from bs4 import BeautifulSoup
import requests
import pandas as pd
req=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
Soup=BeautifulSoup(req.content)
movs=Soup.find_all('td',class_='titleColumn')
movs100=movs[0:100]
Mname=[]
Year=[]
for m in movs100:
    name=m.a.text
    year=m.span.text
    Mname.append(name)
    Year.append(year)
rate=Soup.find_all('td',class_='ratingColumn imdbRating')
rate100=rate[0:100]
IMDB=[]
for r in rate100:
    imdb=r.strong.text
    IMDB.append(imdb)
INDTOP=pd.DataFrame({'Name':Mname,'Year of Release':Year,'Rating':IMDB},index=range(1,101))
INDTOP

Q.4. Write a python program to scrap book name, author name, genre and book review of any 5 books from 'www.bookpage.coom'?
Ans:
from bs4 import BeautifulSoup
import requests
import pandas as pd
request=requests.get('https://bookpage.com/')
soup=BeautifulSoup(request.content)
dv=soup.find_all('div',class_='content')
Book={'Name':[],'Review':[],'Genre':[],'Author_Name':[]}
for i in dv:
    nam=i.find('h4',class_='italic').text.replace('\n','').replace(' ★ ','')
    rev=i.find('p',class_='excerpt').text.replace('\n','')
    Gen=i.find('p',class_='genre-links hidden-phone').text.replace('/',',').replace('\n','')
    Auth=i.find('p',class_='sans bold').text.replace('\n','').replace('Interview by','').replace('Feature by','').replace('Review by','')
    Book['Name'].append(nam)
    Book['Review'].append(rev)
    Book['Genre'].append(Gen)
    Book['Author_Name'].append(Auth)
Books=pd.DataFrame(Book,index=range(1,7))
Books

Q.5 Write a python program to scrape cricket rankings from 'www.icc-cricket.com'You have to scrape:
i) Top 10 ODI teams in men cricket along with the records for matches,points and rating.
ii) Top 10 ODI batsman in men along with records of their team and rating.
iii) Top 10 ODI bowlers along with records of their team and rating.
Ans:
i)
from bs4 import BeautifulSoup
import requests
import pandas as pd
info=requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
soup=BeautifulSoup(info.content)
team=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=team[0:10]
data = {'Team_Name':[],'Matches': [],'Points': [],'Rating':[]}
for i in top10:
    pnt=i.find_all('td',recursive=True)
    data['Team_Name'].append(i.find('span',class_='u-hide-phablet').text)
    data['Matches'].append(pnt[2].text)
    data['Points'].append(pnt[3].text)
    data['Rating'].append(pnt[4].text.replace('\n',''))
MenTeam=pd.DataFrame(data,index=range(1,11))
MenTeam

ii)
req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}
for i in Top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
ODIBATSMAN=pd.DataFrame(data,index=range(1,11))
ODIBATSMAN

iii)
req=requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup=BeautifulSoup(req.content)
bowler=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
Top10=bowler[0:10]
bdata={'Player_Name':[],'Team_Name': [], 'Rating':[]}
for i in Top10:
    bat=i.find_all('td',recursive=True)
    bdata['Player_Name'].append(bat[1].text.replace('\n',''))
    bdata['Team_Name'].append(bat[2].text.replace('\n',''))
    bdata['Rating'].append(bat[3].text.replace('\n',''))
ODIBOWL=pd.DataFrame(bdata,index=range(1,11))
ODIBOWL


Q.6 Write a python program to scrape cricket rankings from 'www.icc-cricket.com'You have to scrape:
i) Top 10 ODI teams in women cricket along with the records for matches,points and rating.
ii) Top 10 ODI players in women along with records of their team and rating.
iii) Top 10 ODI women's all rounder along with records of their team and rating.
Ans:
i)
from bs4 import BeautifulSoup
import requests
import pandas as pd
req=requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
soup=BeautifulSoup(req.content)
team=soup.find_all('tr',class_=('rankings-block__banner','table-body'))
top10=team[0:10]
data = {'Team_Name':[],'Matches': [],'Points': [],'Rating':[]}

for i in top10:
    pnt=i.find_all('td',recursive=True)
    data['Team_Name'].append(i.find('span',class_='u-hide-phablet').text)
    data['Matches'].append(pnt[2].text)
    data['Points'].append(pnt[3].text)
    data['Rating'].append(pnt[4].text.strip().replace('\n',''))
WomenTeam=pd.DataFrame(data,index=range(1,11))
WomenTeam

ii)
req=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))

top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}

for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
BATW=pd.DataFrame(data,index=range(1,11))  
BATW

iii)
req=requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')
soup=BeautifulSoup(req.content)
player=soup.find_all('tr',class_=('rankings-block__banner','table-body'))

top10=player[0:10]
data={'Player_Name':[],'Team_Name': [], 'Rating':[]}

for i in top10:
    bat=i.find_all('td',recursive=True)
    data['Player_Name'].append(bat[1].text.replace('\n',''))
    data['Team_Name'].append(bat[2].text.replace('\n',''))
    data['Rating'].append(bat[3].text.replace('\n',''))
W_All=pd.DataFrame(data,index=range(1,11))
W_All

Q.7. Write a python program to scrape details of all the mobile phones under rs.20000 liste on amazon.in.The scraped data should include product name,price,image url and average rating.
Ans:
from bs4 import BeautifulSoup
import requests
import pandas as pd
req=requests.get('https://www.amazon.in/s?k=mobile+phones+under+20000&qid=1632977285&ref=sr_pg_1')
soup=BeautifulSoup(req.content)
PH=soup.find_all('div',class_='a-section a-spacing-none',recursion=False)

Name1={'Name':[],'Price':[],'Rating(out of 5 stars)':[],'Image_URL':[]}
for i in PH:
    nam=i.find_all('h2',class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2',recursive=False)
    for p in nam:
        nm=p.a.find('span',class_='a-size-medium a-color-base a-text-normal').text.split('|',3)[0]
        Name1['Name'].append(nm)
    prc=i.find_all('div',class_='a-row a-size-base a-color-base')
    for j in prc:
        pr=j.find('span',class_='a-price-whole').text
        Name1['Price'].append(pr)
    Rtng=i.find_all('div',class_='a-row a-size-small')
    for e in Rtng:
        rt=e.find('span').text.replace("out of 5 stars ",'')
        Name1['Rating(out of 5 stars)'].append(rt)
    Img=i.find_all('div',class_='a-section aok-relative s-image-fixed-height')
    for L in Img:
        im=L.find('img',class_='s-image')
        Name1['Image_URL'].append(im.get('src'))
Mob=pd.DataFrame(Name1,index=range(1,17))
Mob

Q.8.Write a python program to extract information the National Weather Service website of USA , https://www.weather.gov/ for the city San Francisco.You need to extract data about 7 days extended forecast display for the city.The data should include period,short description,temperature and description?
Ans:
from bs4 import BeautifulSoup
import requests
import pandas as pd
get=requests.get('https://forecast.weather.gov/MapClick.php?CityName=San+Francisco&state=CA&site=MTR&textField1=37.775&textField2=-122.418&e=0#.YVbtQJpBzb2')
soup=BeautifulSoup(get.content)
dt=soup.find_all('div',class_='col-sm-10 forecast-text')
cast=[]
for i in dt:
    cast.append(i.text)
det=cast[0:9]   

prd=soup.find_all('div',class_='col-sm-2 forecast-label')
per=[]
for p in prd:
    per.append(p.text)
perd=per[0:9]

tp=soup.find_all('div',class_='tombstone-container')
tmp=[]
srt=[]
for m in tp:
    cv=m.find('p',class_=('temp temp-low','temp temp-high')).text
    tmp.append(cv)
    sd=m.find('p',class_='short-desc').text
    srt.append(sd)
    
Weather=pd.DataFrame({},index=range(1,10))
Weather['Period']=perd
Weather['Short Description']=srt
Weather['Temperature']=tmp
Weather['Details']=det
Weather


Q.9. Write a python program to scrape fresher job listings from 'https://internshala.com/'.It should include job title,company name,CTC and apply date.
Ans:
from bs4 import BeautifulSoup
import requests
import pandas as pd
page=requests.get('https://internshala.com/fresher-jobs')
soup=BeautifulSoup(page.content)
sal=soup.find_all("div",class_='internship_other_details_container')
titles=soup.find_all("div",class_='heading_4_5 profile')
companies=soup.find_all("a",class_='link_display_like_text')
lc=soup.find_all('p',id='location_names')
job_titles=[]
for i in titles:
    job_titles.append(i.text.strip())
len(job_titles)
CTC=[]
CTC1=[]
for k in sal:
    S=k.find('div',class_='other_detail_item_row',recursive=False)
    CTC1.append(S)
    for q in CTC1:
        d=q.find('div',class_='item_body',id=False).text.replace('\n','').replace('                ','').replace('LPA','')
    CTC.append(d)
len(CTC)

company_names=[]
for i in companies:
    company_names.append(i.text.strip())
    
loc=[]
for t in lc:
    z=t.a.text
    loc.append(z)
    
jobs=pd.DataFrame({},index=range(1,41))
jobs['Job_Title']=job_titles
jobs['Company']=company_names
jobs['Location']=loc
jobs['Salary in LPA']=CTC
jobs

Q.10. Write a python program to scrape house details from 'https://www.nobroker.in/ for any location.It should include house title,location,area,emi and price?
Ans:
req=requests.get('https://www.nobroker.in/property/sale/bangalore/Whitefield?searchParam=W3sibGF0IjoxMi45Njk4MTk2LCJsb24iOjc3Ljc0OTk3MjEsInBsYWNlSWQiOiJDaElKZ193TlhmTVJyanNSLVJVQjJCS2x6ekEiLCJwbGFjZU5hbWUiOiJXaGl0ZWZpZWxkIn1d&radius=2.0&type=BHK2')
soup=BeautifulSoup(req.content)

nam=soup.find_all('h2',class_='heading-6 font-semi-bold nb__1AShY')
name=[]
for i in nam:
    q=i.find('span').text
    name.append(q)

l_c=soup.find_all('div',class_='nb__35Ol7')
addr=[]
for l in l_c:
    y=l.text.replace('Explore Nearby','')
    addr.append(y)

em=soup.find_all('div',class_='nb__17R6o')
epi=[]
ar=[]
for y in em:
    r=y.find('div',class_="font-semi-bold heading-6",id="roomType").text.replace('/Month','')
    epi.append(r)
    v=y.find('div',class_='font-semi-bold heading-6',recursive=True).text
    ar.append(v)


er=soup.find_all('div',class_='nb__2NPHR',id='minDeposit',itemprop='valueReference',itemtype=True)
C=[]
for n in er:
    c=n.span.text
    C.append(c)

House=pd.DataFrame({},index=range(1,11))
House['House_Title']=name
House['Address']=addr
House['EMI']=epi
House['Area']=ar
House['Price']=C


