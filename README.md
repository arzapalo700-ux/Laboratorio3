# Laboratorio 3: Creación de Modelos, Migraciones y Formsets en Django

Este repositorio contiene la solución e implementación del **Laboratorio N° 3** para la asignatura de **Desarrollo de Aplicaciones Empresariales**.

## 📌 Descripción del Proyecto
La aplicación `quiz` gestiona exámenes, preguntas y opciones mediante el ORM de Django, vistas basadas en funciones, plantillas HTML y validación personalizada de reglas de negocio en la capa de formularios.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.14
* **Framework:** Django 6.1.1
* **Base de Datos:** SQLite
* **Control de Versiones:** Git & GitHub

## 🚀 Características e Implementación
* **Modelos (`models.py`):**
  * `Exam`: Registra los exámenes (título, descripción, fecha de creación).
  * `Question`: Entidad dependiente de un examen, con enunciado y campo numérico de puntaje (`score`).
  * `Choice`: Entidad dependiente de una pregunta para almacenar el texto de las alternativas y la marca `is_correct`.
* **Migraciones:**
  * Estructura inicial declarada y ejecutada en `0001_initial.py`.
  * Evolución de la base de datos para incorporar el nuevo atributo `score` en `Question`.
* **Formsets y Validaciones (`forms.py`):**
  * Implementación de `inlineformset_factory` junto con un `BaseInlineFormSet` personalizado.
  * Regla de negocio mediante el método `clean()`: Garantiza que **exactamente una opción** sea marcada como correcta por cada pregunta.

## ⚙️ Instrucciones de Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone: https://github.com/arzapalo700-ux/Laboratorio3.git
