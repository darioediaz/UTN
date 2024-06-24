import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom'
import Index from './components/Index';
import Registro from './components/Registro';
import Consulta from './components/Consulta';

import './App.css';

function App() {
  return (
    <div>
      <Router>
        <div>
          <Routes>
            <Route path='/' element={<Index />} />
            <Route path='/registro' element={<Registro />} />
            <Route path='/consulta' element={<Consulta />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;

