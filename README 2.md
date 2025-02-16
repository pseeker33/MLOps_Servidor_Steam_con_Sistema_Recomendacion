# 🚀 Steam Recommendations API

API desarrollada con **FastAPI** para analizar y proporcionar recomendaciones personalizadas de juegos de **Steam**. Utiliza múltiples datasets en formato **Parquet** para realizar análisis avanzados sobre usuarios, géneros, desarrolladores y reseñas.

## 📊 Funcionalidades

- **Recomendaciones Personalizadas**: Basadas en el análisis de comportamiento y preferencias de los usuarios.
- **Análisis de Reseñas**: Procesa y analiza reseñas de juegos para identificar patrones y sentimientos.
- **Búsqueda de Juegos**: Consulta juegos por género, desarrollador, popularidad y más.
- **Similitud de Usuarios**: Encuentra usuarios con gustos similares.
- **Optimización de Recursos**: Manejo eficiente de memoria y grandes volúmenes de datos.

## 📂 Estructura del Proyecto

```
steam-api/
├── data/                   # Archivos Parquet
├── notebooks/              # Análisis exploratorio y preprocesamiento
├── app/
│    ├── main.py            # Punto de entrada principal (FastAPI)
│    ├── routes/            # Endpoints de la API
│    ├── services/          # Lógica de negocio
│    └── utils/             # Funciones auxiliares
└── requirements.txt        # Dependencias del proyecto
```

## 🛠️ Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/steam-api.git
   cd steam-api
   ```

2. Crear y activar un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Ejecución

1. Asegúrate de tener los archivos Parquet en `data/`.

2. Iniciar la API de FastAPI:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Acceder a la documentación interactiva en:

   [http://localhost:8000/docs](http://localhost:8000/docs)

## 📌 Endpoints Principales

- `/recommendations` - Obtener recomendaciones personalizadas.
- `/games` - Buscar juegos por parámetros específicos.
- `/users/similarity` - Identificar usuarios con gustos similares.
- `/reviews/analysis` - Análisis de sentimientos en las reseñas.

## 📊 Datasets

Asegúrate de tener los datasets en formato **Parquet** en el directorio `data/`.

- Información de juegos (nombre, género, desarrollador, etc.).
- Reseñas de usuarios.
- Historial de interacciones.

## 🧹 Mantenimiento y Optimización

- Liberación de memoria después de cargar grandes volúmenes de datos.
- Validación de entradas en los endpoints.
- Logs detallados para rastrear el rendimiento y errores.

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

🤖 **Contribuciones bienvenidas**. Si tienes ideas para mejorar las recomendaciones o el análisis, ¡abre un issue o envía un PR!

