a = 'Th é meu nome'
b = 'Th é meu nome'
print(a == b)
print(a is b)
a = [1, 2, 3]
b = a

print(a is b)  # True, pois 'b' se refere ao mesmo objeto na memória que 'a'
#para verificar a igualdade de valor, é mais comum usar o operador ==. 'is' é usado para ver se dois objetos tem a mesmsa identidade(se referem ao mesmo local na memoria)
