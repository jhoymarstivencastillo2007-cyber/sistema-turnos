# Sistema de Turnos para Atención Estudiantil

## 1. Nombre de la aplicación
**Sistema de Turnos para Atención Estudiantil**

## 2. Descripción no técnica del problema
En la oficina de atención a estudiantes se generan filas largas de espera para realizar diversos trámites académicos y administrativos. Sin un sistema organizado, se presentan problemas como el desorden en la atención, discusiones sobre quién llegó primero y falta de equidad en el servicio. Se requiere un mecanismo digital sencillo para registrar a los estudiantes conforme van llegando y atenderlos estrictamente en ese mismo orden.

## 3. Descripción de la solución
Se desarrolló una aplicación en Python ejecutada desde la consola que permite gestionar el flujo de estudiantes en tiempo real. El programa ofrece opciones para:
1. Registrar a un estudiante con su nombre y el motivo de su visita.
2. Atender al siguiente estudiante en la fila, mostrando sus datos en pantalla.
3. Consultar la lista general de estudiantes en espera.
4. Finalizar la jornada.

Además, el sistema valida límites como evitar la atención si la fila está vacía y negar nuevos registros cuando se alcanza la capacidad máxima permitida (5 estudiantes).

## 4. Estructura de datos seleccionada
Se seleccionó una **Cola (Queue)** implementada mediante un vector/lista dinámica en Python (`cola = []`), donde cada elemento es un diccionario con la estructura `{"nombre": str, "motivo": str}`.

## 5. Justificación técnica de la elección
La estructura de **Cola** funciona bajo el principio **FIFO** (*First In, First Out*), lo que garantiza técnicamente que el primer elemento ingresado mediante la operación `append()` sea el primero en salir con la operación `pop(0)`. Esta propiedad refleja de forma exacta el comportamiento real de una fila de atención, asegurando la equidad del proceso con un consumo mínimo de memoria.

## 6. Análisis de lo que ocurriría al utilizar otra estructura
* **Pila (Stack / LIFO):** Si se usara una Pila (*Last In, First Out*), el último estudiante en llegar sería el primero en ser atendido, dejando a los primeros atrapados al final de la fila.
* **Vector Simple sin lógica FIFO:** Si se permitiera el acceso y eliminación aleatoria por índices, se perdería el control de llegada y el operador podría atender a cualquier persona sin respetar el orden.
* **Matriz / Lista Enlazada:** Una matriz agregaría complejidad innecesaria. Una lista enlazada optimizaría las eliminaciones al frente, pero para una capacidad de 5 elementos la diferencia de rendimiento con una lista simple es imperceptible.

## 7. Instrucciones para ejecutar el programa
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/jhoymarstivencastillo2007-cyber/sistema-turnos.git](https://github.com/jhoymarstivencastillo2007-cyber/sistema-turnos.git)

 ## 8. Casos de prueba utilizados
* **Flujo Normal:** Se ingresan 3 estudiantes (ej. Juan, María, Carlos). Al seleccionar "Atender", el sistema extrae a Juan por haber sido el primero en llegar.
* **Caso Límite 1 (Cola Vacía):** Al intentar atender sin estudiantes, el sistema muestra: `"La cola está vacía. No hay estudiantes para atender."`
* **Caso Límite 2 (Capacidad Máxima):** Se registran 5 estudiantes. Al intentar ingresar un 6.º estudiante, el sistema rechaza el registro con: `"La cola está llena. No se puede agregar otro estudiante."`

## 9. Limitaciones y posibles mejoras
* **Limitaciones:**
  * Almacenamiento volátil en memoria RAM (los datos se borran al cerrar).
  * Capacidad fija estática limitada a 5 registros.
  * La operación `pop(0)` en listas estándar de Python requiere reindexar elementos $O(n)$.
* **Posibles Mejoras:**
  * Implementar la librería `collections.deque` para optimizar operaciones al frente a $O(1)$.
  * Integrar almacenamiento en Base de Datos o archivos JSON.
  * Desarrollar una interfaz gráfica de usuario (GUI).
