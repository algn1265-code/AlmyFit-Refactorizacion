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
