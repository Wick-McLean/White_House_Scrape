from datetime import datetime
import requests
from bs4 import BeautifulSoup
import lxml
from get_remarks_pages import get_remarks_urls
from get_remarks_pages import save_to_file
from get_remarks_pages import make_file
from SaveToS3 import save_to_s3

url = ('https://www.whitehouse.gov/remarks/')
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

now = str(datetime.now())

# runtime
y = get_remarks_urls(soup)
z = make_file(y)
save_to_file(z)
botofiles = save_to_s3('speech_list.txt', 'nymag-scrape-articles-from-python', 'Remarks by President', now)
