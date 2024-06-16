import React from 'react'
import Button from '@mui/material/Button';
import Avatar from '@mui/material/Avatar';



const Navbar = () => {
  return (
    <>
    <div className='bg-[#ff5b2e] shadow-md flex justify-between mt-3 mr-4 ml-4 rounded-full'>
      <div className='flex justify-start'>
        <img src='./logo copy.png' className='h-14 pl-10'></img>
        <div className='text-2xl font-bold text-white pt-3 pl-5'>Walter White</div>
      </div>
      <div className='flex justify-around'>
      <div className='text-xl font-bold text-white pt-3 mr-4'>Contact</div>
      <div className='text-xl font-bold text-white pt-3 mr-4'>Features</div>
      <div className='text-xl font-bold text-white pt-3 mr-36'>About</div>
      </div>
        <Avatar className='mt-2 mr-5'>PG</Avatar>
    </div>
    </>
  )
}


export default Navbar