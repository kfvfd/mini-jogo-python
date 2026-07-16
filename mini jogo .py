print("--- BEM-VINDO AO SOBREVIVENCIA NA ESTRADA---")
print("seu carro quebrou no meio do nada a noite")
print("Voce esta com sede e o estresse esta subindo.\n")

#o jogasdor faz a primeira escolha
print("opções")
print("1-beber a agua do radiador(que esta suja e quente)")
print("2-procurar ferramentas no porta malas")
print("3-ir andando ate o posto de combustivel no escuro")
esxolha = input("\n0 oque voce vai fazer? (digite 1,2 ou 3)")
#o computador começa a testar as decisoues
if esxolha=="2" :
    print("\n[SUCCESO]voce achou uma ferramenta no porta-malas" )
elif esxolha=="1":
    print("\n[errofeio]a agua do radiador estavasuja e quente vc se queimou!" )
elif esxolha=="3":
    print("\n[erro de doido ]vc foi anadando ate o posto mais proximo,vc achou um carro pensou que tinha alquem la mais nao tinha ninhguem no posto" )
#mantem a janela aberta
input(" \nAPERTE ENTER PARA SAIR DO JOGO..." )
