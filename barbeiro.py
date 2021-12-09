from random import random, uniform
from time import sleep
import secrets
from threading import Thread, Lock

atendimento = [0, 0, 0, 0, 0]  # 0 = nao atendido , 1 = atendido


class Barbeiro(Thread):
    execute = True  # variável para realizar a execução

    def __init__(self, nome, atual, proxima):  # Construtor da classe barbeiro
        Thread.__init__(self)
        self.nome = nome
        self.atual = atual
        self.proxima = proxima
        self.servicos = [{ "nome": "cabelo", "tempo": 1},{ "nome": "Barba", "tempo": 6},{ "nome": "Bigode", "tempo": 3} ]

    def run(self):
        while self.execute:
            print(f"\n {self.nome} está esperando")
            sleep(uniform(5, 15))
            servico = secrets.choice(self.servicos)
            self.atendimento(servico["tempo"], servico["nome"])


    def atendimento(self,tempo,servico):

        atual, proxima = self.atual, self.proxima

        while self.execute:  # enquanto tiver executando
            atual.acquire(True)  # tenta ser atendido
            # verifica se esta ocupado
            locked = proxima.acquire(False)
            if locked:
                break
            atual.release()  # libera o barbeiro
        else:
            return  # volta a fila

        print(f"\n {self.nome} está {servico}")
        sleep(tempo)
        print(f"\n {self.nome} finalizou o atendimento\n")
        # contabiliza o número de vezes que cada cliente foi atendido
        atendimento[nomes.index(self.nome)] += 1
        print(f"Atendimeto {atendimento}")
        atual.release()  # libera a vaga
        proxima.release()  # proximo na fila

nomes = ['Capitão América', 'Homem Aranha', 'Pantera Negra',
         'Doutor estranho', 'Shang chi']  # Nomes dos cliente

fila = [Lock() for _ in range(5)]

cadeira = [Barbeiro(nomes[i], fila[i % 5], fila[(i + 1) % 5])
           for i in range(5)]

for _ in range(20):
    Barbeiro.execute = True  # Inicia a execução
    for cliente in cadeira:
        try:
            cliente.start()  # inicia o objeto de thread criado.
            sleep(2)
        except RuntimeError:  # Se a thread já tiver sido iniciada
            pass
    sleep(uniform(5, 15))
    Barbeiro.execute = False  # Para a execução
