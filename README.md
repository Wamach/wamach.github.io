# wamach.github.io
- - - - Formulario de medicamentos

Parametros de entrada:
- Dia en formato (DD-MM-YYYY)
- Nombre del medicamento
- Frecuencia de horas
- Dias de consumo

Salida - Genera un PDF con:
-  Dia (Formato DD-MM-YYYY) ,
-  Dia de la semana (Lunes / Martes, Miercoles, Etc.)
-  Hora de consumo, y
-  Nombre de medicamento.

Mejoras detectadas Version 1.
- 1. La hora se selecciona del sistema, si se agrega un medicamento a las 06:01 y otro a las 06:02, el resultado de la tabla se ve mal por que lo toma por separado.
     Se agrega punto 1 para version 2.

Planes Version 2.
- 1. Si se inicia en un rango de horas "Ejemplo 06:00 pm". No se incrementen los minutos hasta recargar la pagina.
  2. Validaciones en rango de fecha, frecuencia consumo, dias de consumo y nombre.


Version 2. 30/07/2024
Se identificaron los siguientes escenarios:
1. No se esta poniendo la fecha y hora inicial.
     - Al momento de seleccionar que se comenzara con el medicamento a las 8am el dia 2 de agosto por ejemplo, no se agrega este dia, sino la frecuencia siguiente, es decir 4pm, en el caso de ser 8h.
2. Se agregan opciones en input de frecuencias de horas y dias.
     Frecuencia horas: 6, 8, 12 y 24
     Frecuencia dias: 2 a 15.
3. Update FIX 01/08/2024. Se soluciona el problema de inicio de medicamentos.