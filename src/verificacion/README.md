
# Verificación de archivos CSV

Este directorio contiene scripts de verificación de archivos CSV.

Estas pruebas de verificación se ejecutan automáticamente utilizando GitHub actions.

# Ejecutar

Las pruebas se pueden ejecutar localmente. Requieren node 12.x.

Para correr las pruebas localmente:

```
npm install
npm run test
```

# Pruebas disponibles

Se ejecutan las siguientes pruebas para cada archivo:

|Regla |Descripción |Archivos
|-|-|-
|**[Líneas](./src/emptyLines.test.ts)** |Valida que el archivo CSV no contenga líneas vacías|Todos
|**[Formato de fecha ISO](./src/dateFormat.test.ts)** |Valida que el archivo CSV contenga a lo menos una columna con el formato `yyyy-MM-dd`. Este formato utiliza la [nomenclatura de luxon](https://moment.github.io/luxon/docs/manual/parsing.html#table-of-tokens) |Archivos marcados con la etiqueta `ISO`.

# Nuevos archivos

Para asegurar que se están validando las reglas correctas de cada archivo, estas pruebas fallan cuando un nuevo archivo es agregado y no coincide con ninguno de los patrones listados en [este archivo](./src/config/Files.ts).

Si ese es el caso, se deben seguir los siguientes pasos:

- Agregar una nueva entrada en [`Files.ts`](./src/config/Files.ts)
- Asegurarse de que se incluyen las etiquetas necesarias.
