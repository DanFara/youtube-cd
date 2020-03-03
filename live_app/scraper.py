import requests
from bs4 import BeautifulSoup


url = 'https://www.youtube.com/watch?v=u1Fad96vuBc'
chat_html_id = "live-chat-iframe"


soup = BeautifulSoup(requests.get(url).content, 'html.parser')
chat_frame = soup.find(id=chat_html_id)
chat_url=chat_frame.get('src')

#these headers work, need to filter through to see what is necessary vs what isn't later... (likely a user agent thing)
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-YouTube-Client-Name': '1',
    'X-YouTube-Client-Version': '2.20200302.10.01',
    'X-YouTube-Device': 'cbr=Firefox&cbrver=72.0&cos=X11',
    'X-YouTube-Utc-Offset': '0',
    'X-YouTube-Time-Zone': 'UTC',
    'TE': 'Trailers',
}

chat_json = requests.get(chat_url + '%253D%253D&hidden=false&pbj=1', headers=headers).json()

def chat_json_processor(chat_json):
    response = chat_json[1]['response']
    content=response['continuationContents']['liveChatContinuation']
    messages = content['actions']
    return messages

def message_processor(msg):
    try:
        real_content = msg['addChatItemAction']['item']['liveChatTextMessageRenderer']
        text = real_content['message']['runs'][0]['text']
        author = real_content['authorName']['simpleText']
        timestamp = real_content['timestampUsec']
        return(text, author, timestamp)
    except:
        pass

for msg in chat_json_processor(chat_json):
    x=[]
    y=message_processor(msg)
    if y != None:
        x.append(y)
        print(y)

'''
driver.get(driver.find_elements_by_id("chatframe")[0].get_attribute('src'))
'%253D%253D&hidden=false&pbj=1' #append this to chat url!
'''
