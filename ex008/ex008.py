studentGrade = eval(input(f'Insira a nota para saber sua situação escolar: '))

if(studentGrade >= 7):
    print(f'Parabéns, você foi aprovado!')
elif 5 <= studentGrade :
    print(f'Você está de recuperação.')
else:
    print(f'Você está reprovado.')