import { useState } from 'react'
import './App.css'
import {Routes,Route,useLocation} from 'react-router-dom'
import { Home } from './pages/Home'

function App() {
  
  const location=useLocation()
  return (
    <>
      <div>
        <Routes location={location}>
          <Route path='/' element={<Home/>}/>

           
          

        </Routes>
      </div>
    </>
  )
}

export default App
