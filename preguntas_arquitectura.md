# Respuestas Parte 3 – Preguntas Técnicas de Arquitectura

### ✅ Pregunta 1: Arquitectura Modular

**¿Cómo modularizarías el sistema para que las cotizaciones, tickets, expedientes y otros módulos puedan mantenerse independientes pero conectados?**

Separaría cada parte del sistema en carpetas o módulos diferentes, por ejemplo uno para cotizaciones y otro para expedientes. Así se hace más ordenado y si hay que modificar algo, no se afecta todo. Todos los módulos usarían la misma base de datos para estar conectados.

### ✅ Pregunta 2: Escalabilidad

**¿Qué ajustes aplicarías a la base de datos si el sistema empieza con 10 usuarios pero escala a 100?**

Cambiaría de SQLite a una base de datos más fuerte como PostgreSQL. También pondría índices en campos importantes para que las búsquedas no se pongan lentas, y organizaría mejor las tablas para evitar datos repetidos.

### ✅ Pregunta 3: Integraciones

**¿Cómo automatizarías el guardado de documentos legales en Google Drive o Dropbox?**

Usaría la API de Google Drive o Dropbox para subir los archivos desde el sistema. El usuario subiría un archivo y el sistema lo enviaría directo a su cuenta en la nube. Luego se puede guardar el enlace del archivo en la base de datos.


### ✅ Pregunta 4: Deployment

**¿Cómo desplegarías esta aplicación para que sea accesible desde computadoras y celulares del estudio, con bajo costo de mantenimiento?**

Usaría un hosting gratuito o económico como Railway o Render. Subiría el proyecto desde GitHub y lo dejaría disponible con un enlace web. Así todos en el estudio pueden acceder desde cualquier dispositivo con internet.


### ✅ Pregunta 5: Seguridad

**¿Qué harías para mantener la seguridad básica de los datos (sin entrar en detalles avanzados)?**

Protegería la clave de la API usando un archivo `.env`, validaría los datos que entran en el sistema y usaría HTTPS si es posible. También pondría un login básico si la app va a ser usada por usuarios reales.
