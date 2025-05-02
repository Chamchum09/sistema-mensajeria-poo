class Usuario:
    def __init__(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nombre

class Mensaje:
    def __init__(self, remitente, destinatario, contenido):
        if not contenido:
            raise ValueError("El contenido del mensaje no puede estar vacío")
        self.remitente = remitente
        self.destinatario = destinatario
        self.contenido = contenido

class SistemaMensajeria:
    def __init__(self):
        self.usuarios = []
        self.mensajes = []

    def agregar_usuario(self, usuario):
        if usuario in self.usuarios:
            print(f"El usuario {usuario.nombre} ya está registrado.")
        else:
            self.usuarios.append(usuario)

    def enviar_mensaje(self, remitente, destinatario, contenido):
        if remitente not in self.usuarios or destinatario not in self.usuarios:
            print("Error: uno de los usuarios no está registrado.")
            return
        mensaje = Mensaje(remitente, destinatario, contenido)
        self.mensajes.append(mensaje)

    def mostrar_mensajes(self):
        if not self.mensajes:
            print("No hay mensajes.")
            return
        for m in self.mensajes:
            print(f"De: {m.remitente.nombre} Para: {m.destinatario.nombre} - {m.contenido}")

# Ejemplo de uso
sistema = SistemaMensajeria()
u1 = Usuario("Ana")
u2 = Usuario("Luis")
sistema.agregar_usuario(u1)
sistema.agregar_usuario(u2)
sistema.enviar_mensaje(u1, u2, "Hola Luis")
sistema.enviar_mensaje(u2, u1, "Hola Ana")
sistema.mostrar_mensajes()
