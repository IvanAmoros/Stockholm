# 馃攼 Stockholm

## Descripci贸n

Este proyecto consta en hacer un ransomware con _educational proposes only_, el cual se encarga de encryptar todos los ficheros (con la extensi贸n afectada por el [WannaCry ransomware](https://es.wikipedia.org/wiki/WannaCry)), encontrados dentro del directorio _infection_ en _home_. No encrypta de forma recursiva en caso de encontrar mas directorios dentro.

El programa se ha hecho especificamente para trabajar en una maquina virtual Kali, pero se puede utilizar en otro _OS_ haciendo un par de modificaciones, como por ejemplo el _PATH_.

El manejo de errores ha sido meticulosamente cuidado, con tal de que el programa no de fallos en ning煤n momento. Tratando casos como los permisos de los ficheros a la hora de encryptar, avisos en caso de interar a reencryptar ficheros, poner extensiones a los directorios,...

El programa ha sido desarollado en Python3, ya que se pueden encontrar multitud de librerias para encryptar de una forma muy segura. En este caso he optado por usar [Cryptography.Fernet](https://cryptography.io/en/latest/fernet/) que proporciona cifrado sim茅trico y autenticaci贸n de datos.

## Uso

```python3 stockholm.py``` para ejecutar el encryptador.

```python3 stockholm.py -s``` o ```python3 stockholm.py -silent``` para ejecutar el encryptador sin mostrar en pantalla ning煤n aviso.

```python3 stockholm.py -h``` o ```python3 stockholm.py -help``` para conocer el uso del programa.

```python3 stockholm.py -v``` o ```python3 stockholm.py -version``` para mostrar en pantalla la versi贸n del programa.

```python3 stockholm.py -r [KEY]``` o ```python3 stockholm.py -reverse [KEY]``` para desencryptar los archivos previamente encryptados, utilizando la clave que se encuentra en el fichero '_key.key_' creado al encryptar.

## Demostraci贸n

https://user-images.githubusercontent.com/86268267/186781948-9df41a91-9419-44a0-a562-82908fd54cce.mov


