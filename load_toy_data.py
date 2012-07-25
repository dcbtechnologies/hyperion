from pyes.es import ES
import random
import datetime

now = datetime.datetime.now()
es = ES()
for i in range(1000):
    d = {'created_at': now - datetime.timedelta(seconds=i),
            'level': 'ERROR' if random.random() < 0.1 else 'WARN',
            'message': "Test message"}
    es.index(d, 'my_index', 'my_type')
