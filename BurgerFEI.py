from asyncore import write
import os
from datetime import datetime

#1
#feito
#função para criar o arquivo do novo cliente, ele organiza as informações do pedido dentro do arquivo
def novopedido():
    print()
    nome=input("Nome: ")
    cpf=input("CPF: ")
    senha=input("Senha: ")

    if os.path.isfile(cpf+'.txt'):
        print("\nCliente já registrado!\n")
    #construindo o arquivo com as informações do cliente
    else:
        if len(cpf) == 11:
            data_e_hora = datetime.now()
            data_e_hora = data_e_hora.strftime('%Y-%m-%d %H:%M')
            total = 0
            #lista criada para armazenar o número de pedidos de cada uma das sete opções possíveis
            numero_de_pedidos = [0,0,0,0,0,0,0]
            arquivo = open(cpf+'.txt', 'w')
            arquivo.write('%s\n'%data_e_hora)
            arquivo.write('%s\n'%nome)
            arquivo.write('%s\n'%cpf)
            arquivo.write('%s\n'%senha)
            arquivo.write('%i\n'%total)
            arquivo.write('%s\n'%numero_de_pedidos)
            #criando o histórico de todas as operações realizadas no pedido
            arquivo.write('\nNome: {}'.format(nome))
            arquivo.write('\nCPF: {}'.format(cpf))
            arquivo.write('\nTotal: R$ {}'.format(total))
            arquivo.write('\nData: {}\nItens do pedido: '.format(data_e_hora))
            arquivo.close()
            print("\nCadastro concluído\n")
            print()
            menu_do_pedido(cpf)
        else:
            print('\n Número de caracteres mínimo não atingido para o CPF.\n\nInsira os dados corretamente...')

#feito
#função responsável por adicionar o produto, quantidade e adicionar o seu valor ao total
def menu_do_pedido(cpf):
    print()
    print("%10s"%"Código","%14s"%"Produto","%18s"%"Preço\n","%4s"%"1","%20s"%"X-salada","%20s"%"R$ 10,00\n","%4s"%"2","%21s"%"X-burguer","%19s"%"R$ 10,00\n","%4s"%"3","%27s"%"Cachorro quente","%12s"%"R$ 7,50\n","%4s"%"4","%24s"%"Misto quente","%15s"%"R$ 8,00\n","%4s"%"5","%28s"%"Salada de frutas","%11s"%"R$ 5,50\n","%4s"%"6","%24s"%"Refrigerante","%15s"%"R$ 4,50\n","%4s"%"7","%24s"%"Suco natural","%14s"%"R$ 6,25")
    print()
    #transformando o arquivo em uma lista para modificar os dados do arquivo
    lista = []
    arquivo = open(cpf+'.txt')
    for linha in arquivo.readlines():
        lista.append(linha)
    arquivo.close()
    codigo_do_produto=int(input("Digite o código do produto: "))
    quantidade_do_produto=int(input("Digite o valor de unidades do produto: "))
    if codigo_do_produto == 1:
        #X-salada
        nome_do_produto = 'X-salada'
        preço_unitário = 10.00
        pagar = preço_unitário * quantidade_do_produto
        total = float(lista[4]) + pagar
        lista[4] = str(total)
        lista[4] = (lista[4]+"\n")
        lista[9] = ('Total: R$ {}\n'.format(total))
        #para transformar a lista contida no arquivo em uma lista de inteiros
        pedido_atual = lista[5].strip('][\n').split(', ')
        for i in range(0,len(pedido_atual)):
            pedido_atual[i] = int(pedido_atual[i].strip())
        pedido_atual[0] += quantidade_do_produto
        lista[5] = str(pedido_atual)+'\n'
        lista.append('\n%-4s'%quantidade_do_produto)
        lista.append('- %-16s'%nome_do_produto)
        lista.append('- Preço unitário: %-6s'%preço_unitário)
        lista.append('Valor: + %3s'%pagar)
        arquivo = open(cpf+'.txt','w')
        #reposição de informações no arquivo
        for i in range(0,len(lista)):
            arquivo.writelines(lista[i])
        arquivo.close()
        print('\nRealizado com sucesso!\n')
    #os elifs a seguir seguem as mesmas instruções porem mudam de acordo com o pedido
    elif codigo_do_produto == 2:
        #X-burguer
        nome_do_produto = 'X-burguer'
        preço_unitário = 10.00
        pagar = preço_unitário * quantidade_do_produto
        total = float(lista[4]) + pagar
        lista[4] = str(total)
        lista[4] = (lista[4]+"\n")
        lista[9] = ('Total: R$ {}\n'.format(total))
        pedido_atual = lista[5].strip('][\n').split(', ')
        for i in range(0,len(pedido_atual)):
            pedido_atual[i] = int(pedido_atual[i].strip())
        pedido_atual[1] += quantidade_do_produto
        lista[5] = str(pedido_atual)+'\n'
        lista.append('\n%-4s'%quantidade_do_produto)
        lista.append('- %-16s'%nome_do_produto)
        lista.append('- Preço unitário: %-6s'%preço_unitário)
        lista.append('Valor: + %3s'%pagar)
        arquivo = open(cpf+'.txt','w')
        for i in range(0,len(lista)):
            arquivo.writelines(lista[i])
        arquivo.close()
        print('\nRealizado com sucesso!\n')
    elif codigo_do_produto == 3:
        #Cachorro quente
        nome_do_produto = 'Cachorro quente'
        preço_unitário = 7.50
        pagar = preço_unitário * quantidade_do_produto
        total = float(lista[4]) + pagar
        lista[4] = str(total)
        lista[4] = (lista[4]+"\n")
        lista[9] = ('Total: R$ {}\n'.format(total))
        pedido_atual = lista[5].strip('][\n').split(', ')
        for i in range(0,len(pedido_atual)):
            pedido_atual[i] = int(pedido_atual[i].strip())
        pedido_atual[2] += quantidade_do_produto
        lista[5] = str(pedido_atual)+'\n'
        lista.append('\n%-4s'%quantidade_do_produto)
        lista.append('- %-16s'%nome_do_produto)
        lista.append('- Preço unitário: %-6s'%preço_unitário)
        lista.append('Valor: + %3s'%pagar)
        arquivo = open(cpf+'.txt','w')
        for i in range(0,len(lista)):
            arquivo.writelines(lista[i])
        arquivo.close()
        print('\nRealizado com sucesso!\n')
    elif codigo_do_produto == 4:
        #Misto quente
        nome_do_produto = 'Misto quente'
        preço_unitário = 8.00
        pagar = preço_unitário * quantidade_do_produto
        total = float(lista[4]) + pagar
        lista[4] = str(total)
        lista[4] = (lista[4]+"\n")
        lista[9] = ('Total: R$ {}\n'.format(total))
        pedido_atual = lista[5].strip('][\n').split(', ')
        for i in range(0,len(pedido_atual)):
            pedido_atual[i] = int(pedido_atual[i].strip())
        pedido_atual[3] += quantidade_do_produto
        lista[5] = str(pedido_atual)+'\n'
        lista.append('\n%-4s'%quantidade_do_produto)
        lista.append('- %-16s'%nome_do_produto)
        lista.append('- Preço unitário: %-6s'%preço_unitário)
        lista.append('Valor: + %3s'%pagar)
        arquivo = open(cpf+'.txt','w')
        for i in range(0,len(lista)):
            arquivo.writelines(lista[i])
        arquivo.close()
        print('\nRealizado com sucesso!\n')
    elif codigo_do_produto == 5:
        #Salada de frutas
        nome_do_produto = 'Salada de frutas'
        preço_unitário = 5.50
        pagar = preço_unitário * quantidade_do_produto
        total = float(lista[4]) + pagar
        lista[4] = str(total)
        lista[4] = (lista[4]+"\n")
        lista[9] = ('Total: R$ {}\n'.format(total))
        pedido_atual = lista[5].strip('][\n').split(', ')
        for i in range(0,len(pedido_atual)):
            pedido_atual[i] = int(pedido_atual[i].strip())
        pedido_atual[4] += quantidade_do_produto
        lista[5] = str(pedido_atual)+'\n'
        lista.append('\n%-4s'%quantidade_do_produto)
        lista.append('- %-16s'%nome_do_produto)
        lista.append('- Preço unitário: %-6s'%preço_unitário)
        lista.append('Valor: + %3s'%pagar)
        arquivo = open(cpf+'.txt','w')
        for i in range(0,len(lista)):
            arquivo.writelines(lista[i])
        arquivo.close()
        print('\nRealizado com sucesso!\n')
    elif codigo_do_produto == 6:
        #Refrigerante
        nome_do_produto = 'Refrigerante'
        preço_unitário = 4.50
        pagar = preço_unitário * quantidade_do_produto
        total = float(lista[4]) + pagar
        lista[4] = str(total)
        lista[4] = (lista[4]+"\n")
        lista[9] = ('Total: R$ {}\n'.format(total))
        pedido_atual = lista[5].strip('][\n').split(', ')
        for i in range(0,len(pedido_atual)):
            pedido_atual[i] = int(pedido_atual[i].strip())
        pedido_atual[5] += quantidade_do_produto
        lista[5] = str(pedido_atual)+'\n'
        lista.append('\n%-4s'%quantidade_do_produto)
        lista.append('- %-16s'%nome_do_produto)
        lista.append('- Preço unitário: %-6s'%preço_unitário)
        lista.append('Valor: + %3s'%pagar)
        arquivo = open(cpf+'.txt','w')
        for i in range(0,len(lista)):
            arquivo.writelines(lista[i])
        arquivo.close()
        print('\nRealizado com sucesso!\n')
    elif codigo_do_produto == 7:
        #Suco natural
        nome_do_produto = 'Suco natural'
        preço_unitário = 6.25
        pagar = preço_unitário * quantidade_do_produto
        total = float(lista[4]) + pagar
        lista[4] = str(total)
        lista[4] = (lista[4]+"\n")
        lista[9] = ('Total: R$ {}\n'.format(total))
        pedido_atual = lista[5].strip('][\n').split(', ')
        for i in range(0,len(pedido_atual)):
            pedido_atual[i] = int(pedido_atual[i].strip())
        pedido_atual[6] += quantidade_do_produto
        lista[5] = str(pedido_atual)+'\n'
        lista.append('\n%-4s'%quantidade_do_produto)
        lista.append('- %-16s'%nome_do_produto)
        lista.append('- Preço unitário: %-6s'%preço_unitário)
        lista.append('Valor: + %3s'%pagar)
        arquivo = open(cpf+'.txt','w')
        for i in range(0,len(lista)):
            arquivo.writelines(lista[i])
        arquivo.close()
        print('\nRealizado com sucesso!\n')
    else:
        print('\nCódigo inválido\n')
    print()

#2
#feito
def cancelapedido():
    print()
    cpf = input('Digite o CPF: ')
    senha = input ('Digite a senha: ')
    if os.path.isfile(cpf+'.txt'):
        arquivo = open(cpf + '.txt', 'r')
        leitor = arquivo.read()
        lista = []
        lista = leitor.split()
        arquivo.close()
        if lista[3] == cpf and lista[4] == senha:
            os.remove(cpf+'.txt')
            print("\nPedido cancelado\n")
        else:
            print("\nOs dados não coincidem\n")
    else:
        print('\nEste CPF não foi cadastrado\n')

#3
#feito
#A função a seguir pede as informações do usuário e confere o cpf e senha 
def insereproduto():
    print()
    cpf = input('Digite o CPF: ')
    senha = input ('Digite a senha: ')
    #para verificar é necessário transformar o arquivo em lista novamente
    if os.path.isfile(cpf+'.txt'):
        arquivo = open(cpf + '.txt', 'r')
        leitor = arquivo.read()
        lista = []
        lista = leitor.split()
        arquivo.close()
        if lista[3] == cpf and lista[4] == senha:
            #se os dados estiverem certos o usuário pode fazer o seu pedido
            menu_do_pedido(cpf)
        else:
            print("Os dados não coincidem")  
    else:
        print('\nEste CPF não foi cadastrado\n') 

#4
#função responsável pela cancela de produtos do pedido
def cancelaproduto():
    print()
    cpf = input('Digite o CPF: ')
    senha = input ('Digite a senha: ')
    #conferindo os dados
    if os.path.isfile(cpf+'.txt'):
        arquivo = open(cpf + '.txt', 'r')
        leitor = arquivo.read()
        lista = []
        lista = leitor.split()
        arquivo.close()
        if lista[3] == cpf and lista[4] == senha:
            print()
            print("%10s"%"Código","%14s"%"Produto","%18s"%"Preço\n","%4s"%"1","%20s"%"X-salada","%20s"%"R$ 10,00\n","%4s"%"2","%21s"%"X-burguer","%19s"%"R$ 10,00\n","%4s"%"3","%27s"%"Cachorro quente","%12s"%"R$ 7,50\n","%4s"%"4","%24s"%"Misto quente","%15s"%"R$ 8,00\n","%4s"%"5","%28s"%"Salada de frutas","%11s"%"R$ 5,50\n","%4s"%"6","%24s"%"Refrigerante","%15s"%"R$ 4,50\n","%4s"%"7","%24s"%"Suco natural","%14s"%"R$ 6,25")
            print()
            lista = []
            arquivo = open(cpf+'.txt')
            for linha in arquivo.readlines():
                lista.append(linha)
            arquivo.close()
            codigo_do_produto=int(input("Digite o código do produto: "))
            quantidade_do_produto=int(input("Digite o valor de unidades do produto: "))
            pedido_atual = lista[5].strip('][\n').split(', ')
            for i in range(0,len(pedido_atual)):
                pedido_atual[i] = int(pedido_atual[i].strip())
            #praticamente igual a função de menu do pedido porem remove valores
            if codigo_do_produto == 1:
                if pedido_atual[0] >= quantidade_do_produto:
                    nome_do_produto = 'X-salada'
                    preço_unitário = 10.00
                    remover = preço_unitário * quantidade_do_produto
                    total = float(lista[4]) - remover
                    lista[4] = str(total)
                    lista[4] = (lista[4]+"\n")
                    lista[9] = ('Total: R$ {}\n'.format(total))
                    pedido_atual = lista[5].strip('][\n').split(', ')
                    for i in range(0,len(pedido_atual)):
                        pedido_atual[i] = int(pedido_atual[i].strip())
                    pedido_atual[0] -= quantidade_do_produto
                    lista[5] = str(pedido_atual)+'\n'
                    lista.append('\n%-4s'%quantidade_do_produto)
                    lista.append('- %-16s'%nome_do_produto)
                    lista.append('- Preço unitário: %-6s'%preço_unitário)
                    lista.append('Valor: - %3s'%remover)
                    lista.append(' - Cancelado')
                    arquivo = open(cpf+'.txt','w')
                    for i in range(0,len(lista)):
                        arquivo.writelines(lista[i])
                    arquivo.close()
                    print('\nCancelado com sucesso!\n')
                else:
                    print("\nNão é possível remover mais produtos do que os pedidos.\n")
            if codigo_do_produto == 2:
                if pedido_atual[1] >= quantidade_do_produto:
                    nome_do_produto = 'X-burguer'
                    preço_unitário = 10.00
                    remover = preço_unitário * quantidade_do_produto
                    total = float(lista[4]) - remover
                    lista[4] = str(total)
                    lista[4] = (lista[4]+"\n")
                    lista[9] = ('Total: R$ {}\n'.format(total))
                    pedido_atual = lista[5].strip('][\n').split(', ')
                    for i in range(0,len(pedido_atual)):
                        pedido_atual[i] = int(pedido_atual[i].strip())
                    pedido_atual[1] -= quantidade_do_produto
                    lista[5] = str(pedido_atual)+'\n'
                    lista.append('\n%-4s'%quantidade_do_produto)
                    lista.append('- %-16s'%nome_do_produto)
                    lista.append('- Preço unitário: %-6s'%preço_unitário)
                    lista.append('Valor: - %3s'%remover)
                    lista.append(' - Cancelado')
                    arquivo = open(cpf+'.txt','w')
                    for i in range(0,len(lista)):
                        arquivo.writelines(lista[i])
                    arquivo.close()
                    print('\nCancelado com sucesso!\n')
                else:
                    print("\nNão é possível remover mais produtos do que os pedidos.\n")
            if codigo_do_produto == 3:
                if pedido_atual[2] >= quantidade_do_produto:
                    nome_do_produto = 'Cachorro quente'
                    preço_unitário = 7.50
                    remover = preço_unitário * quantidade_do_produto
                    total = float(lista[4]) - remover
                    lista[4] = str(total)
                    lista[4] = (lista[4]+"\n")
                    lista[9] = ('Total: R$ {}\n'.format(total))
                    pedido_atual = lista[5].strip('][\n').split(', ')
                    for i in range(0,len(pedido_atual)):
                        pedido_atual[i] = int(pedido_atual[i].strip())
                    pedido_atual[2] -= quantidade_do_produto
                    lista[5] = str(pedido_atual)+'\n'
                    lista.append('\n%-4s'%quantidade_do_produto)
                    lista.append('- %-16s'%nome_do_produto)
                    lista.append('- Preço unitário: %-6s'%preço_unitário)
                    lista.append('Valor: - %3s'%remover)
                    lista.append(' - Cancelado')
                    arquivo = open(cpf+'.txt','w')
                    for i in range(0,len(lista)):
                        arquivo.writelines(lista[i])
                    arquivo.close()
                    print('\nCancelado com sucesso!\n')
                else:
                    print("\nNão é possível remover mais produtos do que os pedidos.\n")
            if codigo_do_produto == 4:
                if pedido_atual[3] >= quantidade_do_produto:
                    nome_do_produto = 'Misto quente'
                    preço_unitário = 8.00
                    remover = preço_unitário * quantidade_do_produto
                    total = float(lista[4]) - remover
                    lista[4] = str(total)
                    lista[4] = (lista[4]+"\n")
                    lista[9] = ('Total: R$ {}\n'.format(total))
                    pedido_atual = lista[5].strip('][\n').split(', ')
                    for i in range(0,len(pedido_atual)):
                        pedido_atual[i] = int(pedido_atual[i].strip())
                    pedido_atual[3] -= quantidade_do_produto
                    lista[5] = str(pedido_atual)+'\n'
                    lista.append('\n%-4s'%quantidade_do_produto)
                    lista.append('- %-16s'%nome_do_produto)
                    lista.append('- Preço unitário: %-6s'%preço_unitário)
                    lista.append('Valor: - %3s'%remover)
                    lista.append(' - Cancelado')
                    arquivo = open(cpf+'.txt','w')
                    for i in range(0,len(lista)):
                        arquivo.writelines(lista[i])
                    arquivo.close()
                    print('\nCancelado com sucesso!\n')
                else:
                    print("\nNão é possível remover mais produtos do que os pedidos.\n")
            if codigo_do_produto == 5:
                if pedido_atual[4] >= quantidade_do_produto:
                    nome_do_produto = 'Salada de frutas'
                    preço_unitário = 5.50
                    remover = preço_unitário * quantidade_do_produto
                    total = float(lista[4]) - remover
                    lista[4] = str(total)
                    lista[4] = (lista[4]+"\n")
                    lista[9] = ('Total: R$ {}\n'.format(total))
                    pedido_atual = lista[5].strip('][\n').split(', ')
                    for i in range(0,len(pedido_atual)):
                        pedido_atual[i] = int(pedido_atual[i].strip())
                    pedido_atual[4] -= quantidade_do_produto
                    lista[5] = str(pedido_atual)+'\n'
                    lista.append('\n%-4s'%quantidade_do_produto)
                    lista.append('- %-16s'%nome_do_produto)
                    lista.append('- Preço unitário: %-6s'%preço_unitário)
                    lista.append('Valor: - %3s'%remover)
                    lista.append(' - Cancelado')
                    arquivo = open(cpf+'.txt','w')
                    for i in range(0,len(lista)):
                        arquivo.writelines(lista[i])
                    arquivo.close()
                    print('\nCancelado com sucesso!\n')
                else:
                    print("\nNão é possível remover mais produtos do que os pedidos.\n")
            if codigo_do_produto == 6:
                if pedido_atual[5] >= quantidade_do_produto:
                    nome_do_produto = 'Refrigerante'
                    preço_unitário = 4.50
                    remover = preço_unitário * quantidade_do_produto
                    total = float(lista[4]) - remover
                    lista[4] = str(total)
                    lista[4] = (lista[4]+"\n")
                    lista[9] = ('Total: R$ {}\n'.format(total))
                    pedido_atual = lista[5].strip('][\n').split(', ')
                    for i in range(0,len(pedido_atual)):
                        pedido_atual[i] = int(pedido_atual[i].strip())
                    pedido_atual[5] -= quantidade_do_produto
                    lista[5] = str(pedido_atual)+'\n'
                    lista.append('\n%-4s'%quantidade_do_produto)
                    lista.append('- %-16s'%nome_do_produto)
                    lista.append('- Preço unitário: %-6s'%preço_unitário)
                    lista.append('Valor: - %3s'%remover)
                    lista.append(' - Cancelado')
                    arquivo = open(cpf+'.txt','w')
                    for i in range(0,len(lista)):
                        arquivo.writelines(lista[i])
                    arquivo.close()
                    print('\nCancelado com sucesso!\n')
                else:
                    print("\nNão é possível remover mais produtos do que os pedidos.\n")
            if codigo_do_produto == 7:
                if pedido_atual[6] >= quantidade_do_produto:
                    nome_do_produto = 'Suco natural'
                    preço_unitário = 6.25
                    remover = preço_unitário * quantidade_do_produto
                    total = float(lista[4]) - remover
                    lista[4] = str(total)
                    lista[4] = (lista[4]+"\n")
                    lista[9] = ('Total: R$ {}\n'.format(total))
                    pedido_atual = lista[5].strip('][\n').split(', ')
                    for i in range(0,len(pedido_atual)):
                        pedido_atual[i] = int(pedido_atual[i].strip())
                    pedido_atual[6] -= quantidade_do_produto
                    lista[5] = str(pedido_atual)+'\n'
                    lista.append('\n%-4s'%quantidade_do_produto)
                    lista.append('- %-16s'%nome_do_produto)
                    lista.append('- Preço unitário: %-6s'%preço_unitário)
                    lista.append('Valor: - %3s'%remover)
                    lista.append(' - Cancelado')
                    arquivo = open(cpf+'.txt','w')
                    for i in range(0,len(lista)):
                        arquivo.writelines(lista[i])
                    arquivo.close()
                    print('\nCancelado com sucesso!\n')
                else:
                    print("\nNão é possível remover mais produtos do que os pedidos.\n")
        else:
            print("Os dados não coincidem")
    print()

#5
#feito
#função apenas pega Total contido no arquivo
def valor_a_pagar():
    print()
    cpf = input('Digite o CPF: ')
    senha = input ('Digite a senha: ')
    if os.path.isfile(cpf+'.txt'):
        arquivo = open(cpf + '.txt', 'r')
        leitor = arquivo.read()
        lista = []
        lista = leitor.split()
        arquivo.close()
        if lista[3] == cpf and lista[4] == senha:
            print()
            print("O valor a pagar é R$ {}".format((lista[5]).strip()))
        else:
            print("Os dados não coincidem")
    else:
        print('\nEste CPF não foi cadastrado\n')
    print()

#6
#feito
#mostra o arquivo a partir da linha 8
def extrato():
    print()
    cpf = input('Digite o CPF: ')
    senha = input ('Digite a senha: ')
    if os.path.isfile(cpf+'.txt'):
        arquivo = open(cpf + '.txt', 'r')
        leitor = arquivo.read()
        lista = []
        lista = leitor.split()
        arquivo.close()
        if lista[3] == cpf and lista[4] == senha:
            arquivo = open(cpf + '.txt', 'r')
            lista = []
            for linha in arquivo.readlines():
                lista.append(linha)
            arquivo.close()
            print()
            for i in range(7,len(lista)):
                print(str(lista[i]).strip())
        else:
            print("Os dados não coincidem")
    else:
        print('\nEste CPF não foi cadastrado\n')
    print()

#7
#loop principal
def main():
    while True:
        intencao=int(input("1 - Novo Pedido\n2 - Cancela Pedido\n3 - Insere produto\n4 - Cancela produto\n5 - Valor do pedido\n6 - Extrato do pedido\n \n0 - Sair\n\nEscolha uma das opções: "))
        if intencao == 1:
            novopedido()
        elif intencao == 2:
            cancelapedido()
        elif intencao == 3:
            insereproduto()
        elif intencao == 4:
            cancelaproduto()
        elif intencao == 5:
            valor_a_pagar()
        elif intencao == 6:
            extrato()
        elif intencao == 0:
            print('\n\n\nObrigado pela preferencia!\n\nPrograma encerrado...\n\n\n')
            break
        else:
            print('\nEsta opção não existe\n')
main()