import React from'react'
import Recipe from './Recipe'

const Recipes=({list})=>{

   
    
    return(
        <div className="recipes list-group">
            {
                list.map(
                    (item,index)=>(
                        <Recipe 
                            title={item.title} 
                            preparation_time={item.preparation_time}
                            description={item.description}
                            key={index}
                        />
                    )
                )
            }
        </div>
    )
}


export default Recipes