
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Mensaje:
    def __init__(self, remitente, destinatario, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido

class SistemaMensajeria:
    def __init__(self):
        self.usuarios = []
        self.mensajes = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def enviar_mensaje(self, remitente, destinatario, contenido):
        mensaje = Mensaje(remitente, destinatario, contenido)
        self.mensajes.append(mensaje)

    def mostrar_mensajes(self):
        for m in self.mensajes:
            print("De:", m.remitente.nombre, "Para:", m.destinatario.nombre, "-", m.contenido)

# Ejemplo de uso
sistema = SistemaMensajeria()
u1 = Usuario("Ana")
u2 = Usuario("Luis")
sistema.agregar_usuario(u1)
sistema.agregar_usuario(u2)
sistema.enviar_mensaje(u1, u2, "Hola Luis")
sistema.enviar_mensaje(u2, u1, "Hola Ana")
sistema.mostrar_mensajes()
