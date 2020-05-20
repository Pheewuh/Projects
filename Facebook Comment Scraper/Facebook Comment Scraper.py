import requests
import signal
import sys

graph_api_version = 'v7.0'
access_token = 'EAAoTqyOAerABADz266RWHTbd3hc3ndbWLRB50ut7sOFpXLdbJN6j1mJEy8nxPtA9EmNOIjTFMf1ZAMOwH0F7zzorUd7AShcQ9vBaRnlReWypAVxQuK4oc6PzGTZAPZBA3ddvyW7OnJpKvC4wkX3ZAdPNaTOE9F1ctSY6ygAewlAKFUcMLklEgS1BJG6MDSJMkg4FT8rHnbBaAKhzCJZBPs3RbSYQviTzhh0aKVj6M0gZDZD'

user_id = '100013060031570'

post_id = '917946408650685'

url = 'https://graph.facebook.com/{}/{}_{}/comments'.format(graph_api_version, user_id, post_id)

comments = []

limit = 200

def write_comments_to_file(filename):
    print()

    if len(comments) == 0:
        print('No comments to write.')
        return

    with open(filename, 'w', encoding='utf-8') as f:
        for comment in comments:
            f.write(comment + '\n')

    print('Wrote {} comments to {}\n'.format(len(comments), filename))

def signal_handler(signal, frame):
    print('KeyboardInterrupt')
    write_comments_to_file('comments.txt')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

r = requests.get(url, params={'access_token': access_token})
while True:
    data = r.json()

    if 'error' in data:
        raise Exception(data['error']['message'])

    for comment in data['data']:
        text = comment['message'].replace('\n', ' ')
        comments.append(text)

    print('Got {} comments, total: {}'.format(len(data['data']), len(comments)))

    if 0 < limit <= len(comments):
        break

    if 'paging' in data and 'next' in data['paging']:
        r = requests.get(data['paging']['next'])
    else:
        break

write_comments_to_file('comments.txt')

pos=['good','cool']
negadj=['bad','lame']
neg=['not']
contents=open('comments.txt',mode='r')
words=[]
values=[]

for i in contents.readlines():
	words.append(i[:len(i)-1])
	values.append('')

for i in words:
	for j in i.split():
		if j in pos:
			if i.split()[i.split().index(j)-1] not in neg:
				print('Pos')
				values[words.index(i)]=1
			else:
				print('Neg')
				values[words.index(i)]=0
		if j in negadj:
			if i.split()[i.split().index(j)-1] not in neg:
				print('Neg')
				values[words.index(i)]=0
			else:
				print('Pos')
				values[words.index(i)]=1