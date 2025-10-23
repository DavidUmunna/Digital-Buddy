import { useState } from "react"
export default function SearchBar(){
  const [Value,setValue]=useState("")
  return (
    <>
    <div className="relative w-full p-4">
         <input
            type="text"
            onChange={(e)=>setValue(e.target.value)}
            className="border-2 border-gray-300 rounded-3xl w-full px-60 py-6 pr-14 text-lg text-left  focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
           {!Value && (
             <div className="absolute left-8 bottom-8 text-gray-400 pointer-events-none">
               Type Anything...
             </div>
           )}
          <button
            className="absolute right-2 top-1/2 transform -translate-y-1/2 bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 mr-5"
           >
             Go
          </button>
    </div>

    </>
  )
}