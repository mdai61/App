import React, { useState } from 'react';
import { uploadFile } from './api';

const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleUpload = async () => {
    if (file) {
      const response = await uploadFile(file);
      console.log(response);
    }
  };

  return (
    <div>
      <input type='file' onChange={(e) => setFile(e.target.files?.[0] || null)} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
};

export default App;