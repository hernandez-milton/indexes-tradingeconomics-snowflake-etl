# Proyecto ETL de Índices Bursátiles - Trading Economics & Snowflake

Este proyecto automatiza la extracción, procesamiento y carga de datos de índices bursátiles globales desde [Trading Economics](https://tradingeconomics.com/stocks) hacia una base de datos Snowflake, utilizando Apache Airflow como orquestador.

## Descripción

El pipeline realiza las siguientes tareas:
- **Extracción:** Obtiene tablas de índices bursátiles desde la web de Trading Economics.
- **Procesamiento:** Limpia y transforma los datos usando Pandas, asegurando la compatibilidad de los nombres de columnas con Snowflake.
- **Carga:** Guarda los datos en archivos CSV y los inserta en Snowflake mediante comandos SQL.
- **Orquestación:** Airflow gestiona la secuencia de tareas ETL, permitiendo la automatización y monitoreo del proceso.

## Herramientas Utilizadas

- **Python**: Scripts de extracción y procesamiento.
- **Pandas**: Limpieza y transformación de datos.
- **BeautifulSoup**: Parseo de tablas HTML.
- **Apache Airflow**: Orquestación de tareas ETL.
- **Snowflake**: Almacenamiento y consulta de datos.
- **SQL**: Scripts para carga y transformación en Snowflake.

## Estructura del Proyecto

```
AIRFLOW_DEPLOY/
│
├── dags/
│   ├── trading_index/
│   │   ├── index_tradingeconomics.py
│   │   └── queries/
│   │       ├── upload_stage_tradingeconomics.sql
│   │       └── ingest_table_tradingeconomics.sql
│   └── utils_index.py
│
├── local/
│   └── trading/
│       └── indexes_tradingeconomics.csv
│
└── tradingeconomics/
    └── tradingeconomics.ipynb
```

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Configura Airflow y Snowflake según tu entorno.

## Ejecución

1. Inicia Airflow y asegúrate de tener configuradas las variables y conexiones necesarias.
2. Ejecuta el DAG `TRADING_ECONOMICS` para iniciar el pipeline ETL.

## Personalización

- Puedes modificar el archivo `utils_index.py` para adaptar el procesamiento de datos según tus necesidades.
- Los scripts SQL pueden ajustarse para coincidir con la estructura de tus tablas en Snowflake.

## Licencia

Este proyecto está bajo la licencia MIT.

## Autor

Milton Hernández  
145373465+hernandez-milton@users.noreply.github.com
