# preguntas.py
# Banco de preguntas de ciberseguridad educativa — todo en español.

PREGUNTAS = [

    # ══════════════════════════════════════════
    # CATEGORÍA: Seguridad de Redes
    # ══════════════════════════════════════════
    {
        "categoria": "Seguridad de Redes",
        "dificultad": "fácil",
        "pregunta": "¿Qué hace principalmente un firewall?",
        "opciones": ["Cifra archivos", "Filtra el tráfico de red", "Crea copias de seguridad", "Acelera el Wi-Fi"],
        "respuesta": 1,
        "explicacion": "Un firewall filtra el tráfico entrante y saliente según reglas definidas para proteger la red.",
    },
    {
        "categoria": "Seguridad de Redes",
        "dificultad": "fácil",
        "pregunta": "¿Cuál es el propósito de una VPN?",
        "opciones": ["Hacer contraseñas más cortas", "Crear un túnel cifrado sobre la red", "Eliminar malware", "Recuperar archivos borrados"],
        "respuesta": 1,
        "explicacion": "Una VPN cifra la conexión entre dos puntos, protegiendo los datos en tránsito.",
    },
    {
        "categoria": "Seguridad de Redes",
        "dificultad": "fácil",
        "pregunta": "¿Qué hace el protocolo DNS?",
        "opciones": ["Cifra los correos", "Traduce nombres de dominio a direcciones IP", "Autentica usuarios", "Filtra puertos"],
        "respuesta": 1,
        "explicacion": "El DNS resuelve nombres de dominio legibles por humanos (como google.com) a direcciones IP.",
    },
    {
        "categoria": "Seguridad de Redes",
        "dificultad": "medio",
        "pregunta": "¿Qué protocolo se usa para el tráfico web seguro?",
        "opciones": ["HTTP", "FTP", "HTTPS", "Telnet"],
        "respuesta": 2,
        "explicacion": "HTTPS es HTTP sobre TLS/SSL, lo que proporciona cifrado e integridad en la comunicación web.",
    },
    {
        "categoria": "Seguridad de Redes",
        "dificultad": "medio",
        "pregunta": "¿En qué puerto opera comúnmente HTTPS?",
        "opciones": ["21", "53", "80", "443"],
        "respuesta": 3,
        "explicacion": "HTTPS usa el puerto 443 por defecto, mientras que HTTP usa el puerto 80.",
    },
    {
        "categoria": "Seguridad de Redes",
        "dificultad": "medio",
        "pregunta": "¿Qué es un ataque de denegación de servicio (DoS)?",
        "opciones": ["Robar contraseñas", "Saturar un sistema para que deje de funcionar", "Instalar un keylogger", "Interceptar correos"],
        "respuesta": 1,
        "explicacion": "Un ataque DoS busca saturar un servidor o red con tráfico masivo para dejarlo inaccesible.",
    },
    {
        "categoria": "Seguridad de Redes",
        "dificultad": "difícil",
        "pregunta": "¿Qué diferencia hay entre IDS e IPS?",
        "opciones": [
            "IDS bloquea tráfico, IPS solo registra",
            "IPS bloquea y previene, IDS detecta y alerta",
            "Son exactamente lo mismo",
            "IDS solo funciona en redes inalámbricas",
        ],
        "respuesta": 1,
        "explicacion": "El IPS actúa activamente bloqueando tráfico malicioso, mientras que el IDS solo detecta y genera alertas.",
    },
    {
        "categoria": "Seguridad de Redes",
        "dificultad": "difícil",
        "pregunta": "¿Qué es un ataque de hombre en el medio (MitM)?",
        "opciones": [
            "Un ataque físico a los servidores",
            "Interceptar y posiblemente alterar la comunicación entre dos partes",
            "Adivinar contraseñas por fuerza bruta",
            "Enviar spam masivo",
        ],
        "respuesta": 1,
        "explicacion": "En un ataque MitM el atacante se interpone entre dos partes para leer o modificar el tráfico sin que lo noten.",
    },

    # ══════════════════════════════════════════
    # CATEGORÍA: Seguridad Web
    # ══════════════════════════════════════════
    {
        "categoria": "Seguridad Web",
        "dificultad": "fácil",
        "pregunta": "¿Qué es la inyección SQL?",
        "opciones": ["Un error de pantalla", "Inyectar código SQL malicioso en consultas", "Un tipo de cifrado", "Un método de respaldo"],
        "respuesta": 1,
        "explicacion": "La inyección SQL ocurre cuando una entrada no confiable es interpretada como SQL, permitiendo acceder o modificar la base de datos.",
    },
    {
        "categoria": "Seguridad Web",
        "dificultad": "fácil",
        "pregunta": "¿Qué significa XSS?",
        "opciones": ["Secuencias de Comandos entre Sitios", "Sincronización entre Servidores", "Escaneo XML de Sitios", "Sincronización entre Sistemas"],
        "respuesta": 0,
        "explicacion": "XSS (Cross-Site Scripting) permite inyectar scripts maliciosos en páginas web vistas por otros usuarios.",
    },
    {
        "categoria": "Seguridad Web",
        "dificultad": "fácil",
        "pregunta": "¿Qué cabecera HTTP ayuda a reducir el clickjacking?",
        "opciones": ["X-Frame-Options", "Cache-Control", "Accept-Language", "User-Agent"],
        "respuesta": 0,
        "explicacion": "X-Frame-Options impide que una página sea cargada dentro de un iframe de otro sitio.",
    },
    {
        "categoria": "Seguridad Web",
        "dificultad": "medio",
        "pregunta": "¿Qué es CSRF?",
        "opciones": [
            "Falsificación de Solicitud entre Sitios",
            "Filtro de Recursos de Seguridad",
            "Restablecimiento de Sesión Cifrada",
            "Fallo de Enrutamiento entre Sistemas",
        ],
        "respuesta": 0,
        "explicacion": "CSRF engaña al navegador para que envíe solicitudes autenticadas no deseadas en nombre del usuario.",
    },
    {
        "categoria": "Seguridad Web",
        "dificultad": "medio",
        "pregunta": "¿Cuál es la mejor práctica para almacenar contraseñas?",
        "opciones": ["Texto plano", "Codificación Base64", "Hash con algoritmo fuerte y sal", "Ponerlas en comentarios del código"],
        "respuesta": 2,
        "explicacion": "Las contraseñas deben almacenarse con hash (ej. bcrypt) y una sal única para cada usuario, nunca en texto plano.",
    },
    {
        "categoria": "Seguridad Web",
        "dificultad": "medio",
        "pregunta": "¿Para qué sirve la validación de entradas del usuario?",
        "opciones": [
            "Hacer la página más lenta",
            "Asegurar que los datos sean seguros antes de procesarlos",
            "Ocultar el código fuente",
            "Comprimir el tráfico web",
        ],
        "respuesta": 1,
        "explicacion": "La validación previene que datos maliciosos o inesperados lleguen a la lógica sensible de la aplicación.",
    },
    {
        "categoria": "Seguridad Web",
        "dificultad": "difícil",
        "pregunta": "¿Qué hace la Política de Seguridad de Contenido (CSP)?",
        "opciones": [
            "Acelera la carga de CSS",
            "Restringe qué recursos puede cargar una página",
            "Reemplaza el protocolo TLS",
            "Gestiona las cookies de sesión",
        ],
        "respuesta": 1,
        "explicacion": "CSP reduce el impacto de XSS limitando los orígenes desde donde se pueden cargar scripts y otros recursos.",
    },
    {
        "categoria": "Seguridad Web",
        "dificultad": "difícil",
        "pregunta": "¿Qué son las consultas parametrizadas y para qué sirven?",
        "opciones": [
            "Consultas que se ejecutan más rápido en paralelo",
            "Consultas que separan el código SQL de los datos para evitar inyección",
            "Consultas cifradas con clave pública",
            "Consultas ejecutadas sin conexión",
        ],
        "respuesta": 1,
        "explicacion": "Las consultas parametrizadas evitan la inyección SQL al tratar los datos del usuario siempre como valores, nunca como código SQL.",
    },

    # ══════════════════════════════════════════
    # CATEGORÍA: Criptografía
    # ══════════════════════════════════════════
    {
        "categoria": "Criptografía",
        "dificultad": "fácil",
        "pregunta": "¿Para qué se usa el cifrado?",
        "opciones": ["Ocultar datos de personas no autorizadas", "Eliminar archivos", "Aumentar el brillo de pantalla", "Crear nombres de usuario"],
        "respuesta": 0,
        "explicacion": "El cifrado transforma los datos para que solo partes autorizadas puedan leerlos.",
    },
    {
        "categoria": "Criptografía",
        "dificultad": "fácil",
        "pregunta": "¿Para qué se usa típicamente el hashing?",
        "opciones": [
            "Recuperar texto plano exactamente",
            "Verificar integridad y almacenar contraseñas de forma segura",
            "Comprimir videos",
            "Enviar correos cifrados",
        ],
        "respuesta": 1,
        "explicacion": "El hashing es una función de una sola vía usada para verificar integridad y almacenar contraseñas.",
    },
    {
        "categoria": "Criptografía",
        "dificultad": "fácil",
        "pregunta": "¿Qué protege TLS?",
        "opciones": ["Solo capturas de pantalla", "Los datos en tránsito por la red", "Archivos offline únicamente", "La configuración del teclado"],
        "respuesta": 1,
        "explicacion": "TLS cifra los datos mientras viajan por la red, protegiéndolos de interceptación.",
    },
    {
        "categoria": "Criptografía",
        "dificultad": "medio",
        "pregunta": "¿Cuál es la diferencia entre cifrado simétrico y asimétrico?",
        "opciones": [
            "El simétrico usa una sola clave; el asimétrico usa un par clave pública/privada",
            "Son idénticos en funcionamiento",
            "El asimétrico no puede descifrar",
            "El simétrico solo funciona en línea",
        ],
        "respuesta": 0,
        "explicacion": "El cifrado simétrico usa una clave compartida. El asimétrico usa una clave pública para cifrar y una privada para descifrar.",
    },
    {
        "categoria": "Criptografía",
        "dificultad": "medio",
        "pregunta": "¿Por qué se añaden sales (salts) a los hashes de contraseñas?",
        "opciones": [
            "Para hacer las contraseñas más difíciles de recordar",
            "Para que cada hash sea único y resistir ataques de tablas arcoíris",
            "Para hacer el hash reversible",
            "Para evitar el uso de claves",
        ],
        "respuesta": 1,
        "explicacion": "Las sales aleatorias hacen que dos contraseñas iguales produzcan hashes distintos, frustrando ataques precomputados.",
    },
    {
        "categoria": "Criptografía",
        "dificultad": "medio",
        "pregunta": "¿Para qué sirve una firma digital?",
        "opciones": [
            "Renombrar archivos automáticamente",
            "Probar la autenticidad e integridad de un mensaje",
            "Ocultar pestañas del navegador",
            "Detectar malware",
        ],
        "respuesta": 1,
        "explicacion": "Las firmas digitales usan criptografía asimétrica para verificar quién firmó un documento y que no fue alterado.",
    },
    {
        "categoria": "Criptografía",
        "dificultad": "difícil",
        "pregunta": "¿Qué propiedad fundamental debe tener un hash criptográfico?",
        "opciones": ["Ser reversible", "Resistencia a colisiones", "Alta resolución de salida", "Bajo consumo de memoria únicamente"],
        "respuesta": 1,
        "explicacion": "La resistencia a colisiones garantiza que sea computacionalmente inviable encontrar dos entradas que produzcan el mismo hash.",
    },
    {
        "categoria": "Criptografía",
        "dificultad": "difícil",
        "pregunta": "¿Qué es el secreto perfecto hacia adelante (Forward Secrecy)?",
        "opciones": [
            "El tráfico pasado queda seguro incluso si la clave de larga duración se compromete después",
            "El tráfico siempre es anónimo",
            "Las claves criptográficas nunca expiran",
            "Las contraseñas se cifran automáticamente",
        ],
        "respuesta": 0,
        "explicacion": "Forward Secrecy protege sesiones pasadas generando claves efímeras por sesión, independientes de la clave a largo plazo.",
    },

    # ══════════════════════════════════════════
    # CATEGORÍA: Ingeniería Social
    # ══════════════════════════════════════════
    {
        "categoria": "Ingeniería Social",
        "dificultad": "fácil",
        "pregunta": "¿Qué es el phishing?",
        "opciones": [
            "Un método de respaldo de archivos",
            "Engañar a personas para revelar información o hacer clic en enlaces maliciosos",
            "Un protocolo inalámbrico",
            "Un tipo de firewall",
        ],
        "respuesta": 1,
        "explicacion": "El phishing usa el engaño (correos, mensajes falsos) para robar credenciales o instalar malware.",
    },
    {
        "categoria": "Ingeniería Social",
        "dificultad": "fácil",
        "pregunta": "Un mensaje urgente que pide acción inmediata es señal de ¿qué?",
        "opciones": ["Buen servicio al cliente", "Posible ingeniería social", "Compresión de datos", "Recuperación de datos"],
        "respuesta": 1,
        "explicacion": "La urgencia artificial es una de las tácticas de presión más comunes en ataques de ingeniería social.",
    },
    {
        "categoria": "Ingeniería Social",
        "dificultad": "fácil",
        "pregunta": "¿Cuál es la respuesta más segura ante un enlace sospechoso?",
        "opciones": ["Hacer clic rápidamente", "Verificar el dominio y la fuente antes de abrir", "Reenviarlo a todos los contactos", "Responder con tus datos"],
        "respuesta": 1,
        "explicacion": "Verificar la URL y el remitente ayuda a evitar caer en phishing y sitios maliciosos.",
    },
    {
        "categoria": "Ingeniería Social",
        "dificultad": "medio",
        "pregunta": "¿Qué es el pretexting?",
        "opciones": [
            "Escribir código por adelantado",
            "Crear un escenario falso para ganarse la confianza de la víctima",
            "Probar la velocidad de una aplicación",
            "Una política de respaldo de datos",
        ],
        "respuesta": 1,
        "explicacion": "En el pretexting el atacante inventa un rol o historia creíble para manipular a la víctima.",
    },
    {
        "categoria": "Ingeniería Social",
        "dificultad": "medio",
        "pregunta": "¿Qué debes hacer si alguien dice ser de soporte técnico y te pide la contraseña?",
        "opciones": [
            "Dársela si suena oficial",
            "Verificar por canales oficiales y nunca compartir tu contraseña",
            "Enviarla por correo electrónico",
            "Publicarla en el chat del equipo",
        ],
        "respuesta": 1,
        "explicacion": "El soporte legítimo nunca necesita tu contraseña. Siempre verifica la identidad por un canal independiente.",
    },
    {
        "categoria": "Ingeniería Social",
        "dificultad": "medio",
        "pregunta": "¿Qué es el tailgating en seguridad física?",
        "opciones": [
            "Seguir a alguien a una zona restringida sin autorización",
            "Cambiar un nombre de usuario",
            "Usar una VPN corporativa",
            "Cifrar un disco duro",
        ],
        "respuesta": 0,
        "explicacion": "El tailgating es la técnica de colarse físicamente en una zona restringida aprovechando la apertura de puerta de otra persona.",
    },
    {
        "categoria": "Ingeniería Social",
        "dificultad": "difícil",
        "pregunta": "¿Por qué suelen ser efectivos los ataques de ingeniería social?",
        "opciones": [
            "Explotan la confianza, la urgencia y los sesgos humanos",
            "Requieren supercomputadoras",
            "Solo afectan a sistemas Linux",
            "Son siempre fáciles de detectar",
        ],
        "respuesta": 0,
        "explicacion": "Estos ataques tienen éxito porque manipulan emociones y comportamientos humanos en lugar de eludir controles técnicos.",
    },
    {
        "categoria": "Ingeniería Social",
        "dificultad": "difícil",
        "pregunta": "¿Qué es el spear phishing?",
        "opciones": [
            "Phishing genérico enviado masivamente",
            "Phishing muy dirigido y personalizado hacia una persona u organización específica",
            "Un ataque a redes Wi-Fi",
            "Un tipo de ransomware",
        ],
        "respuesta": 1,
        "explicacion": "El spear phishing es altamente personalizado usando información real de la víctima, lo que lo hace más difícil de detectar.",
    },

    # ══════════════════════════════════════════
    # CATEGORÍA: Malware y Virus
    # ══════════════════════════════════════════
    {
        "categoria": "Malware y Virus",
        "dificultad": "fácil",
        "pregunta": "¿Qué es el malware?",
        "opciones": ["Software malicioso diseñado para dañar sistemas", "Una pestaña nueva del navegador", "Texto cifrado", "Hardware de red"],
        "respuesta": 0,
        "explicacion": "El malware es cualquier software diseñado para dañar, espiar o interrumpir sistemas sin el consentimiento del usuario.",
    },
    {
        "categoria": "Malware y Virus",
        "dificultad": "fácil",
        "pregunta": "¿Qué necesita un virus informático para propagarse?",
        "opciones": ["Un archivo o programa anfitrión", "Una impresora conectada", "Un teclado mecánico", "Una conexión VPN activa"],
        "respuesta": 0,
        "explicacion": "Un virus se adjunta a un archivo o programa legítimo y se activa cuando ese archivo se ejecuta.",
    },
    {
        "categoria": "Malware y Virus",
        "dificultad": "fácil",
        "pregunta": "¿Qué es el ransomware?",
        "opciones": [
            "Software que mejora el rendimiento",
            "Malware que cifra tus datos y exige un rescate para liberarlos",
            "Un gestor de contraseñas",
            "Una herramienta de respaldo",
        ],
        "respuesta": 1,
        "explicacion": "El ransomware cifra los archivos de la víctima y exige un pago (generalmente criptomonedas) a cambio de la clave de descifrado.",
    },
    {
        "categoria": "Malware y Virus",
        "dificultad": "medio",
        "pregunta": "¿Qué es un troyano?",
        "opciones": [
            "Una actualización legítima del sistema",
            "Malware disfrazado de software inofensivo o útil",
            "Una tarjeta de red inalámbrica",
            "Un archivo de respaldo",
        ],
        "respuesta": 1,
        "explicacion": "El troyano se presenta como software legítimo para engañar al usuario y ejecutarse en el sistema.",
    },
    {
        "categoria": "Malware y Virus",
        "dificultad": "medio",
        "pregunta": "¿Cuál es una señal común de infección por malware?",
        "opciones": [
            "Ventanas emergentes inesperadas y lentitud del sistema",
            "Una libreta nueva sobre el escritorio",
            "Menor brillo de la pantalla",
            "Iconos de escritorio perfectamente ordenados",
        ],
        "respuesta": 0,
        "explicacion": "Comportamientos inesperados como popups, lentitud o procesos desconocidos pueden indicar una infección.",
    },
    {
        "categoria": "Malware y Virus",
        "dificultad": "medio",
        "pregunta": "¿Qué hace un sandbox en el análisis de malware?",
        "opciones": [
            "Prepara informes de rendimiento",
            "Ejecuta código sospechoso en un entorno aislado y seguro",
            "Elimina todos los archivos del sistema",
            "Acelera las descargas de internet",
        ],
        "respuesta": 1,
        "explicacion": "Un sandbox permite observar el comportamiento del malware sin arriesgar el sistema real.",
    },
    {
        "categoria": "Malware y Virus",
        "dificultad": "difícil",
        "pregunta": "¿Por qué algunos malware usan ofuscación en su código?",
        "opciones": [
            "Para dificultar la detección por antivirus y el análisis forense",
            "Para mejorar la duración de la batería del dispositivo",
            "Para abrir puertos de red de forma segura",
            "Únicamente para reducir el tamaño del archivo",
        ],
        "respuesta": 0,
        "explicacion": "La ofuscación oculta la verdadera funcionalidad del malware dificultando el análisis estático y eludiendo firmas de antivirus.",
    },
    {
        "categoria": "Malware y Virus",
        "dificultad": "difícil",
        "pregunta": "¿Cuál es el mejor primer paso al sospechar una infección por malware?",
        "opciones": [
            "Desconectar el equipo de la red y reportar el incidente",
            "Compartir el archivo sospechoso en internet para analizarlo",
            "Borrar la carpeta system32",
            "Compartirlo con compañeros de trabajo",
        ],
        "respuesta": 0,
        "explicacion": "Aislar el equipo evita que el malware se propague y reportarlo permite iniciar la respuesta al incidente.",
    },

    # ══════════════════════════════════════════
    # CATEGORÍA: Herramientas y Técnicas
    # ══════════════════════════════════════════
    {
        "categoria": "Herramientas y Técnicas",
        "dificultad": "fácil",
        "pregunta": "¿Para qué sirve la autenticación multifactor (MFA)?",
        "opciones": [
            "Añadir una capa extra de verificación de identidad",
            "Reemplazar completamente las contraseñas",
            "Desactivar las alertas de inicio de sesión",
            "Acelerar el proceso de autenticación",
        ],
        "respuesta": 0,
        "explicacion": "La MFA requiere más de un factor (algo que sabes, tienes o eres) para verificar la identidad.",
    },
    {
        "categoria": "Herramientas y Técnicas",
        "dificultad": "fácil",
        "pregunta": "¿Para qué sirve un gestor de contraseñas?",
        "opciones": [
            "Generar y almacenar contraseñas únicas y seguras",
            "Crear malware automatizado",
            "Cambiar tu dirección IP",
            "Filtrar correos no deseados",
        ],
        "respuesta": 0,
        "explicacion": "Un gestor de contraseñas crea contraseñas fuertes y únicas para cada servicio y las guarda de forma cifrada.",
    },
    {
        "categoria": "Herramientas y Técnicas",
        "dificultad": "fácil",
        "pregunta": "¿Para qué sirven las actualizaciones y parches de seguridad?",
        "opciones": [
            "Añadir nuevas vulnerabilidades al sistema",
            "Corregir errores y fallos de seguridad conocidos",
            "Eliminar copias de seguridad antiguas",
            "Reducir el nivel de cifrado del sistema",
        ],
        "respuesta": 1,
        "explicacion": "Los parches corrigen vulnerabilidades conocidas, reduciendo la superficie de ataque.",
    },
    {
        "categoria": "Herramientas y Técnicas",
        "dificultad": "medio",
        "pregunta": "¿Por qué es importante el registro de eventos (logging) en seguridad?",
        "opciones": [
            "Permite reconstruir eventos y detectar anomalías",
            "Sirve para ocultar actividad maliciosa",
            "Reduce el cifrado de datos",
            "Formatea discos automáticamente",
        ],
        "respuesta": 0,
        "explicacion": "Los registros son esenciales para monitorización continua, detección de intrusiones y respuesta a incidentes.",
    },
    {
        "categoria": "Herramientas y Técnicas",
        "dificultad": "medio",
        "pregunta": "¿Qué es el principio de mínimo privilegio?",
        "opciones": [
            "Dar acceso de administrador a todos por defecto",
            "Otorgar solo los permisos estrictamente necesarios para cada tarea",
            "Eliminar toda autenticación del sistema",
            "Bloquear el acceso a todos los usuarios",
        ],
        "respuesta": 1,
        "explicacion": "Limitar los permisos al mínimo necesario reduce el impacto de un error o de una cuenta comprometida.",
    },
    {
        "categoria": "Herramientas y Técnicas",
        "dificultad": "medio",
        "pregunta": "¿Qué busca robar el phishing de tokens MFA?",
        "opciones": [
            "Capturas de pantalla del sistema",
            "Códigos de un solo uso o tokens de sesión activos",
            "El cartucho de tinta de la impresora",
            "La configuración del teclado",
        ],
        "respuesta": 1,
        "explicacion": "Los atacantes capturan en tiempo real el código OTP o el token de sesión para eludir la MFA.",
    },
    {
        "categoria": "Herramientas y Técnicas",
        "dificultad": "difícil",
        "pregunta": "¿Qué es una línea base de seguridad (security baseline)?",
        "opciones": [
            "Un estándar de configuración segura mínima para los sistemas",
            "Un sistema que hace todos los equipos idénticos para siempre",
            "Un proceso para eliminar actualizaciones pendientes",
            "Una política para deshabilitar todos los permisos de usuario",
        ],
        "respuesta": 0,
        "explicacion": "Una línea base define la configuración de seguridad mínima aceptable que deben cumplir los sistemas de una organización.",
    },
    {
        "categoria": "Herramientas y Técnicas",
        "dificultad": "difícil",
        "pregunta": "¿Por qué son esenciales las copias de seguridad en ciberseguridad?",
        "opciones": [
            "Hacen que el malware se ejecute más rápido",
            "Permiten recuperarse ante pérdida de datos, fallos o ataques de ransomware",
            "Reemplazan la necesidad de autenticación",
            "Solo sirven para guardar capturas de pantalla",
        ],
        "respuesta": 1,
        "explicacion": "Sin copias de seguridad actualizadas y probadas, un ataque de ransomware o un fallo puede significar pérdida total de datos.",
    },

    # ══════════════════════════════════════════
    # CATEGORÍA: Conceptos y Fundamentos
    # ══════════════════════════════════════════
    {
        "categoria": "Conceptos y Fundamentos",
        "dificultad": "fácil",
        "pregunta": "¿Qué significa la tríada CIA en seguridad?",
        "opciones": [
            "Confidencialidad, Integridad, Disponibilidad",
            "Código, Identificación, Acceso",
            "Criptografía, Identidad, Autenticación",
            "Control, Internet, Alerta",
        ],
        "respuesta": 0,
        "explicacion": "La tríada CIA es el fundamento de la seguridad de la información: Confidencialidad, Integridad y Disponibilidad.",
    },
    {
        "categoria": "Conceptos y Fundamentos",
        "dificultad": "fácil",
        "pregunta": "¿Qué es la autenticación?",
        "opciones": [
            "El proceso de verificar quién eres",
            "Ajustar el brillo de la pantalla",
            "Cifrar un archivo del sistema",
            "Cambiar los permisos de un archivo",
        ],
        "respuesta": 0,
        "explicacion": "La autenticación verifica la identidad de un usuario o sistema antes de conceder acceso.",
    },
    {
        "categoria": "Conceptos y Fundamentos",
        "dificultad": "fácil",
        "pregunta": "¿Qué es la autorización en seguridad?",
        "opciones": [
            "Determinar a qué recursos puede acceder un usuario autenticado",
            "Cambiar la distribución del teclado",
            "Detectar malware en el sistema",
            "Hacer copias de seguridad de correos",
        ],
        "respuesta": 0,
        "explicacion": "Tras autenticarse, la autorización decide qué permisos y recursos tiene disponibles el usuario.",
    },
    {
        "categoria": "Conceptos y Fundamentos",
        "dificultad": "medio",
        "pregunta": "¿Qué es una vulnerabilidad en ciberseguridad?",
        "opciones": [
            "Una debilidad que puede ser explotada por un atacante",
            "Un tipo especial de cable de red",
            "Una política de copias de seguridad",
            "Un formulario de inicio de sesión",
        ],
        "respuesta": 0,
        "explicacion": "Una vulnerabilidad es un fallo o debilidad en un sistema que un atacante podría aprovechar para causar daño.",
    },
    {
        "categoria": "Conceptos y Fundamentos",
        "dificultad": "medio",
        "pregunta": "¿Qué es una amenaza en ciberseguridad?",
        "opciones": [
            "Cualquier evento o actor que podría explotar una vulnerabilidad",
            "Un gestor de contraseñas avanzado",
            "Un parche de software reciente",
            "El formateo de un disco duro",
        ],
        "respuesta": 0,
        "explicacion": "Una amenaza es un agente o circunstancia que tiene el potencial de causar daño explotando una vulnerabilidad.",
    },
    {
        "categoria": "Conceptos y Fundamentos",
        "dificultad": "medio",
        "pregunta": "¿Cómo se define el riesgo en ciberseguridad?",
        "opciones": [
            "La probabilidad de que ocurra un incidente multiplicada por su impacto",
            "Un tipo específico de firewall",
            "El número total de usuarios del sistema",
            "La velocidad de conexión a internet",
        ],
        "respuesta": 0,
        "explicacion": "El riesgo = probabilidad × impacto. Gestionar el riesgo implica reducir uno o ambos factores.",
    },
    {
        "categoria": "Conceptos y Fundamentos",
        "dificultad": "difícil",
        "pregunta": "¿Qué es la defensa en profundidad?",
        "opciones": [
            "Usar múltiples capas de controles de seguridad redundantes",
            "Depender de una única contraseña muy segura",
            "Desactivar todos los registros del sistema",
            "Compartir acceso de administrador entre equipos",
        ],
        "respuesta": 0,
        "explicacion": "La defensa en profundidad usa capas superpuestas de controles para que si una falla, las demás sigan protegiendo el sistema.",
    },
    {
        "categoria": "Conceptos y Fundamentos",
        "dificultad": "difícil",
        "pregunta": "¿Por qué es importante una configuración segura por defecto?",
        "opciones": [
            "Reduce el riesgo de errores de configuración y exposición desde el primer momento",
            "Deshabilita todo acceso al sistema para mayor seguridad",
            "Hace el software notablemente más lento",
            "Reemplaza la necesidad de formación en seguridad",
        ],
        "respuesta": 0,
        "explicacion": "Los valores por defecto seguros reducen la superficie de ataque desde el despliegue inicial, sin esperar configuración manual.",
    },

    # ══════════════════════════════════════════
    # CATEGORÍA: CTF y Hacking Ético
    # ══════════════════════════════════════════
    {
        "categoria": "CTF y Hacking Ético",
        "dificultad": "fácil",
        "pregunta": "¿Qué significa CTF en ciberseguridad?",
        "opciones": [
            "Capturar la Bandera (Capture The Flag)",
            "Controlar el Firewall Total",
            "Formato de Prueba Cibernética",
            "Centro de Transferencia de Ficheros",
        ],
        "respuesta": 0,
        "explicacion": "CTF (Capture The Flag) es un formato de competición de ciberseguridad donde los participantes resuelven retos para capturar «banderas».",
    },
    {
        "categoria": "CTF y Hacking Ético",
        "dificultad": "fácil",
        "pregunta": "En un CTF, ¿qué es normalmente una 'flag' (bandera)?",
        "opciones": [
            "Un valor o cadena de texto secreto que prueba que resolviste el reto",
            "Un cable de red especial",
            "Un gestor de contraseñas",
            "Un archivo de registro del sistema",
        ],
        "respuesta": 0,
        "explicacion": "Una flag suele tener el formato flag{texto_secreto} y es el token que valida que completaste el reto.",
    },
    {
        "categoria": "CTF y Hacking Ético",
        "dificultad": "fácil",
        "pregunta": "¿Qué es la enumeración en una evaluación de seguridad?",
        "opciones": [
            "Recopilar información sobre el objetivo o sistema objetivo",
            "Eliminar archivos del servidor",
            "Formatear los discos duros del objetivo",
            "Cambiar el fondo de pantalla del sistema",
        ],
        "respuesta": 0,
        "explicacion": "La enumeración es la fase de reconocimiento donde se recopila información sobre puertos, servicios, usuarios y versiones.",
    },
    {
        "categoria": "CTF y Hacking Ético",
        "dificultad": "medio",
        "pregunta": "¿Por qué son útiles los entornos de laboratorio CTF?",
        "opciones": [
            "Ofrecen entornos seguros y legales para practicar técnicas de seguridad",
            "Deshabilitan la seguridad en redes reales",
            "Reemplazan por completo los sistemas de producción",
            "Son únicamente para jugadores de videojuegos",
        ],
        "respuesta": 0,
        "explicacion": "Los CTF permiten aprender y practicar técnicas de hacking de forma ética, segura y completamente legal.",
    },
    {
        "categoria": "CTF y Hacking Ético",
        "dificultad": "medio",
        "pregunta": "¿Para qué se practica el cracking de hashes en los CTF?",
        "opciones": [
            "Aprender sobre contraseñas débiles en un entorno controlado y legal",
            "Ocultar evidencia de un ataque real",
            "Crear malware para distribuir",
            "Eludir actualizaciones de seguridad reales",
        ],
        "respuesta": 0,
        "explicacion": "En CTFs, los ejercicios de hashes enseñan la importancia de usar contraseñas y algoritmos fuertes, sin afectar sistemas reales.",
    },
    {
        "categoria": "CTF y Hacking Ético",
        "dificultad": "medio",
        "pregunta": "¿Qué es un write-up en el contexto de CTF?",
        "opciones": [
            "Un documento que explica cómo se resolvió un reto paso a paso",
            "Un contrato legal para hackear sistemas",
            "Un archivo de configuración del servidor",
            "Un tipo de exploit automatizado",
        ],
        "respuesta": 0,
        "explicacion": "Los write-ups documentan el proceso de resolución de un reto CTF, compartiendo el aprendizaje con la comunidad.",
    },
    {
        "categoria": "CTF y Hacking Ético",
        "dificultad": "difícil",
        "pregunta": "¿Qué es la divulgación responsable de vulnerabilidades?",
        "opciones": [
            "Reportar la vulnerabilidad al fabricante de forma privada antes de hacerla pública",
            "Publicar contraseñas de usuarios en internet",
            "Ignorar los errores de seguridad encontrados",
            "Vender el exploit al mejor postor",
        ],
        "respuesta": 0,
        "explicacion": "La divulgación responsable da tiempo al fabricante para corregir el fallo antes de que sea público, protegiendo a los usuarios.",
    },
    {
        "categoria": "CTF y Hacking Ético",
        "dificultad": "difícil",
        "pregunta": "¿Qué es un test de penetración (pentest)?",
        "opciones": [
            "Un ataque autorizado y planificado para evaluar la seguridad de un sistema",
            "Un ataque no autorizado a infraestructuras críticas",
            "Un análisis de velocidad de la red",
            "Una actualización automática del sistema operativo",
        ],
        "respuesta": 0,
        "explicacion": "Un pentest es una simulación de ataque controlada y con autorización escrita, cuyo fin es encontrar vulnerabilidades antes que los atacantes reales.",
    },
]

CATEGORIAS = sorted({p["categoria"] for p in PREGUNTAS})

DIFICULTAD_COLOR = {"fácil": "🟢", "medio": "🟡", "difícil": "🔴"}

def normalizar_categoria(nombre: str) -> str:
    valor = nombre.strip().lower()
    alias = {
        # inglés (compatibilidad)
        "network": "Seguridad de Redes",
        "network security": "Seguridad de Redes",
        "web": "Seguridad Web",
        "web security": "Seguridad Web",
        "crypto": "Criptografía",
        "cryptography": "Criptografía",
        "social": "Ingeniería Social",
        "social engineering": "Ingeniería Social",
        "malware": "Malware y Virus",
        "malware & viruses": "Malware y Virus",
        "tools": "Herramientas y Técnicas",
        "tools & techniques": "Herramientas y Técnicas",
        "fundamentals": "Conceptos y Fundamentos",
        "concepts": "Conceptos y Fundamentos",
        "ctf": "CTF y Hacking Ético",
        "hacking": "CTF y Hacking Ético",
        # español
        "redes": "Seguridad de Redes",
        "seguridad de redes": "Seguridad de Redes",
        "seguridad web": "Seguridad Web",
        "criptografia": "Criptografía",
        "criptografía": "Criptografía",
        "ingenieria social": "Ingeniería Social",
        "ingeniería social": "Ingeniería Social",
        "virus": "Malware y Virus",
        "malware y virus": "Malware y Virus",
        "herramientas": "Herramientas y Técnicas",
        "herramientas y técnicas": "Herramientas y Técnicas",
        "herramientas y tecnicas": "Herramientas y Técnicas",
        "conceptos": "Conceptos y Fundamentos",
        "fundamentos": "Conceptos y Fundamentos",
        "conceptos y fundamentos": "Conceptos y Fundamentos",
        "ctf y hacking ético": "CTF y Hacking Ético",
        "ctf y hacking etico": "CTF y Hacking Ético",
        "hacking ético": "CTF y Hacking Ético",
        "hacking etico": "CTF y Hacking Ético",
    }
    if valor in alias:
        return alias[valor]
    for cat in CATEGORIAS:
        if valor == cat.lower():
            return cat
    return ""

def normalizar_dificultad(valor: str) -> str:
    v = valor.strip().lower()
    mapa = {
        "facil": "fácil", "fácil": "fácil", "easy": "fácil",
        "medio": "medio", "medium": "medio",
        "dificil": "difícil", "difícil": "difícil", "hard": "difícil",
    }
    return mapa.get(v, "")
