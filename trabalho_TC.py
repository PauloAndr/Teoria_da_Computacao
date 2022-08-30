from tkinter import *

def E(estados, tabela_transicoes):
    S = set(estados)
    estados_nao_visitados = list(estados)
    while len(estados_nao_visitados) > 0:
        q = estados_nao_visitados.pop()
        if (q, 'epsilon') in tabela_transicoes:
            novos = tabela_transicoes[(q, 'epsilon')].difference(S)
            S.update(novos)
            estados_nao_visitados.extend(novos)
    return S


def afn(Q, Sigma, tabela_transicoes, q0, F, cadeia):
    QA = E({q0}, tabela_transicoes)
    for s in cadeia:
        novos_estados_ativos = set()
        for q in QA:
            if (q, s) in tabela_transicoes:
                novos_estados_ativos.update(E(tabela_transicoes[(q, s)], tabela_transicoes))
        QA = novos_estados_ativos
    return len(QA.intersection(F)) != 0


tabela_transicoes = {('q1', '0'): {'q1'}, ('q1', '1'): {'q1', 'q2'}, ('q2', '0'): {'q3'}, ('q2', '1'): {'q3'}, ('q3', '0'): {'q4'},
         ('q3', '1'): {'q4'}}

print(afn(['q1', 'q2', 'q3', 'q4'], ['0', '1'], tabela_transicoes, 'q1', {'q4'}, '00001100'))

