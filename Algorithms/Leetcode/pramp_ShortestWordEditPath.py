def shortestWordEditPath(source, target, words):
  queue = [(source, 0)]
  seen = set([source]) 

  while queue:
    current = queue.pop(0)
    current_word = current[0]
    current_count = current[1]

    if current_word == target:
      return current_count 

    for neighbor in get_one_off(current_word, words):
      if neighbor not in seen:
        queue.append((neighbor, current_count + 1))
        seen.add(neighbor)
  return -1 

def get_one_off(current_word, words):
  result_arr = [] 
  for word in words:
    count = 0
    if word == current_word or len(word) != len(current_word):
      continue
    for i in range(len(current_word)):
      if current_word[i] != word[i]: 
        count+=1
        if count > 1:
          break
    if count <= 1:
      result_arr.append(word)
  return result_arr








