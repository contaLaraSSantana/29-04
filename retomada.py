# CRIAÇÃO DAS VARIAVEIS 

produtos = ['Bala','Chocolate','Pirulito','Bombom','Chiclete']
estoque = [200,300,100,70,50]
minimo = [20,30,10,7,5]

# MOSTRANDO AS LINHAS DE PRODUTOS 

for i in range(len(produtos)):
    print(f"A quantidade de {produtos[i]} é {estoque[i]} e seu estoque minimo é de {minimo[i]}")

# USUARIO ADICIONANDO COISAS NA LISTA

prod = input("Digite o seu produto aqui: ")
est = int(input("Digite o seu estoque aqui: "))
minimos = int(input("Digite o seu minimo de estoque aqui: "))

# ATRIBUINDO OQUE ELE DIGITOU

produtos.append(prod)
estoque.append(est)
minimo.append(minimos)

# MOSTRANDO O QUE ELE DIGITOU

for i in range(len(produtos)):
    print(f"A quatidade de {produtos[i]} é {estoque[i]} e seu estoque minimo é de {minimo[i]}")

# ATRIBUINDO LIMITE DO ESTOQUE 

for i in range(len(produtos)):
    if estoque[i] <= minimo[i]:
        print(f"\nO produto {produtos[i]} está e sua quantidade minima")

#Dividindo em listas/matriz

lista = []
for num in range (len(produtos)):
    lista.append([produtos[num], estoque[num], minimo[num]])

#apagar um item da lista

while True:
    remover = input("Digite o nome do produto que deseja apagar:")
    if remover in produtos:
        break
    else:
        print("Produto não encontrado!")
        ind = produtos.index(remover) 
        produtos.remove(remover)
        estoque.remove(estoque[ind])
        minimo.remove(minimo[ind])
        print(produtos, estoque, minimo)

#Lista de compras
pedidos = []
while True:
    ped_prod = input("Digite o seu pedido aqui: ")
    ped_qnt = int(input("Digite a quantidade aqui: "))
    pedidos.append([ped_prod, ped_qnt])
    repete = input('Deseja continuar? s/n: ')
    if repete.upper() == 'n':
        break
print(pedidos)

#Criar uma função para remover pedidos da lista de pedidos;

for itens in pedidos:
    if itens[0] not in produtos:
        print (f'Produto {itens[0]} não etá em estoque')
    elif itens [1] < estoque[produtos.index(itens[0])]:
        print (f'Saldo insuficiente de'{itens[0]})
