def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  quant = 0
  trocas = 0

  if len(figurinhas_da_maria) <= len(figurinhas_do_joao):
    while figurinhas_da_maria != figurinhas_do_joao:
     trocas = len(figurinhas_da_maria)
     break
   
    maria = sorted(set(figurinhas_da_maria))
    for i in  range(len(maria)):
     for j in range(len(figurinhas_do_joao)):
      if maria[i] == figurinhas_do_joao[j]:
        quant += 1
       
        trocas = len(maria) - quant
           
  else:
     if len(figurinhas_do_joao) <= len(figurinhas_da_maria):
       while figurinhas_do_joao != figurinhas_da_maria:
         trocas = len(figurinhas_do_joao)
         break

       joao = sorted(set(figurinhas_do_joao))
       for i in range(len(joao)):
         for j in range(len(figurinhas_da_maria)):
           if joao[i] == figurinhas_da_maria[j]:
             quant += 1
             trocas = len(joao) - quant
  
  return trocas        
         
if __name__ == '_main_':
  A, B = input().split(' ')
  figurinhas_da_maria = input().split(' ')
  figurinhas_da_joao = input().split(' ')
  trocas = maximizar_troca_de_figurinhas(figurinhas_da_maria,figurinhas_da_joao)
  print(f"{trocas}")