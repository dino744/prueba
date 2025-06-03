class Nivel:
    def __init__(self,mapa):
        self.secrem="pantalla"
        self.sprite_0="pared"
        self.sprite_1="camino"
        self.sprite_2="puerta"
        self.mapa=mapa

    def iniciar_mapa(self):
        for a in range (0,len(self.mapa)):
            for b in range (0,len(self.mapa[a])):
                for c in range (0,3):
                  print(2==self.mapa[a][b])
                  if 2==self.mapa[a][b]:
                     print(self.sprite_2)



tiled=[[0,0,0,0,0,0,0,0,0,0,0.0,0],
       [0,0,1,1,1,1,1,1,0,0,1.1,0],
       [1,1,1,0,0,0,0,1,0,0,0.1,0],
       [0,0,0,1,1,1,1,1,0,2,1.1,0],
       [0,0,0,1,0,0,0,0,0,1,0.0,0],
       [0,3,0,1,1,1,0,0,1,1,1.0,0],
       [0,1,0,0,0,1,0,0,1,0,1.0,0],
       [0,1,1,0,0,1,3,1,1,0,1.0,0],
       [0,0,1,1,1,2,1,1,0,0,1.1,1],
       [0,0,0,0,0,0,0,0,0,0,0.0,0]]

a=Nivel(tiled)
a.iniciar_mapa()

print("actu")