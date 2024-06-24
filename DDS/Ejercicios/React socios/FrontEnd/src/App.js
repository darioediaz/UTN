import './App.css';
import {Menu} from './components/Menu';
import { Inicio } from './components/Inicio';
import Articulos from './components/Articulos';
import Socio from './components/Socio';

import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Menu />
      <div className="app-body">
        <Routes>
          <Route path="/inicio" element={<Inicio />} />
          <Route path="/articulos" element={<Articulos />} />
          <Route path="/socios" element={<Socio />} />

          <Route path="*" element={<Navigate to="/inicio" replace />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
