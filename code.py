import hashlib
def dump_dict(filename):
         txt = str(open(filename, "r").readlines())
         txt = ((txt.split("{")[1]).split("}")[0])
         txt = txt.split("]")
         ldict = {}
         for i in txt[:-1]: 
             llist = []
             split = i.split('"')
             for j in i :
                 if len(j) == 1 : 
                     if ord(j) not in [44,91,93,32,58,34] :
                         llist.append(j)
                 else :
                     pass
             ldict[llist[0]] = llist[1:]
         return ldict 
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
def glue(list):
    _list = [] 
    for i in list : 
        str = ""
        for j in i : 
            str += j 
        _list.append(str)
    return _list
def arglist(message,keys):
    arglist = []
    for i in message: 
            if i in keys : 
                arglist.append(ldict[i])
            else : 
                arglist.append([i])
    return arglist
ldict = dump_dict("letters.json")
message = input("Enter Your Message : ")
arglist = arglist(message,list(ldict.keys()))
strings = glue(list(product(*arglist, repeat=1)))
phrase = input("Enter that phrase you want to find in your hash:")
cnt = 0 
for i in strings : 
    hash = hashlib.sha256(i.encode()).hexdigest()
    if hash.count(phrase) > 0 : 
       cnt += 1
       print(" | hash : {} \n | string : {} | count : {} ".format(hash,i,hash.count(phrase)))

print("\n | total found : {} \n | total strings : {}".format(cnt,len(strings)))




