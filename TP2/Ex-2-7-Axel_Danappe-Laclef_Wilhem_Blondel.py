def tour(x: float, y:float, hauteur_etage: float, largeur_etage_1:float, largeur_etage_2: float) -> Image:
    """
    Préconditions: x >= -1 et x <= 1 et y >= -1 et y <= 1 hauteur_etage > 0, largeur_etage_1 et largeur_etage_2 > 0
    Construit une tour au cordonnée indiquée sur le coin inférieur gauche (x;y)
    """
    return overlay(rectangle(x, y, largeur_etage_1, hauteur_etage), rectangle(x+largeur_etage_1/2-largeur_etage_2/2, y+hauteur_etage, largeur_etage_2, hauteur_etage))

def rectangle(x: float, y: float, l: float, h: float) -> Image:
    """
    Préconditions: x >= -1 et x <= 1 et y >= -1 et y <= 1 l > 0 et h > 0
    Construit un rectangle rempli à partir des coordonnées du point inférieur gauche
    """
    return overlay(fill_triangle(x,y,x+l,y,x+l,y+h),fill_triangle(x,y,x,y+h,x+l,y+h))

show_image(overlay(tour(-0.5,-0.5,0.2,0.4,0.1), tour(0,-0.5,0.1,0.5,0.3)))

    
