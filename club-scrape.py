from bs4 import BeautifulSoup
from urllib.request import urlopen

def stackoverflow_job_info(url):
    output = []
    with urlopen(url) as fp:
        bs = BeautifulSoup(fp, 'html.parser')

    #job type
    items = bs.find(id='overview-items')
    mb8 = bs.find_all(class_='mb8')
    mb8_text = [x.get_text() for x in mb8]
    #print(mb8_text)

    job_type = ''
    for i, text in enumerate(mb8_text):
        if 'Job type:' in text:
            job_type = text

    output.append(job_type[11:].strip())

    #technologies
    technologies = []
    for tech in bs.find_all(class_='post-tag job-link no-tag-menu'):
        technologies.append(tech.get_text())
    output.append(technologies)

    #job title
    output.append(bs.find(class_='fc-black-900').get_text())

    #location
    location = (bs.find(class_='fc-black-500').get_text().strip())
    location = location[3:]
    output.append(location)

    return output

job_url = 'https://stackoverflow.com/jobs'
with urlopen(job_url) as fp:
    bs = BeautifulSoup(fp, 'html.parser')

links = bs.find_all(class_='mb4 fc-black-800 fs-body3')

urls = []
for link in links:
    urls.append(link.a.get('href'))

for url in urls:
    new_url = job_url[:job_url.find('/jobs')] + url
    print(new_url)
    print(stackoverflow_job_info(new_url))
    print()

