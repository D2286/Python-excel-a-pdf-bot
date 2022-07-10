import pyautogui as main

# Coordenas, condicionales y prompts para insertar en array de (coordenadas)

empresas = ["EMPRESA_A","EMPRESA_B","EMPRESA_C"]
estado_civil= [(551,344),(599,345),(567,345)]
genero_sexo = [(693,344),(704,344)]
posiciones = [(447,345),(341,376),(454,375),(631,346),(344,390),(506,373),(344,415)]
coordenadas = []

def empresa(a,b):
    array [a.append(b[0]) if btn_empresa == "EMPRESA_A" else a.append(b[1]) if btn_empresa  == ""EMPRESA_B"" else a.append(b[2]) if btn_empresa  == "EMPRESA_C"  for i in b]
    return array
    
def estado(a,b): 
    coordenadas = [a.append(b[0]) if estado_c == "Soltero" else a.append(b[1]) if estado_c  == "Unión L." else a.append(b[2]) if estado_c  == "Casado"  for i in b]
    
def genero(a,b):
    coordenadas = [a.append(b[0]) if input_genero == "Masculino" else a.append(b[1]) for i in b]
    return coordenadas

# función para final de preparación - lista de coordenadas concatenada
def data_position(a):
    estado(a, estado_civil)
    genero(a, genero_sexo)
    return_ubicacion = a + posiciones
    return return_ubicacion

btn_empresa = main.confirm('Empresa', buttons=['EMPRESA_A', 'EMPRESA_B', 'EMPRESA_C'])   
btn_estado = main.confirm('Estado Civil', buttons=['Soltero', 'Unión L.', 'Casado'])
btn_genero = main.confirm('GENERO', buttons=['Femenino', 'Masculino'])
