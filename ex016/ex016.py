##Funções

def evenOfList(array):
    for num in array:
        if num % 2 == 0:
            evens.append(num)


##variaveis 
evens = []
arrayOfValues = [0,1,2,3,4,5,6,7,8,9,10]

##exec da funcao
evenOfList(arrayOfValues)
print(sum(evens))      

