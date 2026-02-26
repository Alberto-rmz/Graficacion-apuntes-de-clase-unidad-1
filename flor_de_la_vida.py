import bpy
import math

# Limpiar escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Parámetros de la figura
radio = 2
angulo_actual = 0
paso = 20  # Cada 60 grados para obtener 6 círculos alrededor

bpy.ops.mesh.primitive_circle_add(
radius=radio,
location=(0,0,0)
)
while angulo_actual<360:
    angulo_radianes = math.radians(angulo_actual)
    x = radio * math.cos(angulo_radianes)
    y = radio * math.sin(angulo_radianes)
    
    bpy.ops.mesh.primitive_circle_add(
        radius=radio,
        location=(x, y, 0)
    )
    
    angulo_actual+= paso


