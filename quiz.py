import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

questoes = [
    {
        "pergunta" : "Qual é a capital da França?", 
        "opcoes"   : ["Paris", "Londres", "Berlim", "Roma"],
        "resposta" : "Paris"
    },
    {
        "pergunta" : "Qual é o resultado de 8 + 5?",
        "opcoes"   :  ["12", "13", "15", "18"],
        "resposta" : "13"
    },
    {
        "pergunta" : "Quem pintou a Mona Lisa?", 
        "opcoes"   : ["Picasso", "Da Vinci", "Van Gogh", "Warhol"],
        "resposta" : "Da Vinci"
    },
    {
        "pergunta" : "Quanto é 6 multiplicado por 7?", 
        "opcoes"   : ["36", "42", "48", "54"],
        "resposta" : "42"
    },
    {
        "pergunta" : "Qual é o maior planeta do sistema solar?",
        "opcoes"   :  ["Marte", "Saturno", "Júpiter", "Vênus"],
        "resposta" :  "Jupiter"
    }
]


#função para verificar resposta e gerar pergunta
def verificar_resposta(opcao_selecionada):
    global pergunta_atual, pontuacao
    if opcao_selecionada == questoes[pergunta_atual]["resposta"]:
        pontuacao +=1 
    pergunta_atual +=1

    if pergunta_atual < len(questoes):
        atualizar_pergunta()
    else:
        pontuacao_final()


# atualizar perguntas e opçoes
def atualizar_pergunta():
    configurando_pergunta.config(text=questoes[pergunta_atual]["pergunta"]) #'get' para puxar informação para tela
    for i, opcao in enumerate(questoes[pergunta_atual]["opcoes"]):
        botoes_opcoes[i].config(text=opcao, command=lambda op=opcao: verificar_resposta(op))
        '''
            command=lambda 
            - O uso de lambda nesse contexto é essencial para garantir que cada botão chame a função verificar_resposta
            com o valor correto de choice. 
            Sem o uso de lambda, todos os botões chamariam a função com o mesmo valor de choice 
            (o último valor de choice no loop).

        '''
    
def pontuacao_final(): #mostrar mensagem ao usuário -> message ## obs
    messagebox.showinfo('PONTUAÇÃO FINAL!', f'{pontuacao}/{len(questoes)}')
    janela.quit()




#configurando tela
janela = ttk.Window(themename='solar')
janela.title('Quiz!')


#variaveis 
pergunta_atual = 0 #controlar qual pergunta esta sendo apresentada / deve ser colocada abaixo da função

pontuacao = 0 #deve ser colocada abaixo da função 

botoes_opcoes = []

soma_pontos = 0

#configurando layout de perguntas e botões
configurando_pergunta = ttk.Label(janela, width = 30, text=questoes[pergunta_atual]["pergunta"], bootstyle='inverse-info')
configurando_pergunta.pack(pady=10)

for i in range(4):
    btn = ttk.Button(janela, width = 30, text='', bootstyle=SUCCESS)
    btn.pack(pady=10)
    botoes_opcoes.append(btn)



#chamando funções

atualizar_pergunta()


janela.mainloop()