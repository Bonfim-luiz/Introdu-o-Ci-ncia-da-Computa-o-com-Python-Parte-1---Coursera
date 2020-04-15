segundos=int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias=segundos//86400
resto1=segundos%86400
horas=resto1//3600
resto2=resto1%3600
minutos=resto2//60
resto3=resto2%60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",resto3,"segundos.")
