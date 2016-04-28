import keys,json,requests

def news_list(search_query, outfile='urls.txt', count=10):
    f = open(outfile,'w')
    endpoint = 'https://gateway-a.watsonplatform.net/calls/data/GetNews'
    payload = { 'outputMode':'json',
                'start':'now-10d',
                'end':'now',
                'count':count,
                'q.enriched.url.enrichedTitle.keywords.keyword.text':search_query,
                'return': 'enriched.url.url,enriched.url.title',
                'apikey':keys.alchemykey,
              }
    r = requests.get(endpoint,params=payload)
    print r.url
    json_vals = r.json()
    for each_story in json_vals['result']['docs']:
        source = each_story['source']['enriched']['url']
        f.write(source['title'].encode('utf-8') + '^' + source['url'].encode('utf-8')+'\n')
    #print json.dumps(json_vals,indent=4,sort_keys=True)

if __name__ == '__main__':
    news_list('india')
