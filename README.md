# Graficacion-apuntes-de-clase-unidad-1
Apuntes de clase del temario


## Introducción a la Graficación por Computadora

Este repositorio contiene el desarrollo teórico y práctico de la **Unidad I**, enfocado en los fundamentos de la graficación por computadora, su evolución, aplicaciones, bases matemáticas y prácticas realizadas en Blender.

---

# 1. Introducción a la Graficación por Computadora

La **graficación por computadora** es la disciplina que estudia la creación, manipulación y representación de imágenes mediante el uso de algoritmos y sistemas computacionales.

Permite transformar datos matemáticos en representaciones visuales, siendo base de áreas como:

* Videojuegos
* Animación digital
* Diseño asistido por computadora (CAD)
* Realidad virtual
* Simulación científica

---

## 1.1 Historia y Evolución de la Graficación por Computadora

### Década de 1950–1960

* Primeros gráficos generados por computadoras.
* Uso en investigación militar y científica.
* Pantallas vectoriales monocromáticas.

### Década de 1970

* Aparición del modelado 3D.
* Desarrollo del algoritmo de rasterización.
* Inicio del CAD.

### Década de 1980

* Introducción del color.
* Interfaces gráficas (GUI).
* Primeras películas con gráficos digitales.

### Década de 1990

* Tarjetas gráficas (GPU).
* Modelado y animación avanzados.
* Nacimiento del renderizado realista.

### 2000–Actualidad

* Renderizado en tiempo real.
* Realidad virtual y aumentada.
* Inteligencia artificial aplicada al diseño.
* Software como Blender democratiza la producción 3D.

---

## 1.2 Áreas de Aplicación

La graficación por computadora se utiliza en múltiples sectores:

| Área            | Aplicación                       |
| --------------- | -------------------------------- |
| Entretenimiento | Videojuegos, cine animado        |
| Ingeniería      | Diseño de piezas y simulaciones  |
| Arquitectura    | Visualización de edificios       |
| Medicina        | Reconstrucciones anatómicas      |
| Educación       | Simuladores interactivos         |
| Ciencia         | Visualización de datos complejos |

---

## 1.3 Aspectos Matemáticos de la Graficación

La base de la graficación es matemática.

### Principales conceptos:

* **Vectores:** Representan posición y dirección en el espacio.
* **Matrices:** Permiten transformaciones (rotación, escala, traslación).
* **Trigonometría:** Utilizada para curvas, cámaras y animación.
* **Geometría Analítica:** Define formas mediante ecuaciones.
* **Interpolación:** Permite suavizar animaciones.
* **Álgebra Lineal:** Base del renderizado 3D.

Ejemplo:
Una rotación en 3D se calcula mediante matrices de transformación aplicadas a los vértices del objeto.

---

## 1.4 Modelos del Color: RGB, CMY, HSV y HSL

Los modelos de color permiten representar colores numéricamente.

### RGB (Red, Green, Blue)

* Modelo aditivo (pantallas).
* Mezcla luz.
* Usado en monitores y gráficos digitales.

### CMY (Cyan, Magenta, Yellow)

* Modelo sustractivo (impresión).
* Mezcla pigmentos.

### HSV (Hue, Saturation, Value)

* Basado en percepción humana.
* Facilita seleccionar colores visualmente.

### HSL (Hue, Saturation, Lightness)

* Variante de HSV.
* Mejor control de iluminación.

---

### Práctica: Iluminación de un Cubo en Blender

**Objetivo:** Comprender cómo la luz afecta el color y volumen.

#### Pasos:

1. Abrir Blender.
2. Eliminar el cubo inicial y crear uno nuevo.
3. Añadir una luz:

   * `Shift + A → Light → Point`.
4. Mover la luz a un costado del cubo.
5. Cambiar potencia en propiedades de luz (ej. 1000W).
6. Activar modo renderizado.
7. Cambiar material del cubo:

   * Ajustar Base Color.
   * Modificar Roughness y Metallic.
8. Observar cómo cambian sombras y volumen.

**Aprendizaje:**
La iluminación define profundidad, percepción del material y realismo.

---

## 1.5 Representación y Trazo de Líneas y Polígonos

Los gráficos están formados por primitivas básicas:

* Punto → Unidad mínima.
* Línea → Conexión entre dos puntos.
* Polígono → Figura cerrada compuesta por líneas.
* Malla → Conjunto de polígonos en 3D.

### Algoritmos importantes:

* Algoritmo de Bresenham (trazado de líneas).
* Rasterización de polígonos.
* Relleno por scanline.

Estos algoritmos convierten ecuaciones en píxeles visibles.

---

### Prácticas Realizadas

#### Dibujo de un Polígono

Se generó una figura mediante vértices definidos matemáticamente y conectados en secuencia.

Concepto aplicado:
Representación geométrica mediante coordenadas cartesianas.

<img width="812" height="457" alt="image" src="https://github.com/user-attachments/assets/5a166994-e644-4c77-94eb-1e5f05a40308" />


#### Construcción de la “Flor de la Vida”

Se trazaron múltiples circunferencias con radio constante y centros equidistantes.

Conceptos aplicados:

* Simetría
* Repetición geométrica
* Uso de funciones trigonométricas

<img width="698" height="459" alt="image" src="https://github.com/user-attachments/assets/89a8197f-f8ef-4031-b0ff-1fcc4342600c" />


---

### 1.5.1 Formatos de Imagen

Los formatos almacenan la información gráfica de diferentes maneras.

| Formato | Características                  |
| ------- | -------------------------------- |
| PNG     | Sin pérdida, ideal para gráficos |
| JPEG    | Comprimido, usado en fotografía  |
| BMP     | Sin compresión                   |
| TIFF    | Alta calidad profesional         |
| SVG     | Basado en vectores               |
| EXR     | Alto rango dinámico (HDR)        |

---

## 1.6 Procesamiento de Mapas de Bits

Un **mapa de bits** es una imagen formada por una matriz de píxeles.

Cada píxel contiene:

* Color
* Intensidad
* Posición

### Procesos comunes:

* Escalado
* Filtrado
* Compresión
* Corrección de color
* Antialiasing
* Detección de bordes

Estos procesos permiten mejorar calidad visual y optimizar almacenamiento.

---

# Bibliografía

Foley, J. D., Van Dam, A., Feiner, S. K., & Hughes, J. F. (2014). *Computer graphics: Principles and practice*. Pearson.

Hearn, D., & Baker, M. P. (2011). *Computer graphics with OpenGL* (4th ed.). Pearson.

Blender Foundation. (2024). *Blender manual*. https://docs.blender.org/manual

Shirley, P. (2016). *Fundamentals of computer graphics* (4th ed.). CRC Press.

Gonzalez, R. C., & Woods, R. E. (2018). *Digital image processing* (4th ed.). Pearson.

---

# Conclusión

La graficación por computadora combina matemáticas, programación y percepción visual para construir representaciones digitales del mundo real o imaginado.
El estudio de sus fundamentos permite comprender cómo se generan imágenes, cómo se representan los objetos y cómo herramientas como Blender utilizan estos principios para crear entornos tridimensionales complejos.


