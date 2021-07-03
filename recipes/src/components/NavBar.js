import React from 'react'
import LoginPage from '../pages/Login'
import SignUpPage from '../pages/SignUp'
import 'bootstrap/dist/css/bootstrap.min.css'

import HomePage from '../pages/Home'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link

} from 'react-router-dom'

const NavBar=()=>{
    return (
        <Router>
        <div>
            <ul className="nav justify-content-center">
                <li className="nav-item">
                    <Link to="/" className="nav-link">Home</Link>
                </li>
                <li className="nav-item">
                    <Link to="/login" className="nav-link">Login</Link>
                </li>
                <li className="nav-item">
                    <Link to="/signup" className="nav-link">Sign Up</Link>
                </li>
            </ul>
        </div>
        <Switch>
                <Route path="/login">
                    <LoginPage/>
                </Route>
                <Route path="/signup">
                    <SignUpPage/>
                </Route>
                <Route path="/">
                    <HomePage/>
                </Route>
            </Switch>
        </Router>
        
    )
}

export default NavBar