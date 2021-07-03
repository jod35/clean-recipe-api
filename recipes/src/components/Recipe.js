import React from 'react'


const Recipe=({title,description,preparation_time})=>{
    return(
        <div className="list-group-item">
            <h3>{title}</h3>
            <p><b>preparation time</b>: {preparation_time} minutes</p>
        </div>
    )
}


export default Recipe