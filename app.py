import os

#o programa deve ser instalado na mesma pasta onde você quer que fique a pasta "tickets"

class Ticket:

    """

    Essa classe representa um ticket

    parâmetros:
    ticket (string): o número do ticket.

    """

#o problema é que do jeito que está, se a funçãp ProcurarDiretorio retornar None, a função Criar irá dar erro. Como corrigir?
    def __init__(self, ticket):
        self.ticket = ticket
        self.pasta_atual = os.getcwd()
        self.diretorio = os.path.join(self.pasta_atual, 'tickets')
        #self.diretorio = self.ProcurarDiretorio()
        self.caminho_pasta = os.path.join(self.diretorio, self.ticket)
        self.nome_arquivo = f'{self.ticket}.txt'
        self.caminho_arquivo = os.path.join(self.caminho_pasta, self.nome_arquivo)
   
    #def ProcurarDiretorio(self, nome = "Tickets" , pasta = "."):
     #   
      #  for dirpath, dirnames, filenames in os.walk(pasta):
       #     if nome in dirnames:
        #        return os.path.join(dirpath, nome)

        #return None

    def Existe(self):
        return os.path.exists(self.caminho_pasta)

    def Criar(self):

        try:
            os.makedirs(self.diretorio, exist_ok=True)        
            os.makedirs(self.caminho_pasta)

            with open(self.caminho_arquivo,"x") as arquivo:
                os.startfile(self.caminho_pasta)
                os.startfile(self.caminho_arquivo)
   
        except:

            return "crie uma pasta chamada Tickets para utilizar o sistema"

    def Pesquisar(self):

        os.startfile(self.caminho_pasta)
        os.startfile(self.caminho_arquivo)