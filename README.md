# Stockholm

## Bienvenido a mi primer proyecto en Python y segundo en el Cybersecuryty Bootcamp de 42 Barcelona.

Este proyecto consta en hacer un ransomware con educational proposes only, el cual se encarga de encryptar todos los ficheros (con la extensión afectada por el WannaCry ransomware), encontrados dentro del directorio '_infection_' en '_HOME_'. No encrypta de forma recursiva en caso de encontrar mas directorios dentro.

El programa se ha hecho especificamente para trabajar en una maquina virtual Kali, pero se podría utilizar en otro OS haciendo un par de modificaciones, como por ejemplo el PATH.

El manejo de errores ha sido muy meticulosamente cuidado, con tal de no poder petar el programa en ningún caso. Tratando errores como los permisos de los ficheros a la hora de encryptar, avisos en caso de interar a reencryptar ficheros,
