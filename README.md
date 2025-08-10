# Proyecto ETL de Índices Bursátiles - Trading Economics & Snowflake

Este proyecto automatiza la extracción, procesamiento y carga de datos de índices bursátiles globales desde [Trading Economics](https://tradingeconomics.com/stocks) hacia una base de datos Snowflake, utilizando Apache Airflow como orquestador y Docker para facilitar la ejecución y despliegue.

## Descripción

El pipeline realiza las siguientes tareas:
- **Extracción:** Obtiene tablas de índices bursátiles desde la web de Trading Economics.
- **Procesamiento:** Limpia y transforma los datos usando Pandas, asegurando la compatibilidad de los nombres de columnas con Snowflake.
- **Carga:** Guarda los datos en archivos CSV y los inserta en Snowflake mediante comandos SQL.
- **Orquestación:** Airflow gestiona la secuencia de tareas ETL, permitiendo la automatización y monitoreo del proceso.
- **Despliegue:** Docker permite ejecutar todo el entorno de Airflow y dependencias de forma sencilla y reproducible.

## Herramientas Utilizadas

- **Python**: Scripts de extracción y procesamiento.
- **Pandas**: Limpieza y transformación de datos.
- **BeautifulSoup**: Parseo de tablas HTML.
- **Apache Airflow**: Orquestación de tareas ETL.
- **Snowflake**: Almacenamiento y consulta de datos.
- **SQL**: Scripts para carga y transformación en Snowflake.
- **Docker**: Contenerización y despliegue

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
    git clone https://github.com/tu_usuario/tradingeconomics-snowflake-etl.git
    ```
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Configura Airflow y Snowflake según tu entorno.

## Ejecución con Docker

1. Asegúrate de tener [Docker](https://www.docker.com/) instalado.
2. Construye la imagen y levanta los servicios:
    ```bash
    docker-compose up --build
    ```
3. Accede a la interfaz de Airflow en [http://localhost:8080](http://localhost:8080) y ejecuta el DAG `TRADING_ECONOMICS`.

## Personalización

- Puedes modificar el archivo `utils_index.py` para adaptar el procesamiento de datos según tus necesidades.
- Los scripts SQL pueden ajustarse para coincidir con la estructura de tus tablas en Snowflake.

## Licencia

Este proyecto está bajo la licencia MIT.

## Autor

Milton Hernández  
145373465+hernandez-milton@users.noreply.github.com
