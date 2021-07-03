import React,{useEffect,useState} from 'react'
import Recipes from '../components/Recipes';

const HomePage=()=>{
    const [recipes,setRecipes]=useState([]);


    const getRecipes=()=>{
        fetch("http://localhost:8000/recipes")
            .then(response=>response.json())
            .then(data=>{
                setRecipes(data)
            })
    }

    useEffect(
        ()=>{
            getRecipes()
            console.log(recipes)
        },[]
    )
    return (
        <div className="container">
            <h1>Recipes</h1>
            <Recipes list={recipes}/>
        </div>
    )
}

export default HomePage