<div align="center">
<h1>Taller 2</h1>
  <p>
    Ingeniería Electrónica · Universidad Santo Tomás
    <br>
    <b>Didier Posse</b>
    <br>
    <em>Primer punto</em>
  </p>
</div>

<hr>

<div align="center">
  <h2>Dockerización de Drones</h2>
</div>

<ol>
  <li><br>
    <div align="center">
      <p><img width="850" src="https://github.com/user-attachments/assets/da5cf12a-2cc8-4aca-a0f9-a3b4ed683d68"/></p>
    </div>
    <p>
      Para comenzar con la <b>dockerización de los drones</b>, se crea una carpeta llamada <b>Drones</b>, donde se guardarán todos los archivos necesarios.
      A diferencia de otras simulaciones, en este caso <b>no es necesario un archivo <i>requirements.txt</i></b> ni mover manualmente el repositorio, ya que el <b>Dockerfile</b> se encarga de clonar automáticamente el repositorio <i>gym-pybullet-drones</i> desde GitHub dentro del contenedor.
    </p>
    <p>
      Dentro de esta carpeta se crea únicamente el archivo <b>Dockerfile</b>, el cual contiene todas las instrucciones necesarias para descargar el repositorio, instalar las dependencias principales (<i>pybullet, numpy, gymnasium</i> y <i>stable-baselines3</i>), y ejecutar el ejemplo de control PID de los drones.
      Antes de construir la imagen, se ejecuta el comando <code>xhost +local:docker</code> para permitir las conexiones X11 necesarias para mostrar el entorno gráfico.
      Finalmente, la imagen se construye con el comando: <code>docker build -t drones .</code>
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width="850" src="https://github.com/user-attachments/assets/60d77b62-c487-41d6-91e3-8b4e6686ef35"/></p>
    </div>
    <p>
      En la imagen se muestra el contenido del archivo <b>Dockerfile</b>, donde se muestra que desde aqui se puede descargar el repositorio donde esta la simulación y las dependencias que necesitamos para Dockerizar, en este archivo se         pueden ver los comandos que conforman la configuración del entorno.
      A continuación, se explica brevemente la función de cada línea:
    </p>
    <ul>
      <li><b>FROM ubuntu:22.04</b> → Define la imagen base del sistema.</li>
      <li><b>ENV DEBIAN_FRONTEND=noninteractive</b> → Evita las preguntas interactivas durante la instalación de paquetes.</li>
      <li><b>RUN apt-get update && apt-get install -y ...</b> → Instala las dependencias necesarias: Python, Git, librerías gráficas (OpenGL, Xvfb, mesa-utils), y limpia la caché al final para reducir el tamaño de la imagen.</li>
      <li><b>WORKDIR /app</b> → Define la carpeta de trabajo dentro del contenedor.</li>
      <li><b>RUN git clone https://github.com/utiasDSL/gym-pybullet-drones.git .</b> → Clona el repositorio de los drones directamente en el contenedor.</li>
      <li><b>RUN pip3 install pybullet numpy gymnasium stable-baselines3</b> → Instala las dependencias de Python necesarias para la simulación.</li>
      <li><b>RUN pip3 install -e .</b> → Instala el paquete <i>gym-pybullet-drones</i> en modo desarrollo.</li>
      <li><b>CMD ["python3", "gym_pybullet_drones/examples/pid.py"]</b> → Comando por defecto que ejecuta el ejemplo del control PID con múltiples drones.</li>
    </ul>
  </li>

  <li><br>
    <div align="center">
      <p><img width="850" src="https://github.com/user-attachments/assets/05d0a105-a4f9-4bfd-afbd-3df3f031d4f6"/></p>
    </div>
    <p>
      Finalmente, se ejecuta el contenedor con el siguiente comando:
    </p>
    <p align="center">
      <code>docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --network host drones</code>
    </p>
    <p>
      Este comando permite que la simulación se ejecute con su entorno gráfico habilitado correctamente, mostrando los drones en PyBullet.
      Aquí ya se observa la simulación corriendo con entorno visual dentro del contenedor, utilizando <b>PyBullet</b> como motor principal.
      En este caso, se muestran <b>tres drones</b> siguiendo una trayectoria circular mediante control PID, demostrando el funcionamiento completo del sistema dockerizado.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width="850" src="https://github.com/user-attachments/assets/7613c7f0-3ba0-496a-a55a-e27f04d76b68"/></p>
    </div>
    <p>
      En esta parte se muestra la simulación corriendo dentro del contenedor, pero desde la terminal.
      Es decir, el código que genera la simulación sin usar el entorno gráfico. 
      Este modo se utiliza cuando se busca <b>optimizar recursos</b> o cuando solo se necesita la información que aparece directamente en la consola, como los datos de control o desempeño de los drones.
    </p>
  </li>
</ol>

<hr>

<div align="center">
  <p><em>Segundo Punto</em></p>
</div>

<hr>

<div align="center">
  <h2>Dockerización de Baxter</h2>
</div>

<ol>
  <li><br>
    <div align="center">
      <p><img width="850" src="https://github.com/user-attachments/assets/e6ea1561-db70-4f7b-b25e-6957999e4729"/></p>
    </div>
    <p>
      Para la <b>dockerización del robot Baxter</b>, se crea una carpeta llamada <b>Baxter</b> donde se guardan los archivos necesarios. 
      Al igual que en la simulación de los drones, <b>no es necesario un archivo <i>requirements.txt</i></b> ni copiar manualmente el repositorio, 
      ya que el <b>Dockerfile</b> se encargará de clonar automáticamente el repositorio <i>pybullet_robots</i> desde GitHub dentro del contenedor.
    </p>
    <p>
      Dentro de la carpeta se crea únicamente el archivo <b>Dockerfile</b>, el cual contiene las instrucciones para descargar el repositorio, 
      instalar las dependencias principales (<i>pybullet</i> y <i>numpy</i>), y ejecutar el demo de <b>cinemática inversa (Inverse Kinematics)</b> del robot Baxter.
      Antes de construir la imagen, se ejecuta el comando <code>xhost +local:docker</code> para habilitar las conexiones X11, necesarias para el entorno gráfico. 
      Finalmente, se construye la imagen con el comando: <code>docker build -t baxter .</code>
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width="850" src="https://github.com/user-attachments/assets/1f009467-8e89-4b63-bc3c-46ab622dc309"/></p>
    </div>
    <p>
      El archivo <b>Dockerfile</b> sigue prácticamente el mismo proceso usado en la simulación de los drones, ya que mantiene la misma estructura de configuración. 
      La diferencia principal es que Baxter requiere <b>más librerías y dependencias</b>, por lo que se deben instalar algunas adicionales para que el entorno funcione correctamente. 
      Fuera de eso, la lógica de construcción del contenedor es la misma que en el caso anterior.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width="850" src="https://github.com/user-attachments/assets/77b47eda-94b1-4ea7-83fe-5d0ee4566ac8"/></p>
    </div>
    <p>
      Una vez configurado todo, se ejecuta el contenedor con el siguiente comando:
    </p>
    <p align="center">
      <code>docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --network host baxter</code>
    </p>
    <p>
      Este comando permite habilitar el <b>entorno gráfico</b> correctamente para visualizar el robot Baxter en <b>PyBullet</b>.  
      Finalmente, se puede observar cómo la simulación se ejecuta dentro del contenedor, mostrando al robot realizando movimientos de 
      <b>cinemática inversa</b> con ambos brazos, alcanzando objetivos marcados como <b>“TARGET”</b> dentro del entorno de simulación.
    </p>
  </li>

  <li><br>
    <div align="center">
      <p><img width="850" src="https://github.com/user-attachments/assets/6478b5d5-eabe-42e7-a304-2ba316f982c5"/></p>
    </div>
    <p>
      Al igual que en la simulación anterior, aquí se muestra el contenedor ejecutándose desde el <b>terminal de Ubuntu</b>, 
      donde se pueden ver las características y datos de la simulación sin el entorno gráfico.  
      Este modo se utiliza en <b>casos específicos</b>, cuando solo se requiere la información del sistema o se desea ahorrar recursos del equipo.
    </p>
  </li>
</ol>

<hr>

<div align="center">
  <p><em>Tercer Punto</em></p>
</div>

<hr>

<div align="center">
  <h2>Dockerización de Atlas</h2>
</div>

<ol>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/3054a9be-3d13-4954-82cd-e15373560c43"/></p>
    </div>
    <p>
      Para la Dockerización del robot humanoide Atlas, se crea una carpeta llamada <b>Atlas</b> donde se colocan los archivos necesarios. Al igual que con Baxter, no se requiere un archivo <i>requirements.txt</i>, ya que el <i>Dockerfile</i> clona automáticamente el repositorio <b>pybullet_robots</b> desde GitHub. 
      Dentro de esta carpeta se crea el archivo <i>Dockerfile</i>, que se encarga de descargar el repositorio, instalar las dependencias necesarias (<i>pybullet</i> y <i>numpy</i>), y ejecutar el script <b>atlas.py</b>, el cual carga y simula el robot Atlas. 
      Antes de construir la imagen, se usa el comando <code>xhost +local:docker</code> para habilitar el entorno gráfico, y finalmente se construye la imagen con <code>docker build -t atlas .</code>
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/97a0bdcb-4dcc-4af4-81e2-06bb311d3d53"/></p>
    </div>
    <p>
      El archivo <i>Dockerfile</i> de Atlas es prácticamente idéntico al de Baxter, ya que ambos provienen del mismo repositorio <b>pybullet_robots</b> y comparten las mismas dependencias del sistema. 
      La única diferencia está en el comando final (<code>CMD</code>), donde en lugar de ejecutar <i>baxter_ik_demo.py</i>, se ejecuta <b>atlas.py</b>, que simula el robot humanoide Atlas con sus articulaciones y su física realista. 
      Fuera de eso, la estructura y configuración del archivo son exactamente las mismas, lo que facilita su adaptación entre ambos proyectos.
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/34b56e46-9ac3-4ed2-820f-49253ea10ccc"/></p>
    </div>
    <p>
      Una vez construida la imagen, se ejecuta el contenedor con el comando:
      <br><code>docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw --network host atlas</code>
      <br>Este comando habilita el entorno gráfico para visualizar el robot Atlas en <b>PyBullet</b>. 
      La simulación se muestra con el robot humanoide en posición de pie sobre un plano, con todas sus articulaciones listas para moverse. 
      En el terminal de Ubuntu se pueden observar datos del entorno de simulación, aunque sin tantos detalles gráficos, ya que estos se aprecian directamente en PyBullet.
    </p>
  </li>
  <li><br>
    <div align="center">
      <p><img width=850 src="https://github.com/user-attachments/assets/aebcc2e5-e4b3-4dea-a8ee-1a9ab223dac1"/></p>
    </div>
    <p>
      Finalmente, se muestra la simulación interactiva de Atlas dentro de PyBullet. 
      En este entorno, la cámara se controla con el ratón, mientras que las teclas se utilizan para activar o desactivar capas del renderizado. 
      Es recomendable moverse por el entorno para observar el modelo desde diferentes ángulos, ya que la vista inicial puede estar alejada del robot. 
      Esta interacción permite apreciar de mejor forma los movimientos y el comportamiento dinámico del robot Atlas.
    </p>
  </li>
</ol>
