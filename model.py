# Clase Project: Gestiona un proyecto audiovisual
class Project:
    def _init_(self, nombre, cliente, fecha_inicio, fecha_entrega):
        self.nombre = nombre
        self.cliente = cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_entrega = fecha_entrega
        self.estado = "Planeado"
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def mostrar_progreso(self):
        return f"Proyecto '{self.nombre}' - Estado: {self.estado}, Tareas: {len(self.tareas)}"

# Clase TeamMember: Representa un miembro del equipo
class TeamMember:
    def _init_(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        self.asignado_a = None
    
    def asignar_a_proyecto(self, proyecto):
        self.asignado_a = proyecto
        print(f"{self.nombre} ha sido asignado al proyecto {proyecto.nombre} como {self.rol}")

# Clase Equipment: Representa el equipo audiovisual
class Equipment:
    def _init_(self, tipo, id_equipo, estado="Disponible"):
        self.tipo = tipo
        self.id_equipo = id_equipo
        self.estado = estado
    
    def asignar_a_proyecto(self, proyecto):
        if self.estado == "Disponible":
            self.estado = "Asignado"
            print(f"Equipo {self.tipo} (ID: {self.id_equipo}) asignado al proyecto {proyecto.nombre}")
        else:
            print(f"Equipo {self.tipo} (ID: {self.id_equipo}) no está disponible.")

# Clase ResourceManager: Gestiona la asignación de recursos (equipo y personal)
class ResourceManager:
    def _init_(self):
        self.equipos = []
        self.miembros_equipo = []
    
    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
    
    def agregar_miembro(self, miembro):
        self.miembros_equipo.append(miembro)
    
    def mostrar_equipos_disponibles(self):
        disponibles = [eq for eq in self.equipos if eq.estado == "Disponible"]
        return f"Equipos disponibles: {[eq.id_equipo for eq in disponibles]}"
    
    def mostrar_miembros_disponibles(self):
        disponibles = [miembro for miembro in self.miembros_equipo if miembro.asignado_a is None]
        return f"Miembros disponibles: {[miembro.nombre for miembro in disponibles]}"

# Clase Client: Representa a un cliente y su interacción con los proyectos
class Client:
    def _init_(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.proyectos = []
    
    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
    
    def revisar_progreso(self):
        for proyecto in self.proyectos:
            print(proyecto.mostrar_progreso())

# Clase Budget: Gestiona los costos de cada proyecto
class Budget:
    def _init_(self, proyecto, costo_inicial):
        self.proyecto = proyecto
        self.costo_inicial = costo_inicial
        self.gastos = 0
    
    def agregar_gasto(self, cantidad):
        self.gastos += cantidad
    
    def calcular_rentabilidad(self):
        rentabilidad = self.costo_inicial - self.gastos
        return f"Rentabilidad del proyecto '{self.proyecto.nombre}': {rentabilidad}"

# Clase TrendAnalyzer: Sugiere mejoras basadas en tendencias del mercado
class TrendAnalyzer:
    def _init_(self):
        self.tendencias = ["Realidad Virtual", "Video 4K", "Transmisión en Vivo"]
    
    def sugerir_mejoras(self, proyecto):
        sugerencia = self.tendencias[0]  # Simplemente devuelve la primera tendencia como ejemplo
        print(f"Para el proyecto '{proyecto.nombre}', se sugiere incorporar: {sugerencia}")

# Clase Report: Genera informes de proyectos
class Report:
    def _init_(self, proyecto):
        self.proyecto = proyecto
    
    def generar_informe(self):
        informe = f"Informe del proyecto: {self.proyecto.nombre}\n"
        informe += f"Estado: {self.proyecto.estado}\n"
        informe += f"Cliente: {self.proyecto.cliente.nombre}\n"
        informe += f"Número de tareas: {len(self.proyecto.tareas)}\n"
        return informe


# Ejemplo de uso del sistema
if __name__ == "_main_":
    # Crear un cliente
    cliente1 = Client("Empresa XYZ", "contacto@xyz.com")

    # Crear un proyecto
    proyecto1 = Project("Video Corporativo", cliente1, "2024-01-01", "2024-01-31")
    cliente1.asignar_proyecto(proyecto1)

    # Crear miembros del equipo
    miembro1 = TeamMember("Juan Pérez", "Fotógrafo")
    miembro2 = TeamMember("María López", "Editor de Video")

    # Crear equipo audiovisual
    equipo1 = Equipment("Cámara", "C001")
    equipo2 = Equipment("Micrófono", "M001")

    # Crear un administrador de recursos y asignar recursos
    gestor_recursos = ResourceManager()
    gestor_recursos.agregar_miembro(miembro1)
    gestor_recursos.agregar_miembro(miembro2)
    gestor_recursos.agregar_equipo(equipo1)
    gestor_recursos.agregar_equipo(equipo2)

    # Asignar equipo y miembros al proyecto
    miembro1.asignar_a_proyecto(proyecto1)
    equipo1.asignar_a_proyecto(proyecto1)

    # Añadir una tarea al proyecto
    proyecto1.agregar_tarea("Grabación de escenas en exteriores")

    # Mostrar progreso del proyecto
    print(proyecto1.mostrar_progreso())

    # Calcular el presupuesto del proyecto
    presupuesto1 = Budget(proyecto1, 5000)  # Costo inicial de 5000
    presupuesto1.agregar_gasto(1000)  # Gastos en equipo
    print(presupuesto1.calcular_rentabilidad())

    # Revisar tendencias del mercado
    analizador_tendencias = TrendAnalyzer()
    analizador_tendencias.sugerir_mejoras(proyecto1)

    # Generar un informe del proyecto
    informe1 = Report(proyecto1)
    print(informe1.generar_informe())