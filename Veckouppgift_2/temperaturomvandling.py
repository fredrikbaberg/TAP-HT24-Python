# Version 1
input_temperature = input("Skriv in en temperatur i grader Celcius: ")
print("Det blir {} grader Farenheit".format((float(input_temperature)*9/5)+32))

# Version 2
input_format = input("Ange enhet för indata (C/F): ")
if input_format not in ['C', 'F']:
    print("Felaktig indata, måste vara 'C' eller 'F'. Avslutar.")
    quit()
input_temperature = input("Skriv in en temperatur i grader {}: ".format(input_format))
temperature_in = float(input_temperature)

if(input_format == 'C'): # Omvandla till F.
    temperature_out = (temperature_in*9/5)+32
else: # Omvandla till C.
    temperature_out = (temperature_in-32)*5/9
print("Det blir {} grader {}".format(temperature_out, input_format))

# Version 3
if( input_format == 'C' and temperature_in < 10 or input_format == 'F' and temperature_out < 10):
    print("Bäst att ta på sig vinterkläder!")
if( input_format == 'C' and temperature_in >= 20 or input_format == 'F' and temperature_out >= 20):
    print("Du borde packa badkläder.")
