import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faShoppingCart } from '@fortawesome/free-solid-svg-icons'
import { useTranslation } from 'react-i18next';
import Hoverable from '../_reusables/Hoverable';
import SearchBar from './SearchBar';

interface CountProps {
  count: number
}

export default function Menu({count}: CountProps) {
  const [t, i18n] = useTranslation('menu')

  return <div className='d-flex align-items-center w-100 py-5'>
    <div className='d-flex justify-content-center col-3'>
      <img style={{width: '5vw', aspectRatio: 1}} src='/static/images/logo.svg' />
      <div className='d-flex ms-2 flex-column justify-content-end'>
        <span className='h2 text-red'>Adapti</span>
        <span className='h1 text-blue'>Home</span>
      </div>
    </div>
    <div className='d-flex h4 col-3'>
      <Link to='/' className='text-decoration-none'>
        <Hoverable color='blue'>{t('home')}</Hoverable>
      </Link>
      <div className='mx-2' />
      <Link to='/shop/folding_bed/' className='text-decoration-none'>
        <Hoverable color='blue'>{t('products')}</Hoverable>
      </Link>
      <div className='mx-2' />
      <Link to='/about' className='text-decoration-none'>
        <Hoverable color='blue'>{t('about')}</Hoverable>
      </Link>
      <div className='mx-2' />
      <Link to='/contacts' className='text-decoration-none'>
        <Hoverable color='blue'>{t('contacts')}</Hoverable>
      </Link>
    </div>
    <div className='d-flex align-items-center col-3 flex-nowrap'>
      <SearchBar t={t} />
      <div className='mx-4' />
      <div className='d-flex flex-nowrap h3'>
        <div onClick={() => i18n.changeLanguage('en')}>
          <Hoverable color='blue' isActive={'en' === i18n.language}>en</Hoverable>
        </div>
        <div className='mx-2' />
        <div onClick={() => i18n.changeLanguage('gr')}>
          <Hoverable color='blue' isActive={'gr' === i18n.language}>gr</Hoverable>
        </div>
      </div>
    </div>
    <div className='d-flex h2 justify-content-center align-items-center col-3 pe-5'>
      <Link to='/cart' className='text-decoration-none'>
        <Hoverable color='blue'>{t('cart')}</Hoverable>
      </Link>
      <Link
        to='/cart'
        style={{width: '3vw', aspectRatio: 1}}
        className='ms-2 bg-teal position-relative d-flex align-items-center justify-content-center rounded-circle h4'
      >
        <FontAwesomeIcon icon={faShoppingCart} color='white'/>
        <div
          style={{
            width: '1.5vw',
            marginTop: '-0.5vw',
            marginRight: '-0.5vw',
            aspectRatio: 1
          }}
          className='position-absolute end-0 top-0 d-flex align-items-center justify-content-center bg-blue rounded-circle h6'>
          <span>{count}</span>
        </div>
      </Link>
    </div>
  </div>
}