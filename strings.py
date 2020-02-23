#Parsing strings
data = 'From dowon@whiteblock.co Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
sppos = data.find(' ', atpos)
host = data[atpos+1 : sppos]
print(host)

#Formatting strings
camels = 42
print('I have spotted %d camels' % camels)
print('In %d years I have spotted %g %s' % (3, 0.1, 'camels'))