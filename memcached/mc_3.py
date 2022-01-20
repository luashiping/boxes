import bmemcached

client = bmemcached.Client(('127.0.0.1:11211', ), 'my_user',
                            'my_password')
client.set('test_key', 'test_val')
print(client.get('test_key'))