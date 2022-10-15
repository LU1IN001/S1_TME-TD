#show_image(draw_line(-0.5, 0.2, 0.7, -0.5))

def dessine_carre(x: float, y: float, c: float) -> Image:
    """
    Préconditions x et y entre -1 et 1 et c<=1 et c >=0
    retourne l'image du carré de cote c et coin inférieur gauche indique
    """
    return overlay(draw_line(x,y, x+c, y), draw_line(x,y,x,y+c), draw_line(x, y+c, x+c, y+c) , draw_line(x+c, y, x+c, y+c))

#show_image(dessine_carre(0,0,1))

def image_2(x: float, y:float, c:float) -> Image:
    return overlay(dessine_carre(x,y,c), draw_line(x,y+c/2, x+c, y+c/2))

def image_3(x:float, y: float, c: float) -> Image:
    return overlay(dessine_carre(x,y,c), fill_triangle(x,y,x,y+c,x+c,y+c))

def image_4(x: float, y: float, c: float) -> Image:
    return overlay(dessine_carre(x,y,c), fill_triangle (x,y,x+c/2,y+c/2,x,y+c))

def image_5(x:float, y:float, c:float) -> Image:
    return overlay(dessine_carre(x,y,c), fill_triangle (x+c,y,x+c/2,y+c/2,x+c,y+c))

def image_6(x: float, y:float, c:float) -> Image:
    return overlay(dessine_carre(x,y,c), draw_ellipse(x,y+c,x+c,y))

def image_7(x: float, y:float, c:float) -> Image:
    return overlay(dessine_carre(x,y,c), fill_ellipse (x,y+c,x+c,y))

def image_8(x: float, y:float, c:float) -> Image:
    return overlay(dessine_carre(x,y,c), image_4(x,y,c), image_5(x,y,c))

def image_9(x: float, y:float, c:float) -> Image:
    return overlay(fill_ellipse(x-c/2,y+c,x+c/2,y), fill_ellipse(x+c/2,y+c,x+1.5*c,y),fill_triangle(x,y,x-c,y,x,y+c,"white"),fill_triangle(x,y+c,x-c,y,x-c,y+c,"white"), fill_triangle(x+c,y,x+c,y+c,x+2*c,y+c, "white"), fill_triangle(x+c,y,x+2*c,y,x+2*c,y+c, "white"), dessine_carre(x,y,c))

show_image(image_9(0,0,0.2))



