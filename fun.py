def query_bond(**test):
    name = test['name']
    type = test['type']
    print name,type
    # for eachXtrArg in name.keys():
    #     print 'Xtra arg %s: %s' % (eachXtrArg, str(name[eachXtrArg]))
query_bond(name="aa",type="pc")