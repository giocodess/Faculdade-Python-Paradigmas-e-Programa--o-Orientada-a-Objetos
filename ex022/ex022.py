def aceitador():
    while(True):
        print(f'Aceita namorar comigo?')
        x = input(f' (S/N) S ou N?: ')
        if(x == "sim"):
            break
        
aceitador()