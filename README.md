# Método de Euler para la ecuación diferencial separable y' = 1 + y

Este proyecto implementa y compara dos soluciones para la ecuación diferencial separable:

\[
\frac{dy}{dt} = 1 + y, \quad y(0) = 0
\]

Se resuelve de dos maneras:

1. Solución analítica usando separación de variables  
2. Aproximación numérica usando el método de Euler

---

## 1. Solución analítica (método de separación de variables)

Partimos de la ecuación:

\[
\frac{dy}{dt} = 1 + y
\]

La ecuación es separable, por lo que se reescribe como:

\[
\frac{1}{1 + y}\, dy = dt
\]

Integramos ambos lados:

\[
\ln|1 + y| = t + C
\]

Despejamos:

\[
1 + y = e^{t + C} = C e^t
\]

Aplicando la condición inicial \(y(0) = 0\):

\[
0 = C - 1 \quad \Rightarrow \quad C = 1
\]

Solución exacta:

\[
y(t) = e^t - 1
\]

---

## 2. Método de Euler

Para aproximar la solución se utiliza:

- Intervalo: \( t \in [0, 1] \)  
- Paso: \( h = 0.2 \)  
- Condición inicial: \( y(0) = 0 \)

La fórmula de Euler es:

\[
y_{n+1} = y_n + h\, f(t_n, y_n)
\]

Con \( f(t, y) = 1 + y \).

El archivo `euler_1_mas_y.py`:

- Implementa la función \( f(t, y) \)  
- Aplica el método de Euler  
- Calcula la solución exacta  
- Imprime una tabla comparativa

---

## 3. Cómo ejecutar el proyecto

### Crear un entorno virtual (opcional):

```bash
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias 

pip install -r requirements.txt

# Ejecutar el programa

python3 euler_1_mas_y.py
