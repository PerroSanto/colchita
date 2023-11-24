from PIL import Image
import cv2
import numpy

def procesar(code):
    # convertir de str a objeto 
    code = eval(code) 
    code.show()

def sew(retazo1, retazo2):
    error = Image.open("./error/error.png").resize((100, 100))
    retazo1_array = numpy.array(retazo1)
    retazo2_array = numpy.array(retazo2)
    alto1 = retazo1_array.shape[0]
    alto2 = retazo2_array.shape[0]
    if alto1 == alto2:
        retazo_array = numpy.concatenate((retazo1_array, retazo2_array), axis=1)
        nuevo_retazo = Image.fromarray(retazo_array)
        return nuevo_retazo
    else:
        return error
  
def turn(retazo):
    retazo_array = numpy.array(retazo)
    retazo_array = cv2.rotate(retazo_array, cv2.ROTATE_90_CLOCKWISE)
    nuevo_retazo = Image.fromarray(retazo_array)
    return nuevo_retazo
  

# Coser 4 retazos
a = Image.open("./retazos/a.png").resize((100, 100))
b = Image.open("./retazos/b.png").resize((100, 100))
c = Image.open("./retazos/c.png").resize((100, 100))
d = Image.open("./retazos/d.png").resize((100, 100))
e = Image.open("./retazos/e.png").resize((100, 100))
f = Image.open("./retazos/f.png").resize((100, 100))
g = Image.open("./retazos/f.png").resize((100, 100))
