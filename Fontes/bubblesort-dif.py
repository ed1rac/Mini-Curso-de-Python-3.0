def bubble_sort(array):  
  contador = 0
  troca = True

  while troca:
    troca = False
    for i in range(len(array)-1):
      if array[ i ] > array[i + 1]:
        contador = contador +1
        array[i], array[i + 1] = array[i + 1], array[i]
        print(array)
        troca = True    
  
  return array,contador

#valores = input('Digite os números do vetor separados por virgulas: ')
#lista = eval("["+valores+"]")
lista = [50,40,30,20,10,5,1,0]
print(lista)
print(bubble_sort(lista))
#print(f"Em {contador}")