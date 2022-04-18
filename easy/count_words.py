# Una función que recibe un arreglo de palabras y una palabra debe retornar la cantidad de veces que aparece esa palabra en el arreglo y el largo del arreglo
#Al llamarla con (["ab","a"], "a") debería retornar (1,2)

def count_word(words, word):
  repetition=0
  for i in words:
    if word == i:
      repetition=repetition+1
  return (repetition, len(words))
