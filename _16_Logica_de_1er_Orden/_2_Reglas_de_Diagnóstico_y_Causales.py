# Variables que representan los síntomas del paciente
tiene_fiebre = True
tiene_tos = True
tiene_dolor_de_garganta = False
# Reglas de diagnóstico
if tiene_fiebre and tiene_tos and tiene_dolor_de_garganta:
    print("El paciente tiene síntomas de gripe.")
elif tiene_fiebre and tiene_tos:
    print("El paciente podría tener una infección respiratoria.")
elif tiene_fiebre:
    print("El paciente podría tener una infección sin especificar.")
else:
    print("El paciente no parece tener síntomas graves.")
# Reglas causales 
if tiene_fiebre:
    print("La fiebre puede ser causada por diversas enfermedades, consulte a un médico para un diagnóstico preciso.")
if tiene_tos:
    print("La tos podría deberse a una infección respiratoria o alergia, consulte a un médico para un diagnóstico adecuado.")
if tiene_dolor_de_garganta:
    print("El dolor de garganta podría ser el resultado de una infección viral o bacteriana, consulte a un médico para un diagnóstico y tratamiento adecuados.")
