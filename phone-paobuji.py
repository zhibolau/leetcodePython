"""
c = [25, 25, 25, 5, 5, 25, 25, 25, 25, 25, 1, 25, 25, 25, 10, 10, 25]
     |---75---|  |--85, 10 back-| |--76, 1 back-| |--95, 20 back  -|
 
Expected Output:
OPEN
[] # no change
OPEN
[10] # note not [5, 5] or [5, 1, 1, 1, 1, 1]
OPEN
[1] # 1 penny back
OPEN
[10, 10] # 2 dimes returned
"""
 
PRICE = 75
VALID_COINS = [1, 5, 10, 25]
c = [25, 25, 25, 5, 5, 25, 25, 25, 25, 25, 1, 25, 25, 25, 10, 10, 25]

def ticket_machine(price, c):
  if c == []:
    return
  res = []
  coins = 0
  start = 0
  for i,j in enumerate(c):
    coins += j
    if coins < 75:
      start += 1
      continue
    else:
      break
  rest = coins - 75
  print(rest)
  #print(c)
  if c:
    ticket_machine(75,c[start+1:])

ticket_machine(75, c)

      
