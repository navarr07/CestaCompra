# Cesta de la Compra

## Descripción
El módulo **Cesta de la Compra** permite gestionar cestas de compra, clientes, productos y tickets de manera eficiente. Está diseñado para Odoo y ofrece una solución completa para controlar inventarios, transacciones y saldos de clientes.

### Características principales
- Gestión de clientes con saldos de monedero y asociación con países.
- Categorías de productos y manejo de inventarios.
- Creación de tickets con cálculo automático de subtotales y totales.
- Validación de stock de productos y saldo del cliente.
- Estructura modular que incluye vistas y menús específicos para cada funcionalidad.

## Instalación del módulo

### Requisitos previos
1. Tener Odoo 14.0 o superior instalado y en funcionamiento.
2. Acceso administrativo (superusuario) fpara instalar módulos personalizados.
3. Python 3.6 o superior instalado en el sistema.

### Pasos de instalación
1. **Descarga el módulo**:
   - Descarga la carpeta del módulo desde el repositorio o archivo comprimido.
   - Asegúrate de que la estructura incluye directorios como `models/`, `views/`, `static/`, y archivos esenciales como `__manifest__.py`.

2. **Copia el módulo a la carpeta de addons de Odoo**:
   - Localiza la carpeta de addons de tu instalación de Odoo (por defecto suele estar en `/odoo/odoo-server/addons/` o en la ruta configurada en tu archivo `odoo.conf`).
   - Copia la carpeta completa del módulo `cesta` a esta ubicación.

3. **Actualizar la lista de aplicaciones**:
   - Accede a tu instancia de Odoo.
   - Habilita el modo desarrollador.
   - Ve a **Aplicaciones** y selecciona "Actualizar lista de módulos".

4. **Instala el módulo**:
   - Busca el módulo "Cesta de la Compra" en la lista de aplicaciones disponibles.
   - Haz clic en el botón "Instalar".

5. **Comprueba las funcionalidades**:
   - Verifica que los menús y las vistas del módulo aparecen correctamente:
     - **Clientes**: Gestión de clientes con saldo y país asociado.
     - **Productos**: Registro de productos y categorías.
     - **Tickets**: Creación y visualización de tickets y sus líneas.

## Archivos incluidos en el módulo
- **models.py**: Define los modelos principales (Clientes, Productos, Tickets, Categorías, etc.)&#8203;:contentReference[oaicite:0]{index=0}.
- **views.xml**: Contiene las vistas de árbol y formulario para cada modelo, además de los menús principales&#8203;:contentReference[oaicite:1]{index=1}.
- **__manifest__.py**: Archivo de configuración que describe el módulo (nombre, versión, dependencias, etc.)&#8203;:contentReference[oaicite:2]{index=2}.
- **demo.xml**: Datos de demostración para probar el módulo con ejemplos preconfigurados como clientes, productos y tickets&#8203;:contentReference[oaicite:3]{index=3}.

## Créditos
- **Autor**: Marcos Navarro
- **Categoría**: Ventas
- **Versión**: 1.0
- **Compatibilidad**: Odoo 14.0 o superior
