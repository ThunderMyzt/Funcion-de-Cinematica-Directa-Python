# Implementación de Cinemática Directa Simbólica para Robots RR, RRR y SCARA

## 1. Breve Introducción

La cinemática de robots es una de las áreas fundamentales de la robótica que se encarga de estudiar el movimiento de los mismos sin considerar las fuerzas que lo producen. Específicamente, la **cinemática directa** busca determinar la posición y orientación del efector final del robot en el espacio, a partir de sus valores articulares (giros en las articulaciones o desplazamientos).

El método de **Denavit-Hartenberg (D-H)** es un algoritmo estándar que permite sistematizar este proceso, asignando sistemas de coordenadas a cada eslabón del robot para obtener una matriz de transformación homogénea que relaciona un eslabón con el siguiente. La multiplicación consecutiva de estas matrices nos da la matriz de transformación total, que describe la ubicación del efector final respecto a la base del robot.

En este proyecto, se implementó la cinemática directa simbólica de tres configuraciones de robots distintas, utilizando el lenguaje de programación **Python** y la librería `SymPy` para el manejo de variables simbólicas. El desarrollo se realizó en el entorno de Visual Studio Code, basándonos en el código proporcionado en el repositorio [DH-Forward-Kinematics-Function---Python](https://github.com/SolKacil/DH-Forward-Kinematics-Function---Python) y los parámetros D-H del libro "Control de robots manipuladores" de Fernando Reyes Cortés.

El objetivo es obtener la **matriz de transformación homogénea simbólica** ($^0T_E$) para cada robot, la cual nos da la información de la posición y orientación del efector final de forma algebraica.

---

## 2. Metodología

El procedimiento consistió en adaptar el código base de Python para que, en lugar de recibir valores numéricos, trabajara con variables simbólicas que representan los parámetros D-H de cada robot. Para cada configuración, se siguió el mismo proceso:

1.  **Identificar los parámetros D-H**: Se extrajeron las tablas con los parámetros de Denavit-Hartenberg para cada robot del libro de texto.
2.  **Definir variables simbólicas**: En el script de Python, se crearon los símbolos necesarios para las variables articulares ($q_i$) y las longitudes de los eslabones ($l_i$) usando la librería `SymPy`.
3.  **Construir la tabla de parámetros simbólica**: Se creó una lista en Python que representa la tabla D-H, utilizando las variables simbólicas definidas en el paso anterior.
4.  **Calcular la matriz de transformación**: Se utilizó la función `ForwardKinematicsDH.symbolic()` del código base, pasándole como argumento la tabla de parámetros simbólica para que calculara la matriz de transformación homogénea final.

A continuación, se detalla la implementación para cada uno de los robots analizados.

### Robot Planar de 2 Grados de Libertad (RR)

Este robot, también conocido como RR (Rotacional-Rotacional), es un manipulador simple que se mueve en un plano y consta de dos articulaciones de revolución.

![Esquema del robot planar RR](RbtPlanar.png)

Los parámetros D-H para este robot, obtenidos del libro, son los siguientes:

![Tabla de parámetros D-H del robot RR](MtrzDHPlanar.png)

Estos parámetros se tradujeron al script de Python, definiendo `q1`, `q2`, `l1` y `l2` como variables simbólicas para construir la tabla de parámetros que se le pasó a la función de cálculo.

### Robot Antropomórfico de 3 Grados de Libertad (RRR)

Este robot RRR (Rotacional-Rotacional-Rotacional) se asemeja a un brazo humano, con tres articulaciones de revolución que le permiten alcanzar una mayor área de trabajo en un espacio tridimensional.

![Esquema del robot antropomórfico RRR](RbtRRR.png)

La tabla de parámetros Denavit-Hartenberg para esta configuración es:

![Tabla de parámetros D-H del robot RRR](MtrzDHRRR.png)

En el script de Python, se definieron las variables simbólicas `q1`, `q2`, `q3`, `l1`, `l2` y `l3`. Un detalle importante en la implementación fue la representación del parámetro $\alpha_1 = 90^{\circ}$, que en la librería `SymPy` se debe indicar en radianes como `sp.pi/2` para que los cálculos simbólicos de seno y coseno sean correctos.

### ⚙️ Robot de Configuración SCARA (RRP)

El robot SCARA (Selective Compliance Assembly Robot Arm) es ampliamente utilizado en tareas de ensamblaje. Su configuración RRP (Rotacional-Rotacional-Prismática) consta de dos articulaciones de revolución y una articulación prismática, lo que le da rigidez en el eje Z pero flexibilidad en el plano XY.

![Esquema del robot SCARA](RbtSCARA.png)

Sus correspondientes parámetros D-H se muestran en la siguiente tabla:

![Tabla de parámetros D-H del robot SCARA](DHRbtSCARA.png)

Para este robot, se definieron las variables simbólicas `q1`, `q2`, `d3`, `l1` y `l2`. La tercera articulación es prismática, por lo que su variable articular es `d3` (un desplazamiento lineal) en lugar de un ángulo $q$.

---

## 3. Resultados

Al ejecutar cada uno de los scripts de Python, se imprimió en la terminal la matriz de transformación homogénea simbólica final ($^0T_E$). Esta matriz de 4x4 contiene en su submatriz de 3x3 superior izquierda la **orientación** del efector final y en la última columna la **posición** (x, y, z) del mismo, todo expresado de forma algebraica en función de las variables articulares.

Los resultados obtenidos fueron verificados exitosamente, comparándolos con las matrices de resultado que se presentan en el libro de texto.

### Resultado: Robot Planar (RR)

La matriz obtenida en la terminal para el robot RR fue:

![Resultado en terminal para el robot RR](RbtPlanarVC.png)

Esta coincide con la matriz de transformación homogénea presentada en la bibliografía:

![Matriz de transformación homogénea para el robot RR](MtrzHomgPlanar.png)

### Resultado: Robot Antropomórfico (RRR)

La salida en la terminal para el robot RRR fue la siguiente:

![Resultado en terminal para el robot RRR](RbtRRRVC.png)

La cual es equivalente a la matriz de transformación que se muestra en el libro:

![Matriz de transformación homogénea para el robot RRR](MtrzHomgRRR.png)

### Resultado: Robot SCARA (RRP)

Finalmente, la matriz simbólica obtenida para la configuración SCARA fue:

![Resultado en terminal para el robot SCARA](RbtSCARAVC.png)

Este resultado también fue validado y coincide con la matriz final del libro:

![Matriz de transformación homogénea para el robot SCARA](MtrzHomgSCARA.png)

La correcta obtención de estas matrices demuestra que la implementación de la cinemática directa simbólica a partir de los parámetros D-H se realizó de manera exitosa.