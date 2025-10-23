import { useState } from "react"
import { Sidebar,User2 } from "lucide-react"
import SidebarHome from "./sidebar"
import SearchBar from "./SearchBar"
export function Home(){
    const [opensidepanel,setopensidepanel]=useState(false)
   
    
    return (
        <div className="bg-white text-black flex items-start  font-bold">
            {opensidepanel&&(
                <div className="w-1/5 bg-blue-500 h-screen">
                    <SidebarHome/>
                </div>
                )
            }
            <div className=" flex justify-between p-2">
                <div className="flex  p-2">
                    <button 
                    onClick={()=>setopensidepanel(!opensidepanel)}
                    className="hover:translate-x-0.5 cursor-pointer ">
                        <Sidebar className="h-5 w-5"/>
                    </button>
    
                </div>
                
            </div>
                <div className="grid grid-cols-[150px_1fr_150px] gap-2 h-screen w-screen">
                    <div className="columns-2">

                    </div>
                    <div className="flex justify-center  items-end">
                        <div className="grid place-items-center">

                          <h1 className="p-3 text-4xl">What's On Your Mind...</h1>
                          <SearchBar />
                        </div>



                    </div>
                    <div className="flex items-start justify-end">
                        <div className="p-4">
                            <button className="cursor-pointer hover:-translate-x-0.5">

                              <User2/>
                            </button>
                            
                        </div>

                    </div>
    
                </div>        

        </div>
    )

}