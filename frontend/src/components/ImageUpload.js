import React, { useState } from 'react';

function ImageUpload() {
  const [image, setImage] = useState(null);
  const [especieInfo, setEspecieInfo] = useState({});
  const [imageToShow, setImageToShow] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!image) return;

    const formData = new FormData();
    formData.append('file', image);

    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      if (data.especieInfo) {
        setEspecieInfo(data.especieInfo);
        setImageToShow(URL.createObjectURL(image)); // Actualizar imageToShow aquí
      } else {
        setEspecieInfo({ especie: 'Predicción no disponible' });
        setImageToShow(null);
      }
    } catch (error) {
      console.error('Error al enviar la imagen:', error);
      setEspecieInfo({ especie: 'Error al procesar la imagen' });
      setImageToShow(null);
    }
  };

  return (
    <div className="image-upload-container">
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleImageChange} />
        <button type="submit">Enviar Imagen</button>
      </form>
      {especieInfo.especie && (
        <>
          <p>Especie: {especieInfo.especie}</p>
          <p>Características: {especieInfo.caracteristicas}</p>
          <p>Hábitat: {especieInfo.habitat}</p>
          {imageToShow && <img src={imageToShow} alt="Imagen subida" style={{ maxWidth: '300px', maxHeight: '300px' }} />}
        </>
      )}
    </div>
  );
}

export default ImageUpload;
