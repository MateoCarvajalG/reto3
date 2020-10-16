#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:30:04 2020

@author: mateo
"""


def ruteo(distancias: dict, ruta_inicial: list)-> dict:

#------- FUNCION QUE CALCULA LA SUMA DE LA DISTANCIA DE CUALQUIERA RUTA-----------    
    def suma_rutas(ruta_inicial):
        distancia_ruta=0
        for i in range(len(ruta_inicial)-1):
            pareja = [ruta_inicial[i],ruta_inicial[i+1]]
            pareja= pareja[0] , pareja[1]
            distancia_punto = distancias[pareja] 
            distancia_ruta = distancia_ruta + distancia_punto
        return distancia_ruta
#-------------CICLO PARA REVISAR LOS DATOS DE ENTRADA-------------------------    
    for pd in distancias :
        if pd[0]== pd[1]:
            if distancias[pd] != 0:
                return"Por favor revisar los datos de entrada."
                break
        if pd[0] != pd[1]   : 
            if distancias[pd] < 1:
                return"Por favor revisar los datos de entrada."
                break
    mejoro = True 
    inc=1
    p2=0
    ruta_intercambiada=ruta_inicial.copy()   #lista1=lista2.copy()
    suma_inicial=(suma_rutas(ruta_inicial))
    mejor_ruta=[]
#---------------- CICLO PARA CALCULAR LA MEJOR RUTA---------------------
#----------------CUANDO LA RUTA NO MEJORE SE ACABA EL CICLO WHILE---------------
    while mejoro !=False :
            #-----SE SEPARA EL ORIGEN DE LA TUPLA (A ,B) : A----------
        for p1 in range(len(ruta_inicial)-3):
            k=ruta_inicial[p1+1]
            inc=inc+1 
            t=3+p1
                #--- SE SEPARA EL DESTINO DE LA TUPLA PARA COMPARAR CADA VALOR 
                #--- CON EL DESTINO 1ER i (A,B) 2do i (A,C)------------------
            for p2 in range(len(ruta_inicial)-t):
                q = ruta_inicial[p2+inc]
                pareja = k , q
                ruta_intercambiada[p2+inc]=k
                ruta_intercambiada[p1+1]=q
                #--- SE SUMA LA RUTA INTERCAMBIANDO LOS VALORES  Y SE COMPARA 
                #--- CON LA RUTA INICIAL PARA VER SI ES MEJOR----------------
                suma_iterativa = (suma_rutas(ruta_intercambiada))
                if suma_iterativa < suma_inicial :
                    mejor_ruta= ruta_intercambiada.copy()
                    ruta_intercambiada=ruta_inicial.copy()
                    suma_inicial=suma_inicial
                    suma_inicial=suma_iterativa
                else:
                    ruta_inicial= ruta_inicial.copy()
                    ruta_intercambiada=ruta_inicial.copy()        
        if not(mejor_ruta == ruta_inicial):
            mejoro=True
            ruta_inicial=mejor_ruta.copy()
            t=0
            inc=1
            ruta_intercambiada=ruta_inicial.copy()
        else:
            mejoro=False
            
    mejor_ruta="-".join(mejor_ruta)   
    resultado={
        'ruta' : mejor_ruta,
        'distancia': suma_inicial
        }
    return resultado
    
ruta_inicial= ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']

distancias= {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

print(ruteo(distancias, ruta_inicial))
