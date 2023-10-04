class Category:
  
  def __init__(self , category):
    self.category = category
    self.ledger = []
    

  def __str__(self):
    txt = self.category.center(30 , "*") + "\n"
    
    for item in self.ledger:
      temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      txt += temp + "\n"

    txt += f"Total: {self.get_balance()}"
    
    return txt
    

  def deposit(self , amount , description = ""):
    temp = {}
    temp['amount'] = amount
    temp['description'] = description
    self.ledger.append(temp)
    
    
  def withdraw(self , amount , description = ""):
    if(self.check_funds(amount)):
      
      temp = {}
      temp['amount'] = 0 - amount
      temp['description'] = description
      self.ledger.append(temp)
      return True
    
    return False


  def get_balance(self):
    balance = 0

    for item in self.ledger:
      balance += item['amount']

    return balance

  
  def transfer(self , amount , to_cat):
    if(self.check_funds(amount)):
      
      self.withdraw(amount , "Transfer to " + to_cat.category)
      
      to_cat.deposit(amount , "Transfer from " + self.category)
      
      return True
      
    return False
  
    
  def check_funds(self , amount):
    if amount > self.get_balance():
      return False
      
    return True
    

def create_spend_chart(categories):
  spend = []

  for category in categories:
    temp = 0

    for item in category.ledger:
      if item['amount'] < 0 :
        temp += abs(item['amount'])
    
    spend.append(temp)

  total = sum(spend)
  percent = [i/total * 100 for i in spend]

  txt = "Percentage spent by category"

  for i in range(100 , -1 , -10):
    txt += "\n" + str(i).rjust(3) + "|"

    for j in percent:
      if j > i :
        txt += " o "
      else :
        txt += " "*3

    txt += " "

  txt += "\n" + " "*4 + "-"*10

  cat_len = []
  
  for category in categories:
    cat_len.append(len(category.category))

  max_len = max(cat_len)

  for i in range(max_len):
    txt += "\n" + " "*4

    for j in range(len(categories)):
      if i < cat_len[j] :
        txt += " " + categories[j].category[i] + " "
      else:
        txt += " "*3
      
    txt += " "
    
  return txt
        

  
      
        
  