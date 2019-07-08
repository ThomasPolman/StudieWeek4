#Opgave 1: dictionary som
def sum_values(my_dictionary):
  return sum(my_dictionary.values())

#Opgave 2: dictionary som even sleutels
def sum_even_keys(my_dictionary):
  sum = 0
  for key in my_dictionary:
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum

#Opgave 3: toevoegen waarde - hier +10 - aan dictwaarden
def add_ten(my_dictionary):
  for item in my_dictionary.keys():
    my_dictionary[item] += 10
  return my_dictionary

#Opgave 4: waarden die ook als sleutels voorkomen
def values_that_are_keys(my_dictionary):
  equals = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      equals.append(value)
  return equals

#Opgave 5: maximum waarde vinden, bijbehorende sleutel printen
def max_key(my_dictionary):
  values = [value for value in my_dictionary.values()]
  maximum = max(values)
  for key, value in my_dictionary.items():
    if value == maximum:
      return key

#Opgave 6: functie die een dictionary creëert van een lijst met woorden en hun lengte
def word_length_dictionary(words):
  length = []
  for word in words:
    length.append(len(word))
  return {key:value for key, value in zip(words, length)}

#Opgave 7: woordenlijst koppelen aan de frequentie van specifieke woorden
def frequency_dictionary(list_of_words):
  dictionary = {}
  for word in list_of_words:
    if word in dictionary:
      dictionary[word] += 1
    elif word in list_of_words:
      dictionary[word] = 1
  return dictionary

#Opgave 8: teller voor unieke waarden in dictionary
def unique_values(my_dictionary):
  values = []
  for value in my_dictionary.values():
    if value in values:
      continue
    else:
      values.append(value)
  return len(values)

#Opgave 9: frequentie tellen beginletter van achternaam
def count_first_letter(names):
  letters = {}
  for key in names.keys():
    if not key[0] in letters:
      letters.update({key[0]:len(names[key])})
    else:
      letters[key[0]] += len(names[key])
  return letters

print(count_first_letter({"Groeneveld": ["Theo", "Maya", "Annelies", "Noortje"], "Gorter": ["Marjolein", "David"], "Uvall": ["Gerrit", "Floor"], "Bronstee": ["Filip"], "van Steen": ["Jacob", "Regina", "Tarik"], "van Hoofdland": ["Margot", "Henk"]}))
        
