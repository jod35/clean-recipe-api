import React from 'react'
import ReactDOM from 'react-dom'
import 'bootstrap/dist/css/bootstrap.min.css'
import './styles/main.css'
import NavBar from './components/NavBar'




const App=()=>{
    return (
        <div className="app">
            <NavBar/>
        </div>
    )
}

ReactDOM.render(<App/>,document.getElementById('root'));

