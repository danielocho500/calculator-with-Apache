# Calculadora Con Apache Thrift

_Nota: La funcionalidad en Docker no ha sido implementada aún_

* Servidor Escrito en NodeJS
* Cliente Escrito en Python

Requisitos:
* [NodeJS](https://nodejs.org/en/)
* [Python](https://www.python.org/)

##Instrucciones para su ejecución

### Servidor 
1. Entrar a la carpeta servidorNode
2. Ejecutar el comando para crear archivos de Thrift
```
Thrift -r --gen js:node ./calc.thrift
```
3. Ejecutar el siguiente comando para descargar las librerias
```
npm install
```
4. Ejecutar el siguiente comando para iniciar el Servidor
```
node app.js
```


### Cliente
1. Entrar a la carpeta de Cliente
2. Ejecutar el comando para crear archivos de Thrift
```
Thrift -r --gen py ./calc.thrift
```
3. Descargar la libreria de Thrift
```
pip3 install Thrift
```
4. Iniciar ejecución del Cliente
```
python ./CalcClient.py
```