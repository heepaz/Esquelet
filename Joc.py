import pygame
from jugador import Jugador


# Definim una Classe que contingui totes les variables del Joc
class Joc(object):
    # Definim una funció main que serà la funció princiàl del joc
    def main(self, pantalla):
        # Desem les característiques de la finestra
        self.amplada = pantalla.get_width()
        self.alçada = pantalla.get_height()
        # Creem un rellotge per comptar el temps
        rellotge = pygame.time.Clock()
        # De moment no volem sortir del joc
        self.surt = False

        # Creem un jugador a partir d'imatge, velocitats i acceleracions
        self.jugador = Jugador("Imatges/Jugador.png", 400, 300, 500, 500)
        # Creem un grup d'sprites que només contindrà en jugador
        self.grup_jugador = pygame.sprite.GroupSingle(self.jugador)

        # Mentre no sortim repetim tota la seqüència
        while not self.surt:
            # Mirem quant temps (dt) ha passat des de l'última vegada
            # i limitem el nombre de cicles a 30 per segon
            dt = rellotge.tick(30)
            # Gestionem els esdeveniments
            self.gestiona_esdeveniments()
            # Actualitzem els sprites segons els esdeveniments ocorreguts
            self.update(dt/1000)
            # Pintem els sprites a la pantalla
            self.draw(pantalla)

    # Gestionem alguns esdeveniments generals i derivem la gestió
    # d'esdeveniments més especialitzats
    def gestiona_esdeveniments(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.surt = True
            elif event.type == pygame.KEYDOWN:
                self.gestiona_pressió(event)
            elif event.type == pygame.KEYUP:
                self.gestiona_alliberament(event)

    # Gestionem els esdeveniments de pressió de tecles
    def gestiona_pressió(self, event):
        if event.key == pygame.K_ESCAPE:
            self.surt = True
        elif event.key == pygame.K_RIGHT:
            self.jugador.dreta = True
        elif event.key == pygame.K_LEFT:
            self.jugador.esquerra = True
        elif event.key == pygame.K_UP:
            self.jugador.amunt = True
        elif event.key == pygame.K_DOWN:
            self.jugador.avall = True

    # Gestionem els esdeveniments d'alliberament de tecles
    def gestiona_alliberament(self, event):
        if event.key == pygame.K_RIGHT:
            self.jugador.dreta = False
        elif event.key == pygame.K_LEFT:
            self.jugador.esquerra = False
        elif event.key == pygame.K_UP:
            self.jugador.amunt = False
        elif event.key == pygame.K_DOWN:
            self.jugador.avall = False

    # Definim la funció que actualitza tots els grups d'sprite
    def update(self, dt):
        # Passem a la funció d'actualitzar-se no només el temps
        # sinó el joc sencer "self" en aquest cas
        self.grup_jugador.update(dt, self)

    # Pintem tots el fons i els sprites a la pantalla
    # Finalment actualitzem la pantalla
    def draw(self, pantalla):
        pantalla.blit(pygame.Surface((self.amplada, self.alçada)), (0, 0))
        self.grup_jugador.draw(pantalla)
        pygame.display.flip()

# Si executem directament aquest fitxer
if __name__ == '__main__':
    # Iniciem el pygame
    pygame.init()
    # Definim les mides de la nostra finestra
    amplada = 800
    alçada = 600
    # Creem una pantalla
    pantalla = pygame.display.set_mode((amplada, alçada))
    # Creem un Joc
    Joc().main(pantalla)
    # Quan acabi el joc, sortim del pygame
    pygame.quit()
