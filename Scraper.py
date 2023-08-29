from autoscraper import AutoScraper
import pandas as pd
url = 'https://www.boerse-stuttgart.de/en/tools/finder-tools/most-frequent-trades/?category=4991'

wanted_list1 = ['Porsche Automobil Holding SE Medium Term Notes v.23(30/30)']
wanted_list2 = ['97.611 G','1.756.199,00']
wanted_list3 = ['A351SX','/de-de/produkte/anleihen/stuttgart/a351sx-porsche-automobil-holding-se-medium-term-notes-v233030']
scraper = AutoScraper()
#scraper.build(url, wanted_dict=wanted_dict)
df = pd.DataFrame()
df['Issuer'] = pd.DataFrame(scraper.build(url, wanted_list1))
df['Price'] = pd.DataFrame(scraper.build(url, wanted_list2))
df['Code'] = pd.DataFrame(scraper.build(url, wanted_list3))

print(df)