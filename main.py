from datetime import date
import pandas as pd
import requests

# It seems like the API is sensitive to these dates. We may have to pull multiple days at once.
begin = date(2020,2,1)
end = date(2020,3,18)

api_string = "https://api.openaq.org/v1/measurements?location={location}&parameter={measure}&date_from={fromdate}&date_to={todate}&limit=9000"
location = "Pasadena"
measure = "co"

df = pd.DataFrame(requests.get(api_string.format(location=location,measure=measure,fromdate=begin,todate=end)).json()['results'])
df['localtime']=[x.get('local') for x in df['date']]
df = df.set_index('localtime')
df = df[['location','parameter','value','unit']]
print(df)
