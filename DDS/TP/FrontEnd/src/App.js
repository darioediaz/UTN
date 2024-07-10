import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import "./App.css";
import { Footer } from "./components/Footer";
import { Inicio } from "./components/Inicio";
import { Menu } from "./components/Menu";

import { ModalDialog } from "./components/ModalDialog";
import { Login } from "./components/login/Login";

import { Cancion } from "./components/canciones/Canciones";
import { Juego } from "./components/juegos/Juegos";
import { Libro } from "./components/libros/Libros";
import { Pelicula } from "./components/peliculas/Peliculas";
import { Serie } from "./components/series/Series";
import { Artista } from "./components/artistas/Artistas";
import { Deporte } from "./components/deportes/Deportes";
import { RedSocial } from "./components/redesSociales/RedesSociales";

function App() {
  return (
    <>
      <BrowserRouter>
        <ModalDialog />
        <Menu />
        <div className="divBody">
          <Routes>
            <Route path="/inicio" element={<Inicio />} />
            <Route path="/libros" element={<Libro />} />
            <Route path="/peliculas" element={<Pelicula />} />
            <Route path="/canciones" element={<Cancion />} />
            <Route path="/juegos" element={<Juego />} />
            <Route path="/series" element={<Serie />} />
            <Route path="/artistas" element={<Artista />} />
            <Route path="/deportes" element={<Deporte />} />
            <Route path="/redes-sociales" element={<RedSocial />} />
            <Route path="/login/:componentFrom" element={<Login />} />
            <Route path="*" element={<Navigate to="/inicio" replace />} />
          </Routes>
        </div>
        <Footer />
      </BrowserRouter>
    </>
  );
}
export default App;
