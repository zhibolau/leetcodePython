file_object1 = open("microsoft 82.txt",'r')
co = []
try:
  while True:
      line = file_object1.readline()
      if line:
      	l = line.split()
        #print "line=",l[0]
        co.append(l[0])
      else:
          break
  indexes = co[1:]        
  print sorted(indexes)
  print len(indexes)        
finally:
    file_object1.close()