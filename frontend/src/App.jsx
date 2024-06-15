import React from 'react'
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import  Home  from './pages/Home';
import Dashboard from './pages/Dashboard';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
    
  )
}

export default App