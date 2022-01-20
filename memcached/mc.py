import memcache

mc = memcache.Client(['127.0.0.1:32768'],debug=0)
print(mc.set("test_key", "test_val"))
print(mc.get("test_key"))