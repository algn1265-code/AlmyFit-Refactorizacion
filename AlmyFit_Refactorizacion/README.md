# Almy Fit — Laboratorio 2: Refactorización

Aplicación académica en Python + SQLite para ventas e inventario. No requiere Docker ni servidor de base de datos.

## Requisitos
- Python 3.10+
- Visual Studio Code recomendado
- Git para evidenciar el trabajo colaborativo

SQLite viene incluido en Python; no se instalan paquetes adicionales.

## Ejecutar
Desde esta carpeta:
```bash
python main.py
```
Para pruebas:
```bash
python -m unittest discover -s tests -v
```

La aplicación crea `almyfit.db` automáticamente. El inventario inicial es ficticio y sirve para demostrar el flujo.

## Estructura
- `main.py`: menú de consola.
- `almyfit/database.py`: conexión y esquema.
- `almyfit/repository.py`: persistencia y consultas parametrizadas.
- `almyfit/services.py`: validaciones y reglas de negocio.
- `tests/test_services.py`: pruebas normales y de error.
- `docs/EVIDENCIAS.md`: capturas recomendadas.

## GitHub
Usen commits reales de ambos integrantes, ramas y Pull Request cuando aplique. No inventen enlaces ni contribuciones.
El diagnóstico del informe corresponde a un diseño inicial simplificado, ya que no se proporcionó un repositorio previo para inspeccionar.

## Instalación y ejecución

### Requisitos previos
- Python 3.10 o superior.
- Git, para clonar el repositorio.
- Visual Studio Code (opcional, recomendado para editar el proyecto).

### Descargar el proyecto

Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/algn1265-code/AlmyFit-Refactorizacion.git
cd AlmyFit-Refactorizacion
```

Si los archivos del programa están dentro de la carpeta `AlmyFit_Refactorizacion`, entra en ella antes de continuar:

```bash
cd AlmyFit_Refactorizacion
```

### Ejecutar la aplicación

Inicia el programa desde la terminal:

```bash
python main.py
```

La aplicación presenta un menú de consola con las siguientes opciones:

1. Ver inventario.
2. Registrar venta.
3. Consultar resumen mensual.
4. Consultar ranking de ganancias.
5. Salir.

### Ejecutar las pruebas automáticas

Para verificar el comportamiento del sistema, ejecuta:

```bash
python -m unittest discover -s tests -v
```

Las pruebas comprueban casos como la consulta del inventario, el registro de ventas, la validación de cantidades, el rechazo de ventas con existencias insuficientes y la validación del mes consultado.

### Base de datos

El proyecto utiliza SQLite, una base de datos integrada en Python, por lo que no requiere instalar PostgreSQL ni configurar Docker.

### Estructura del proyecto

- `main.py`: punto de entrada y menú de la aplicación.
- `almyfit/`: lógica de negocio, acceso a datos y servicios.
- `tests/`: pruebas automatizadas.
- `README.md`: documentación del proyecto.

## Objetivo del proyecto

Almy Fit busca mejorar la organización de las ventas y el inventario de un negocio de ropa deportiva femenina mediante una aplicación de consola desarrollada en Python, con separación de responsabilidades y validaciones para reducir errores.