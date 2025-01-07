Tu tarea es generar una evaluación para el Profesor Adiestrado {Nombre}, de la Facultad de Matemática y Computación, de la Universidad de La Habana.

Tu rol es el Jefe de Departamento, habla como si fueras el Jefe que está evaluando al profesor.

El período evaluado es {Year}.

# Contexto

Para tu evaluación, ten en cuenta los siguientes elementos:

## Asignaturas impartidas:
{Docencia}

## Superación:
{Superacion}

## Investigacion:
{Investigacion}

## Tesis dirigidas:
{Diplomas}

## Otras actividades:
{Actividades}

# Instrucciones

Teniendo en cuenta la información anterior, genera una evaluación cualitativa bien desarrollada donde expliques:

- Las asignaturas impartidas por el profesor,
- La superación realizada, si hubo, en caso contrario, decir que no realizó tareas de superación.
- La investigación realizada, si hubo, en caso contrario decir que no realizó tareas de investigación.
- Las tesis que haya dirigido, si hubo, en caso contrario decir que no dirigió tesis de diploma en el período.
- Las demás actividades realizadas, con una breve explicación de su impacto e importancia.

Divide la respuesta en varios párrafos según los elementos.

Además, debes producir una recomendación final corta y específica para mejorar para el año siguiente, teniendo en cuenta sobre todo si debe mejorar la superación y/o investigación. En caso contrario, simplemente decir que se deben mantener las actividades realizadas.

# Formato

Formatea tu respuesta con un único archivo JSON con el siguiente formato:

{{
    "Evaluacion": "...",
    "Recomendacion": "..."
}}

No agregues ningún comentario antes o después de la respuesta en JSON.
