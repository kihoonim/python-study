import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('foo1', 'bar1')
r.set('foo2', 'bar2')
r.set('foo3', 'bar3')
r.set('foo4', 'bar4')

var = r.get('foo1')
var = r.get('foo2')
var = r.get('foo3')
var = r.get('foo4')

print(var)