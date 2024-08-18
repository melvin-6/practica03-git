<!DOCTYPE html>
<html lang="es">
</html>
<head>
  <meta charset="utf-8">
  <title>Formación Virtual | Bienvenida</title>
  <link href="https://fonts.googleapis.com/css?family=Stint+Ultra+Condensed" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed" rel="stylesheet">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
</body>
<header class="header">
  <h1>
    <img src="images/logo.png" alt="Logo">
  </h1>
</header>
 <nav class="navbar">
  <a href="#inicio">Inicio</a>
  <a href="#quienes-somos">Quiénes Somos</a>
  <a href="#servicios">Servicios</a>
  <a href="#tarifas">Tarifas</a>
  <a href="#localizacion">Localización</a>
</nav>
<section id="quienes-somos" class="content who">
  <h2 class="title">Quiénes Somos</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt enim eligendi similique, necessitatibus quos atque.</p>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
</section>
<section id="servicios" class="content services">
  <h2 class="title">Servicios</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perferendis obcaecati dolores, vel iusto perspiciatis voluptates quasi quam mollitia reiciendis porro.</p>
  <ul class="list-services">
    <li>
      <figure>
        <img src="images/ico1.png" alt="Angular">
        <figcaption>Angular</figcaption>
      </figure>
    </li>
    <li>
      <figure>
        <img src="images/ico2.png" alt="React">
        <figcaption>React</figcaption>
      </figure>
    </li>
    <li>
      <figure>
        <img src="images/ico3.png" alt="Vuejs">
        <figcaption>Vuejs</figcaption>
      </figure>
    </li>
  </ul>
</section>
<section id="tarifas" class="content tarifas">
  <article class="contain">
    <h2 class="title">Tarifas</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptas, odit. Beatae nostrum delectus, perspiciatis illum!</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
    <a href="#contacto" class="btn">Contáctanos</a>
  </article>
</section>
<section id="localizacion" class="content localization">
  <h2 class="title">Localización</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quae quas molestias quibusdam cum corrupti deserunt, explicabo ipsam id, itaque iste!</p>
  <div id="map"></div>
  <h3>Formulario de Contacto</h3>
  <form id="contacto" action="enviar_formulario.php" method="POST">
    <label for="nombre">Nombre:</label>
    <input type="text" id="nombre" name="nombre" required>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <label for="mensaje">Mensaje:</label>
    <textarea id="mensaje" name="mensaje" required></textarea>
    <button type="submit">Enviar</button>
  </form>
</section>
<footer class="footer">
  <p>&copy; 2024 Fazt. Todos los derechos reservados.</p>
  <nav class="footer-nav">
    <a href="#inicio">Inicio</a>
    <a href="#quienes-somos">Quiénes Somos</a>
    <a href="#servicios">Servicios</a>
    <a href="#tarifas">Tarifas</a>
    <a href="#localizacion">Localización</a>
    <a href="#contacto">Contacto</a>
  </nav>
</footer>
