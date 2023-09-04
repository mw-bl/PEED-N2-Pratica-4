# Marcos Willian :D

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valores):
        if not valores:
            return

        fila = []
        valor_index = 0

        if self.raiz is None:
            self.raiz = No(valores[0])
            fila.append(self.raiz)
            valor_index += 1

        while fila:
            no_atual = fila.pop(0)

            if valor_index < len(valores):
                valor_esquerda = valores[valor_index]
                valor_index += 1
                if valor_esquerda is not None:
                    no_atual.esquerda = No(valor_esquerda)
                    fila.append(no_atual.esquerda)

            if valor_index < len(valores):
                valor_direita = valores[valor_index]
                valor_index += 1
                if valor_direita is not None:
                    no_atual.direita = No(valor_direita)
                    fila.append(no_atual.direita)

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, no):
        if no is None:
            return 0
        altura_esquerda = self._altura(no.esquerda)
        altura_direita = self._altura(no.direita)
        return max(altura_esquerda, altura_direita) + 1

    def contar_nos_internos(self):
        return self._contar_nos_internos(self.raiz)

    def _contar_nos_internos(self, no):
        if no is None:
            return 0
        if no.esquerda or no.direita:
            return 1 + self._contar_nos_internos(no.esquerda) + self._contar_nos_internos(no.direita)
        else:
            return 0

    def contar_folhas(self):
        return self._contar_folhas(self.raiz)

    def _contar_folhas(self, no):
        if no is None:
            return 0
        if no.esquerda is None and no.direita is None:
            return 1
        else:
            return self._contar_folhas(no.esquerda) + self._contar_folhas(no.direita)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if valor < no.valor:
            return self._buscar(no.esquerda, valor)
        else:
            return self._buscar(no.direita, valor)

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            self._mostrar_pre_ordem_recursivo(self.raiz)

    def _mostrar_pre_ordem_recursivo(self, no):
        if no is not None:
            print(no.valor, end=" ")
            self._mostrar_pre_ordem_recursivo(no.esquerda)
            self._mostrar_pre_ordem_recursivo(no.direita)

    def mostrar_in_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            self._mostrar_in_ordem_recursivo(self.raiz)

    def _mostrar_in_ordem_recursivo(self, no):
        if no is not None:
            self._mostrar_in_ordem_recursivo(no.esquerda)
            print(no.valor, end=" ")
            self._mostrar_in_ordem_recursivo(no.direita)

    def mostrar_pos_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            self._mostrar_pos_ordem_recursivo(self.raiz)

    def _mostrar_pos_ordem_recursivo(self, no):
        if no is not None:
            self._mostrar_pos_ordem_recursivo(no.esquerda)
            self._mostrar_pos_ordem_recursivo(no.direita)
            print(no.valor, end=" ")


valores = [5, 3, 7, 2, 4, 6, 8]
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(valores)

print("Raiz da árvore:", arvore.raiz.valor)
print("Altura da árvore:", arvore.altura())
print("Nós internos na árvore:", arvore.contar_nos_internos())
print("Folhas na árvore:", arvore.contar_folhas())

busca_valor = 4
if arvore.buscar(busca_valor):
    print(f"\nO número {busca_valor} está presente na árvore.")
else:
    print(f"\nO número {busca_valor} não está presente na árvore.")

# Pré-ordem
print("\nPré-ordem:")
arvore.mostrar_pre_ordem()
print()

# In-ordem
print("In-ordem:")
arvore.mostrar_in_ordem()
print()

# Pós-ordem
print("Pós-ordem:")
arvore.mostrar_pos_ordem()
print()
