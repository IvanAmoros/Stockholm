# 🔐 Stockholm

## Descripción

Este proyecto consta en hacer un ransomware con _educational proposes only_, el cual se encarga de encryptar todos los ficheros (con la extensión afectada por el [WannaCry ransomware](https://es.wikipedia.org/wiki/WannaCry)), encontrados dentro del directorio '_infection_' en '_HOME_'. No encrypta de forma recursiva en caso de encontrar mas directorios dentro.

El programa se ha hecho especificamente para trabajar en una maquina virtual Kali, pero se podría utilizar en otro _OS_ haciendo un par de modificaciones, como por ejemplo el _PATH_.

El manejo de errores ha sido muy meticulosamente cuidado, con tal de no poder petar el programa en ningún caso. Tratando errores como los permisos de los ficheros a la hora de encryptar, avisos en caso de interar a reencryptar ficheros, poner extensiones a los directorios,...

El programa ha sido desarollado en Python3, ya que se pueden encontrar multitud de librerias para encryptar de una forma muy segura. En este caso he optado por usar [Cryptography.Fernet](https://cryptography.io/en/latest/fernet/) que proporciona cifrado simétrico y autenticación de datos.

## Uso



https://user-images.githubusercontent.com/86268267/185763451-3231e631-f99a-4d05-8973-a1f6224b1914.mov

