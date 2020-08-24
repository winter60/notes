import requests,re,csv
with open(r'福利.csv','w',encoding = 'utf-8_sig',newline = '') as f:
    write = csv.writer(f)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    url = 'https://www.iqshw.com/'
    html = requests.get(url = url,headers = headers)
    html.encoding = 'GBK'
    r1 = re.findall(r'html"><i></i>(.*?)</a>',html.text)
    r2 = re.findall(r'<a target="_blank" href="(.*?)"><i></i>',html.text)
    n = 0
    for i in r1:
        u = [i,f'https://www.iqshw.com{r2[n]}']
        write.writerow(u)
        print(u)
        n += 1