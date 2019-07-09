punctuation = [',', '.', '(', ')', '!', '?', '%', '/', '"']

#Censuur enkel woord/zin
def censor_phrase(document, phrase):
  censored_document = document.replace(phrase, "")
  return censored_document

#Censuur van een lijst met woorden
def censor_list(document, lst):
  document = document.lower()
  for word in lst:
    censor = ""
    for i in range(len(word)):
      censor += "*"
    document = document.replace(word, censor)
  return document.capitalize()

#Censuur van een lijst en een tweede lijst, enkel censureren bij repetitie
def censor_list_and_neg_words(document, lst, neg_words):
  document = document.lower()
  listed_document = []
  for x in document.split(" "):
    words = x.split("\n")
    for word in words:
      for j in punctuation:
        word = word.strip(j)
      listed_document.append(word)
  count = 0
  for i in range(len(listed_document)):
    if listed_document[i] in neg_words:
      count += 1
      if count > 2:
        censor = ""
        for x in range(len(listed_document[i])):
          censor += "*"
        listed_document[i] = listed_document[i].replace(listed_document[i], censor)
  for i in range(len(listed_document)):  
    if listed_document[i] in lst:
      censor = ""
      for x in range(len(listed_document[i])):
        censor += "*"
      listed_document[i] = listed_document[i].replace(listed_document[i], censor)
  result = ' '.join(listed_document)
  return result.capitalize()

#Censureer alles van de lijst + het direct voorgaande en nakomende woord
def censor_bonanza(document, censors):
  document = document.lower()
  listed_document = []
  for x in document.split(" "):
    words = x.split("\n")
    for word in words:
      for j in punctuation:
        word = word.strip(j)
      listed_document.append(word)
  for i in range(len(listed_document)):
    
    if listed_document[i] in censors:
      
      censor = ""
      for x in range(len(listed_document[i])):
        censor += "*"
      listed_document[i] = listed_document[i].replace(listed_document[i], censor)
      
      censor2 = ""
      for x in range(len(listed_document[i-1])):
        censor2 += "*"
      listed_document[i-1] = listed_document[i-1].replace(listed_document[i-1], censor2)
      
      censor3 = ""
      for x in range(len(listed_document[i+1])):
        censor3 += "*"
      listed_document[i+1] = listed_document[i+1].replace(listed_document[i+1], censor3)
      
  return ' '.join(listed_document)
  


