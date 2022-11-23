import unittest
import LecturaImagenes as le
import colores as co
class Test_lectura(unittest.TestCase):

    def test_solicitarImagenYPasarlaAMatriz(self):
        '''
        Funcion que solicita la imagen y la pasa a matriz, solo verificamos que esta sea leida correctamente.'''
        imagen_fuente = le.solicitarImagenYPasarlaAMatriz()
        self.assertTrue(imagen_fuente)
    
    def test_tipodefigura(self):
        le.tipo_de_figura(3)
        self.assertEqual(le.tipo_de_figura(3), "T")
    
    def test_aislarFigura(self):
        '''
        test para probar la funcion aislarFigura al comprobar que arroje una imagen
        '''
        imagen_fuente = le.solicitarImagenYPasarlaAMatriz()
        colores_fuente, fondo_fuente = co.escaneoDeColores(imagen_fuente)
        colores_fuente = list(colores_fuente)
        color = colores_fuente[0]
        figura_aislada = le.aislarFigura(color, fondo_fuente, imagen_fuente)
        self.assertTrue(figura_aislada)       
    
    def test_escaneoDeColores(self):
        '''
        test para probar la funcion escaneoDeColores
        '''
        imagen_fuente = le.solicitarImagenYPasarlaAMatriz()
        colores_fuente, fondo_fuente = co.escaneoDeColores(imagen_fuente)
        self.assertEqual(type(colores_fuente), type(set()))
    
    def test_hexadecimal(self):
        '''
        test para probar la funcion hexadecimal
        '''
        imagen_fuente = le.solicitarImagenYPasarlaAMatriz()
        colores_fuente, fondo_fuente = co.escaneoDeColores(imagen_fuente)
        colores_fuente = list(colores_fuente)
        color = colores_fuente[0]
        hex_color = co.hexadecimal(color)
        self.assertEqual(type(hex_color), type(str()))
        

    
if __name__ == '__main__':
    unittest.main()
 #python3 -m unittest test_lectura.py
