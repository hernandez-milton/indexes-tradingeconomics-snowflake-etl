COPY INTO {{ params.table }}
FROM @{{ params.stage }}/indexes_tradingeconomics.csv.gz
FILE_FORMAT = (
  TYPE = 'CSV',
  FIELD_DELIMITER = ',',
  FIELD_OPTIONALLY_ENCLOSED_BY = '"',
  SKIP_HEADER = 1
)
ON_ERROR = 'CONTINUE';