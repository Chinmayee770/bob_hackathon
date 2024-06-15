import React from 'react'
import Button from '@mui/material/Button';
import Avatar from '@mui/material/Avatar';



const Navbar = () => {
  return (
    <>
    <div className='bg-[#ff5b2e] w-full flex justify-between'>
        <img src='./logo.png' className='h-20'></img>
        <div className='text-4xl font-bold text-white pt-4'>Title by BOB</div>
        <Avatar className='mt-4 mr-5'>PG</Avatar>

    </div>
    </>
  )
}


export default Navbar