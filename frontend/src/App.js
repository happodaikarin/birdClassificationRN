import React from 'react';
import './App.css';
// Importa el componente ImageUpload
import ImageUpload from './components/ImageUpload';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Predicción de Especies de Aves</h1>
        <p>Carga una imagen para ver la predicción.</p>
        {/* Incluye el componente ImageUpload */}
        <ImageUpload />
      </header>
    </div>
  );
}

export default App;
