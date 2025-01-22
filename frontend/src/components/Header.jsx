import {} from 'react';
import {} from 'react-router-dom';

const Header = () => {
  
    return(
      <header className="d-flex align-items-center px-3 py-2 border-bottom">
        <h2 className="me-auto">Rebecca</h2>
        <button id="dark-mode-toggle" className="btn btn-secondary me-2">Toggle Dark Mode</button>
        <button id="logout-button" className="btn btn-outline-danger" >Logout</button>
        <button 
          className="btn btn-outline-primary" 
          data-bs-toggle="offcanvas" 
          data-bs-target="#settingsPanel">
          <i className="bi bi-sliders"></i> Settings
      </button>
      </header>
    )
  };
  
  export default Header;
  