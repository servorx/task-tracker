# Project URL

https://roadmap.sh/projects/task-tracker

# 📝 Task Tracker CLI

**Task Tracker** es una aplicación de línea de comandos (CLI) diseñada para ayudarte a gestionar y organizar tus tareas de forma sencilla y rápida desde la terminal. Con esta herramienta podrás registrar lo que necesitas hacer, lo que estás haciendo y lo que ya has completado. Este proyecto es ideal para practicar habilidades como el manejo del sistema de archivos, la captura de entradas del usuario y la construcción de aplicaciones CLI básicas.

---

## ✅ Requisitos

- La aplicación debe ejecutarse desde la línea de comandos.
- Debe aceptar argumentos posicionales para realizar acciones como agregar, actualizar, eliminar o listar tareas.
- Las tareas deben almacenarse en un archivo `tasks.json` en el directorio actual.
- El archivo JSON debe crearse automáticamente si no existe.
- Solo se permite usar módulos nativos del lenguaje (no librerías o frameworks externos).
- El programa debe manejar errores y casos extremos de forma adecuada.

---

## ⚙️ Funcionalidades

El usuario podrá realizar las siguientes acciones:

- **Agregar tareas**
- **Actualizar tareas**
- **Eliminar tareas**
- **Marcar tareas como en progreso**
- **Marcar tareas como completadas**
- **Listar todas las tareas**
- **Listar tareas por estado**


Cada tarea incluye las siguientes propiedades:
- `id`: Identificador único
- `description`: Descripción breve
- `status`: Estado de la tarea (`todo`, `in-progress`, `done`)
- `createdAt`: Fecha y hora de creación
- `updatedAt`: Fecha y hora de la última actualización
