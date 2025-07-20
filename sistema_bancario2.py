#menu principal opão para acessar contas ja cadastradas ou criar contas e cadastrar clientes
menu_main = """
[1] acesso a cntas cadastradas
[2] cadastrar contas e clientes
[3] listar clientes e contas
[4] sair
=>"""

# menu de opções  para operações de contas ja cadastradas
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """
#menu para cadastrar contas e clientes
menu2 = """
[u] cadastrar cliente
[c] criar conta 
[q] sair
=>"""

menu3 = """
[l] listar clientes
[lc] listar contas
[q] sair
=>"""

conta_num = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
excedeu_saldo = bool 
excedeu_limite = bool
excedeu_saques = bool
clientes =[] # ou clientes = list() ambas as formas declaram uma lista
contas = []
id_usuario = 0
id_conta = 0
cliente_cadastrado = []
conta_encontrada =[]


# dados para teste:

# clientes.append({"id":1,"nome":"jairo","data_nasc":"12/12/2000","cpf":"12","endereco":"rua 1,99-jardim p - sao paulo/sp"})
# clientes.append({"id":2,"nome":"cesar","data_nasc":"12/12/2000","cpf":"123","endereco":"rua 1,99-jardim p - sao paulo/sp"})
# clientes.append({"id":3,"nome":"jose","data_nasc":"12/12/2000","cpf":"1234","endereco":"rua 1,99-jardim p - sao paulo/sp"})
# clientes.append({"id":4,"nome":"jose","data_nasc":"12/12/2000","cpf":"12345","endereco":"rua 1,99-jardim p - sao paulo/sp"})

# dados para teste:

# contas.append({"numero_da_conta":1,"agencia":"0001","cliente":"jairo","cpf":"12"})
# contas.append({"numero_da_conta":2,"agencia":"0001","cliente":"cesar","cpf":"123"})
# contas.append({"numero_da_conta":3,"agencia":"0001","cliente":"jose","cpf":"1234"})
# contas.append({"numero_da_conta":4,"agencia":"0001","cliente":"jose","cpf":"12345"})

# def cliente(nome,data_nasc,cpf,endereco):
#    return {"nome":nome,"data_nasc":data_nasc,"cpf":cpf,"endereco":endereco}
      
# print(cliente("jairo","12/12/2000","123456789","rua 1"))


#função achar cliente
def achar_cliente(cpf):
    for clie in clientes:
        if clie["cpf"] == cpf:
            return clie # retorna um discionario com os dados de cliete encontrado pelo cpf
    return None   

def achar_conta(conta):
    for c in contas:
        if c["numero_da_conta"] == conta:
            return c # retorna um discionario com os dados de cliete encontrado pelo cpf
    return None   


#função criar  cliente           
def criar_cliente(nome,data_nasc,cpf,endereco):   
    cliente_cadastrado = achar_cliente(cpf)
   
    if cliente_cadastrado is not None: # se não for none, é porque ja tem clientes cadastrados e armazenados na lista
        print("temos clientes cadastrados  aproximadamente", len(clientes))

        if cpf == cliente_cadastrado["cpf"]:
            print("cliente ja esta cadastrado cpf:" , cliente_cadastrado["cpf"],"nome:",cliente_cadastrado["nome"])
    else:
        print("\nnão temos nehum cliente cadastrado com o cpf:",cpf, "nome:",nome, "\n o mesmo sera cadastrado agora \n")
        if len(clientes) == 0:
                id_usuario = 1
                clientes.append({"id":id_usuario,"nome":nome,"data_nasc":data_nasc,"cpf":cpf,"endereco":endereco})
                print(f"\n usuario cadastrado:")
                print(f"\n nome: {nome}\n data de nascimento: {data_nasc}\n cpf: {cpf}\n endereço: {endereco}")
        else:
                id_usuario = len(clientes) + 1
                clientes.append({"id":id_usuario,"nome":nome,"data_nasc":data_nasc,"cpf":cpf,"endereco":endereco})
                print(f"\n usuario cadastrado:")
                print(f"\n nome: {nome}\n data de nascimento: {data_nasc}\n cpf: {cpf}\n endereço: {endereco}")
       

       


#função listar clientes
def listar_clientes():
    if len(clientes) == 0:
        print("não temos clientes cadastrados")
    else:    
        for clie in clientes:     
            print("\n")
            print("ID: ",clie.get("id"))
            print("Nome: ",clie.get("nome"))
            print("data de nascimento: ",clie.get("data_nasc"))
            print("Cpf: ",clie.get("cpf"))
            print("Endereço: ", clie.get("endereco"))
            print("\n==============================")
        

#função criar conta
def criar_conta(cliente):
    

    cliente_cadastrado = achar_cliente(cliente)
    
    if len(contas) == 0:
        id_conta = 1
        print ("id da conta:",id_conta)
    else:
        id_conta = len(contas) + 1
        print ("numero da conta:",id_conta)
        

    if cliente_cadastrado is None:
        print("usuario nao encontrado: ")
    else:            

        if cliente_cadastrado["cpf"] == cliente:
            agencia = "0001"
            numero_da_conta = id_conta
            contas.append({"numero_da_conta":numero_da_conta,"agencia": agencia,"cliente":cliente_cadastrado["nome"],"cpf":cliente_cadastrado["cpf"]})
            print("\n conta cadastrada com sucesso ")
            print("\n agencia: ",agencia,"\n numero da conta: ",numero_da_conta,"\n cliente: ",cliente_cadastrado ["nome"])
        else:
            print("usuario",usuario," nao encontrado")
   
   
def listar_contas():

    if len(contas) == 0:
        print("não temos contas cadastradas")
    else:

        for conta in contas:     
            print("\n")
            print("numero da conta: ",conta.get("numero_da_conta"))
            print("agencia: ",conta.get("agencia"))
            print("cliente: ",conta.get("cliente"))
            print("Cpf: ",conta.get("cpf"))
            print("\n==============================")    
            
           



def depositar(conta,saldo,extrato,/): # o argumento nessa configurajção com o ,/ obriga o mesmo a ser passa por posição ,
    # porem na linha acima vai ser indiferente, pois a função so pede um argumento em sua chamada
    # global saldo, extrato
    conta_encontrada =achar_conta(conta)

    if conta_encontrada is None:
        print("conta nao encontrada")
    else:
       
        valor = float(input("Informe o valor do depósito: "))
      
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"


        else:
            print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato        

# função sacar:
def sacar(*,valor,saldo,extrato,numero_saques,excedeu_saldo,excedeu_limite, excedeu_saques,LIMITE_SAQUES):
    # na linha acima o *, obriga oas argumento a serem passados usando o conceito de argumento nomeado      

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES
            
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


#função extrato:
def movimentacoes(conta,extrato,/,*,saldo):
    # na linha acima usamos o ,/, que tudo antes dele deve ser passado por posições e o
    #  *, obriga oas argumento a serem passados usando o conceito de argumento nomeado
   
   
    conta_encontrada = achar_conta(conta)

    if conta_encontrada is None:
        print("conta nao encontrada")
        return
    else:
        if conta == conta_encontrada["numero_da_conta"]:
            cliente = conta_encontrada["cliente"]
            numero_conta = conta_encontrada["numero_da_conta"]

            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"cliente: {cliente}\nconta: {numero_conta}")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
        else:
             print("para acessar serviços de outra conta, reinicie o sistema")



while True:
    opcao_main = input(menu_main)
    saldo = 0
    extrato = ""
    numero_saques = 0

    if opcao_main == "1":  
        conta_num = int(input("digite o numero da conta que deseja acessar: \n"))

        if achar_conta(conta_num) is None:
            print("conta nao encontrada")

        else:    

         while True:  
        
            

            opcao = input(menu)
                     
            if opcao == "d":
               saldo, extrato = depositar(conta_num,saldo,extrato)


            elif opcao == "s":
                
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar( 
                    valor=valor ,
                    saldo = saldo,
                    extrato = extrato,
                    numero_saques = numero_saques,
                    excedeu_saldo = excedeu_saldo,
                    excedeu_limite = excedeu_limite,
                    excedeu_saques = excedeu_saques,
                    LIMITE_SAQUES = LIMITE_SAQUES)
            
            elif opcao == "e":                
                movimentacoes(conta_num,extrato,saldo=saldo)

            elif opcao == "q":
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")


    elif opcao_main == "2":


        while True:
            opcao = input(menu2)
            if opcao == "u": # criar cliente
                nome = input("Informe o nome do cliente: ")
                data_nasc = input("Informe a data de nascimento do cliente: ")
                cpf = input("Informe o cpf do cliente: ")
                while True:
                    endereco = input("Informe o endereco do cliente: ")
                    partes = endereco.split("-")
                    if len(partes) == 3 and "/" in partes[2].strip():
                        break
                    else:
                        print("\n Endereço inválido! Siga o formato: rua, número - bairro - cidade/UF\n")

                criar_cliente(nome,data_nasc,cpf,endereco)
            elif opcao == "c": # criar conta
                # agencia = input("Informe o numero da agencia: ")
                # numero_conta = input("Informe o numero da conta: ")
                usuario = input("Informe o cpf do usuario: ")
                criar_conta(usuario)
            elif opcao == "q":
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")    
    
    elif opcao_main == "3":
          while True:
            opcao_list = input(menu3)
            if opcao_list == "l":
                listar_clientes()   

            elif opcao_list == "lc":
                listar_contas()    

            elif opcao_list == "q":
                break
    elif opcao_main == "4":    
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")            
   