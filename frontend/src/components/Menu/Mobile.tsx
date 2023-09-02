import { i18n } from "i18next";
import { TranslationProps } from "../../i18n";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { useEffect, useState } from "react";
import { faBars, faShoppingCart, faTimes } from "@fortawesome/free-solid-svg-icons";
import { Link, useLocation } from "react-router-dom";
import Links from "./Links";
import SearchBar from "./SearchBar";

interface MobileMenuProps extends TranslationProps {
  i18n: i18n,
  count: number,
}

export default function MobileMenu({t, i18n, count}: MobileMenuProps) {
  const [opened, open] = useState(false)
  const location = useLocation()

  useEffect(() => 
    open(false)
  , [location])

  useEffect(() => {
    document.body.style.overflowY = opened ? 'hidden' : 'visible'
  }, [opened])
  
  return <div className='d-flex justify-content-between align-items-center h2 p-4'>
    <Link to='/' className='d-flex align-items-center text-decoration-none'>
      <img style={{width: '10vw', aspectRatio: 1}} src='/static/images/logo.svg' />
      <div className='d-flex ms-2'>
        <span className='text-red'>Adapti</span>
        <span className='text-blue'>Home</span>
      </div>
    </Link>
    <div className='d-flex justify-content-end align-items-center'>
      <FontAwesomeIcon onClick={() => open(!opened)} icon={opened ? faTimes : faBars} />
      <Link
        to='/cart'
        style={{width: '10vw', aspectRatio: 1}}
        className='ms-2 bg-teal position-relative d-flex align-items-center justify-content-center rounded-circle h4'
      >
        <FontAwesomeIcon icon={faShoppingCart} color='white'/>
        <div
          style={{
            width: '6vw',
            marginTop: '-2vw',
            marginRight: '-2vw',
            aspectRatio: 1
          }}
          className='position-absolute end-0 top-0 d-flex align-items-center justify-content-center bg-blue rounded-circle h6'>
          <span>{count}</span>
        </div>
      </Link>
    </div>
    <div style={{
      top: 'calc(10vw + 3rem)',
      zIndex: opened ? 1200 : -1,
      height: 'calc(100vh - 10vw - 3rem)',
      transformOrigin: 'left',
      transform: `translateX(${opened ? '0' : '-100%'})`
    }} className='position-absolute d-flex flex-column justify-content-between px-4 w-100 start-0 transition bg-white'>
      <SearchBar t={t} isMobile={true} />
      <div className='d-flex flex-column align-items-center'>
        <Links t={t} />
      </div>
      <div />
    </div>
  </div>
}