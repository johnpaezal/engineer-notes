Ejemplo global:
Meta de usuario:
Meta suave: Quiero poder registrarme y acceder fácilmente a mi cuenta.
(Es un tipo de meta a conseguir/eliminar)

Necesidad de usuario:
El usuario necesita registrarse y acceder a su cuenta en el sistema.
(Se clasifica como necesidad articulada, ya que el usuario expresó: "Quiero poder registrarme y acceder fácilmente a mi cuenta.")

Requerimiento de usuario:
Registrar y permitir el inicio de sesión del usuario.
(El requerimiento es de tipo Usuario).

Historia de usuario:
Como usuario, quiero poder registrarme y acceder a mi cuenta para utilizar las funcionalidades del sistema.

Características del sistema (funcionalidades):
El sistema deberá permitir el registro de nuevos usuarios solicitando información básica: nombre, correo, contraseña.
Si el correo ingresado ya está registrado, entonces el sistema deberá mostrar un mensaje de error indicando que el correo ya está en uso.
Cuando un usuario ingrese sus credenciales correctas, el sistema deberá permitir el acceso a su cuenta.
…

Test de aceptación:
Dado que un usuario ingresa sus datos de registro válidos, cuando confirme el registro, entonces el sistema deberá crear una cuenta y permitir el inicio de sesión.
Dado que un usuario intenta registrarse con un correo ya existente, cuando confirme el registro, entonces el sistema deberá mostrar un mensaje de error indicando que el correo ya está en uso.
Dado que un usuario tiene una cuenta registrada, cuando ingrese sus credenciales correctas, entonces el sistema deberá permitir el acceso.
…



-------------------------------------

Category: Structural
Importance: High
Usage: Core of object-oriented design. Defines classes, attributes, methods, and relationships.



## Ejemplo Global
*De la meta al test de aceptación*

### Meta de usuario
**Meta suave**: Quiero poder registrarme y acceder fácilmente a mi cuenta
*(tipo: conseguir/eliminar)*

### Necesidad de usuario
El usuario necesita registrarse y acceder a su cuenta en el sistema
*(clasificación: articulada — el usuario lo expresó directamente)*

### Requerimiento
Registrar y permitir el inicio de sesión del usuario
*(tipo: requerimiento de usuario)*

### Historia de usuario
```
Como usuario, quiero poder registrarme y acceder a mi cuenta
para utilizar las funcionalidades del sistema.
```

### Características del sistema
- El sistema deberá permitir el registro solicitando nombre, correo y contraseña
- Si el correo ya está registrado, el sistema deberá mostrar un mensaje de error
- Cuando un usuario ingrese sus credenciales correctas, el sistema deberá permitir el acceso

### Tests de aceptación
```
Dado que un usuario ingresa datos de registro válidos,
cuando confirme el registro,
entonces el sistema deberá crear una cuenta y permitir el inicio de sesión.

Dado que un usuario intenta registrarse con un correo ya existente,
cuando confirme el registro,
entonces el sistema deberá mostrar un mensaje de error.

Dado que un usuario tiene una cuenta registrada,
cuando ingrese sus credenciales correctas,
entonces el sistema deberá permitir el acceso.
```

---

*Fuente: Ingeniería de Software I*