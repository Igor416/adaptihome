import { faMinus, faPlus, faTimes } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { t } from 'i18next'
import { Link } from 'react-router-dom'
import Hoverable from '../_reusables/Hoverable'
import HoverableImage from '../_reusables/HoverableImage'
import Price from '../_reusables/Price'
import SizeDisplay from '../_reusables/SizeDisplay'
import Space from './Space'
import { OutletContextProps } from '../App'
import { ResponsiveProps } from '../..'

interface SummaryProps extends OutletContextProps, ResponsiveProps {
  showTotal?: boolean
}

export default function Summary({products, total, updateQuantity, deleteSize, isMobile, showTotal = true}: SummaryProps) {
  return <div className='d-flex flex-wrap'>
    {!isMobile && <Space color='white' />}
    <div className='col-sm-9 d-flex flex-column bg-white'>
      {products.map((product, i) => {return product.sizes.map((size, j) => 
        <div key={i * 100 + j} className={'d-flex flex-sm-row flex-column align-items-sm-center py-2 py-sm-5' + (products.length > 1 ? ' border-bottom' : '')}>
          <div className='d-flex col-sm-4 align-items-center'>
            <div className='col-6 p-2'>
              <HoverableImage src={product.shortcut} styles={{opacity: 0.9}}>

              </HoverableImage>
            </div>
            <div className='d-flex flex-column align-items-start col-4 col-sm-6'>
              <Link to={`/product/${product.category.name}/${product.name}/`} className='h4 text-decoration-none text-dark'>
                <Hoverable color='dark'>{product.name}</Hoverable>
              </Link>
              <span>{product.category.name_s}</span>
            </div>
            {isMobile && <div onClick={() => deleteSize(product)} className='col-2 h5 text-secondary text-end pe-2'>
              <FontAwesomeIcon icon={faTimes} />
            </div>}
          </div>
          <div className='d-flex justify-content-between align-items-center col-sm-5 p-2 py-4 py-sm-0'>
            <div className='d-flex col-sm-5 d-flex justify-content-center align-items-center h6'>
            {showTotal && <FontAwesomeIcon
                onClick={() => updateQuantity(product, size, -1)}
                icon={faMinus}
                style={{height: '1vh', aspectRatio: 1}}
                className='bg-red rounded-circle p-2'
              />}
              <span className={'mx-3' + (!showTotal ? ' h5' : '')}>{showTotal ? '' : 'x'}{size.quantity}</span>
              {showTotal && <FontAwesomeIcon
                onClick={() => updateQuantity(product, size, 1)}
                icon={faPlus}
                style={{height: '1vh', aspectRatio: 1}}
                className='bg-teal rounded-circle p-2'
              />}
            </div>
            <div className='col-sm-7 h5 d-flex justify-content-center'>
              <SizeDisplay size={size} t={t} />
            </div>
          </div>
          <div className='col-12 col-sm-2 h5 d-flex justify-content-sm-center justify-content-end py-4 py-sm-0'>
            <Price discount={0} size={size} />
          </div>
          {!isMobile && <div onClick={() => deleteSize(product)} className='col-1 h5 text-secondary text-end'>
            <FontAwesomeIcon icon={faTimes} />
          </div>}
        </div>
      )})}
    </div>
    {!isMobile && <Space color='white' />}
    {!isMobile && showTotal && <Space />}
    {showTotal && <div className='col-sm-9 col-12 d-flex justify-content-between my-sm-5 py-sm-5 my-3 h5'>
      <span>{t('total')}</span>
      <span>
        {total.toFixed(2)}
        <sup>EUR</sup>
      </span>
    </div>}
    {!isMobile && showTotal && <Space />}
  </div>
}