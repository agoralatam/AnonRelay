# AnonRelay 🛠️  
**Roteo de dirección IP**

## Descripción  
**AnonRelay** es una script que obtiene una IP pública a través de los nodos finales de la red Tor de manera rotativa (timepo ajustable por el usuario). Utilizando configuraciones para evitar la fuga de solicitudes DNS. Tambien obteniendo la IP asignada por un nodo de salida y detalles del nodo, como su ubicación y huella digital.

Garantizado para pruebas de anonimato y privacidad en línea.

---
# Imagen
![Captura de pantalla](https://raw.githubusercontent.com/agoralatam/AnonRelay/refs/heads/main/image/Screenshot%202024-12-10%2012%5E%2549%5E%2558.png)
---
## Características Principales  
- Rotación de IP
- Informaíon a cerca del nodo
- Protección contra fugas DNS
---

## Requisitos del Sistema  
- **Sistema Operativo**: Linux  
- **Permisos:** Root
---

## Instalación y uso
1. **Clonar el repositorio**:
  ```bash
    git clone https://github.com/tu_usuario/AnonRelay.git
  ```
3. **Entrar a el directorio**:
  ```bash 
   cd AnonRelay
  ```
4.  **Otorgar permisos**:
  ```bash 
   chmod 777 *
  ```
5. **Instalación de dependencias y configuración:**
  ```bash 
   bash configure_services.sh
  ```
6. **Ejecución**
  ```bash 
   bash python3 AnonRelay.py [TIEMPO DE ROTACIÓN EN SEGUNDOS]
  ```
