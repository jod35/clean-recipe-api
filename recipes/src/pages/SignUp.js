import React, { useState } from 'react'


const SignUpPage =()=>{
    const [username,SetUsername]=useState('')
    const [email,setEmail]=useState('')
    const [password,setPassword]=useState('')





    const signUpUser=(e)=>{
        e.preventDefault();

        const requestOptions={
            method:"POST",
            headers:{
                "content-type":"application/json",
            },
            body:JSON.stringify({
                username:username,
                email:email,
                password:password,
            })
            
        }

        fetch("http://localhost:8000/signup/",requestOptions)
        .then(response=>{response.json()})
        .then(data=>alert(data.message))

        setPassword('')
        SetUsername('')
        setEmail('')
    }
    return(
        <div className="signup container">
            <form onSubmit={signUpUser}>
            <div className="form">
                <div className="form-group">
                    <h1>
                        Sign Up
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
                    <label>Email</label>
                    <input type="text" 
                        value={email} 
                        onChange={(e) => { setEmail(e.target.value) }}
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
            </form>
        </div>
    )
}


export default SignUpPage