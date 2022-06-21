class televisão:
    canais = [3,10,11,17,25,52,65,82,92]

    def __init__(self,modelo,cor,tamanho,largura,ligada=False,volume=50,canal=0,funcionando=True):
        self.modelo = modelo
        self.cor = cor
        self.tamanho = tamanho
        self.largura = largura
        self.ligada = ligada
        self.volume = volume
        self.canal = canal
        self.funcionando = funcionando


    #Ligando / desligando a televisão
    def ligar(self):
        if self.ligada and self.funcionando == True:
            print("a televisão ja está ligada")
            return
        if not self.ligada and self.funcionando == False:
            print("televisão está quebrada!")
            return
        if self.ligada == False and self.funcionando == True:
            print("ligando a televisão")
            self.ligada = True
            return

    def desligar(self):
        if not self.ligada and self.funcionando ==True:
            print("A televisão já esta desligada")
            return
        if not self.ligada and self.funcionando == False:
            print("Televisão está quebrada!")
            return

        if self.ligada and self.funcionando == True:
            print("Desligando a televisão")
            self.ligada=False
            return

    #aumentar volume ou diminui volume
    def botãovolume(self,botão,press=1):
        if self.ligada == True and self.funcionando == True:
            if botão == "+":
                self.volume += press
                print(self.volume)
                return
            elif botão == "-":
                self.volume -= press
                print(self.volume)
                return
            else:
                print("Botão não encontrado!")
                return
        else:
            if self.funcionando == False:
                print("Televisão quebrada.")
            else:
                print("Televisão Esta Desligada!")

    #analise de canal
    def botãoCanal(self, botão,press=1):
        if self.ligada == True and self.funcionando== True:
            if botão == "+":
                self.canal += press
                print(self.canal)

            elif botão == "-":
                if self.canal >= 0:
                    self.canal -= press
                    print(self.canal)
                else:
                    print("Apenas canal positivos!")
            else:
                print("Botão não encontrado!")
                return

            if self.canal in self.canais:
                print(f"Voce está conectado no canal {self.canal}")
            else:
                print(f"estação {self.canal} não possui sinal!")
        else:
            if self.funcionando == False:
                print("Televisão quebrada.")
            else:
                print("Televisão está desligada")
    
    def quebrar(self):
        if not self.funcionando:
            print(f"sua televisão {self.modelo} já está quebrada")
            return

        print(f"sua televisão {self.modelo} quebrou.")
        self.funcionando= False
        self.ligada= False
        
    
    def consertar(self):
        if self.funcionando:
            print(f"Sua televisão ja está funcionando.")
            return

        print(f"consertei sua televisão {self.modelo}.")
        self.funcionando= True
        


#Comandos 
#Ligar e Desligar //     aumentar canal/volume usando + ou - e o numero de vezes  // quebrar e consertar 


t1 = televisão("sansung","preto",400,500)
t1.ligar()




