# LLM Output

=== FILE: src/App.jsx ===
import React, { useState, useEffect } from 'react'
import { HashRouter, Routes, Route, Link } from 'react-router-dom'
import axios from 'axios'
import { ToastContainer } from 'react-toastify'
import { toast } from 'react-toastify'
import { FiPlus } from 'react-icons/fi'
import { FiTrash2 } from 'react-icons/fi'
import { FiHeart } from 'react-icons/fi'
import { format } from 'date-fns'
import { useForm } from 'react-hook-form'
import { clsx } from 'clsx'

const BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000"

function App() {
  const [recipes, setRecipes] = useState([])
  const [favourites, setFavourites] = useState([])
  const [user, setUser] = useState(null)
  const { register, handleSubmit } = useForm()

  useEffect(() => {
    axios.get(`${BASE_URL}/recipes`)
      .then(response => {
        setRecipes(response.data)
      })
      .catch(error => {
        console.error(error)
      })

    axios.get(`${BASE_URL}/user`)
      .then(response => {
        setUser(response.data)
      })
      .catch(error => {
        console.error(error)
      })
  }, [])

  const handleAddRecipe = (data) => {
    axios.post(`${BASE_URL}/recipes`, data)
      .then(response => {
        setRecipes([...recipes, response.data])
        toast.success('Recipe added successfully')
      })
      .catch(error => {
        console.error(error)
        toast.error('Failed to add recipe')
      })
  }

  const handleDeleteRecipe = (id) => {
    axios.delete(`${BASE_URL}/recipes/${id}`)
      .then(response => {
        setRecipes(recipes.filter(recipe => recipe.id !== id))
        toast.success('Recipe deleted successfully')
      })
      .catch(error => {
        console.error(error)
        toast.error('Failed to delete recipe')
      })
  }

  const handleFavouriteRecipe = (id) => {
    axios.post(`${BASE_URL}/favourites`, { recipeId: id })
      .then(response => {
        setFavourites([...favourites, response.data])
        toast.success('Recipe favourited successfully')
      })
      .catch(error => {
        console.error(error)
        toast.error('Failed to favourite recipe')
      })
  }

  const handleUnfavouriteRecipe = (id) => {
    axios.delete(`${BASE_URL}/favourites/${id}`)
      .then(response => {
        setFavourites(favourites.filter(favourite => favourite.id !== id))
        toast.success('Recipe unfavourited successfully')
      })
      .catch(error => {
        console.error(error)
        toast.error('Failed to unfavourite recipe')
      })
  }

  return (
    <HashRouter>
      <ToastContainer />
      <div className="container mx-auto p-4 pt-6">
        <h1 className="text-3xl font-bold mb-4">Recipe Book</h1>
        <ul className="flex flex-wrap justify-center mb-4">
          <li className="mr-4">
            <Link to="/" className="text-blue-500 hover:text-blue-700">Recipes</Link>
          </li>
          <li className="mr-4">
            <Link to="/favourites" className="text-blue-500 hover:text-blue-700">Favourites</Link>
          </li>
          <li className="mr-4">
            <Link to="/add-recipe" className="text-blue-500 hover:text-blue-700">Add Recipe</Link>
          </li>
        </ul>
        <Routes>
          <Route path="/" element={
            <div>
              <h2 className="text-2xl font-bold mb-4">Recipes</h2>
              <ul>
                {recipes.map(recipe => (
                  <li key={recipe.id} className="mb-4">
                    <h3 className="text-xl font-bold">{recipe.name}</h3>
                    <p>Ingredients: {recipe.ingredients.join(', ')}</p>
                    <p>Cooking Steps: {recipe.cookingSteps.join(', ')}</p>
                    <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" onClick={() => handleDeleteRecipe(recipe.id)}>
                      <FiTrash2 className="mr-2" />
                      Delete
                    </button>
                    <button className="bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded" onClick={() => handleFavouriteRecipe(recipe.id)}>
                      <FiHeart className="mr-2" />
                      Favourite
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          } />
          <Route path="/favourites" element={
            <div>
              <h2 className="text-2xl font-bold mb-4">Favourites</h2>
              <ul>
                {favourites.map(favourite => (
                  <li key={favourite.id} className="mb-4">
                    <h3 className="text-xl font-bold">{favourite.recipe.name}</h3>
                    <p>Ingredients: {favourite.recipe.ingredients.join(', ')}</p>
                    <p>Cooking Steps: {favourite.recipe.cookingSteps.join(', ')}</p>
                    <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" onClick={() => handleUnfavouriteRecipe(favourite.id)}>
                      <FiTrash2 className="mr-2" />
                      Unfavourite
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          } />
          <Route path="/add-recipe" element={
            <div>
              <h2 className="text-2xl font-bold mb-4">Add Recipe</h2>
              <form onSubmit={handleSubmit(handleAddRecipe)}>
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="name">Name</label>
                <input className="shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" id="name" {...register('name')} />
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="ingredients">Ingredients</label>
                <input className="shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" id="ingredients" {...register('ingredients')} />
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="cookingSteps">Cooking Steps</label>
                <input className="shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" id="cookingSteps" {...register('cookingSteps')} />
                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">
                  <FiPlus className="mr-2" />
                  Add Recipe
                </button>
              </form>
            </div>
          } />
        </Routes>
      </div>
    </HashRouter>
  )
}

export default App
=== END ===

=== FILE: src/main.jsx ===
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
)
=== END ===

=== FILE: src/index.css ===
@tailwind base;
@tailwind components;
@tailwind utilities;
=== END ===

=== FILE: src/api.js ===
// No need for this file as API calls are made directly from App.js
=== END ===