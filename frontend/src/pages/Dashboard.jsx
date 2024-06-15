import React from 'react'
import Navbar from '../components/Navbar'
import Sidebar from '../components/Sidebar'
import DbMain from '../components/DbMain'

const Dashboard = () => {
  return (
    <>
    <Navbar />
    <div className='flex'>
        <Sidebar />
        <DbMain />
    </div>
    </>
  )
}

export default Dashboard