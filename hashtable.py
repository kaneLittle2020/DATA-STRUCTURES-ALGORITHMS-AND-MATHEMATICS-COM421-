class Hashtable:
  def __init__(slef, capacity=127):
    self.buckets = [None] * self.nbuckets

  def put (self, key, value):
    pass

  def get (self, key):
    pass

table = Hashtable()
table.put("cat", "A furry animal which goes meow")
table.put("dog","A furry animel that goes bark")
print(table.get("cat"))
