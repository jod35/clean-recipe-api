import React, { useState } from 'react'


const LoginPage = () => {
    const [username, SetUsername] = useState('');
    const [password, setPassword] = useState('')
    return (
        <div className="login container">
            <div className="form">
                <div className="form-group">
                    <h1>
                        Login
                    </h1>
                </div>
                
                <div className="form-group">
                    <label>UserName</label>
                    <input type="text" 
                        value={username} 
                        onChange={(e) => { SetUsername(e.target.value) }}
                        className="form-control"
                    />
                </div>
                <br/>
                <div className="form-group">
                    <label>Password</label>
                    <input type="password" 
                        value={password} 
                        onChange={(e) => { setPassword(e.target.value) }}
                        className="form-control"
                    />
                </div>
                <br/>
                <div className="form-group">
                    <input type="submit" className="btn btn-primary" value="Login"/>
                </div>
            </div>
        </div>
    )
}


export default LoginPage