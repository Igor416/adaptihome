import { useState } from "react"
import { useTranslation } from "react-i18next"
import HoverableImage from "../_reusables/HoverableImage"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faMinus, faPlus, faTimes } from "@fortawesome/free-solid-svg-icons"
import Price from "../_reusables/Price"
import SizeDisplay from "../_reusables/SizeDisplay"
import { Link, useOutletContext } from "react-router-dom"
import Hoverable from "../_reusables/Hoverable"
import { OutletContextProps } from "../App"

export default function Cart() {
  const outletContext: OutletContextProps = useOutletContext()
  const [currentStep, pickStep] = useState(0)
  const [t, i18n] = useTranslation('cart')

  return <div className='d-flex flex-column'>
    <div className='d-flex w-100 border-top border-bottom py-5'>
      <div className='col-3'></div>
      <div className='col-6 d-flex'>
        {['summary', 'address_address', 'shipping_address', 'shipping_method', "payment", "confirmation"].map((step, i) => 
          <div key={i} className={'d-flex me-4 h6 text-' + (i === currentStep ? 'blue' : 'secondary')}>
            <span className='me-1'>0{i + 1}.</span>
            <span>{t(step)}</span>
          </div>
        )}
      </div>
    </div>
    <div className='d-flex flex-wrap py-5 bg-whitesmoke'>
      <div className='col-2'></div>
      <div className='col-1 bg-white'></div>
      <div className='col-6 bg-white'>
        <div className='d-flex flex-column'>
          {outletContext.products.map((product, i) => {return product.sizes.map((size, j) => 
            <div key={i * 100 + j} className='d-flex align-items-center py-5 border-top'>
              <div className='col-2 p-2'>
                <HoverableImage src={product.shortcut} styles={{opacity: 0.9}}>

                </HoverableImage>
              </div>
              <div className='d-flex flex-column align-items-start col-2'>
                <Link to={`/product/${product.category.name}/${product.name}/`} className='h4 text-decoration-none text-dark'>
                  <Hoverable color='dark'>{product.name}</Hoverable>
                </Link>
                <span>{product.category.name_s}</span>
              </div>
              <div className='d-flex col-2 d-flex justify-content-center align-items-center h6'>
                <FontAwesomeIcon
                  onClick={() => outletContext.updateQuantity(product, size, -1)}
                  icon={faMinus}
                  style={{height: '1vh', aspectRatio: 1}}
                  className='bg-red rounded-circle p-2'
                />
                <span className='mx-3'>{size.quantity}</span>
                <FontAwesomeIcon
                  onClick={() => outletContext.updateQuantity(product, size, 1)}
                  icon={faPlus}
                  style={{height: '1vh', aspectRatio: 1}}
                  className='bg-teal rounded-circle p-2'
                />
              </div>
              <div className='col-3 h5 d-flex justify-content-center'>
                <SizeDisplay size={size} t={t} />
              </div>
              <div className='col-2 h5 d-flex justify-content-center'>
                <Price discount={0} size={size} />
              </div>
              <div onClick={() => outletContext.deleteSize(product)} className='col-1 h5 text-secondary text-end'>
                <FontAwesomeIcon icon={faTimes} />
              </div>
            </div>
          )})}
        </div>
      </div>
      <div className='col-1 bg-white'></div>
      <div className='col-2'></div>
      <div className='col-3'></div>
      <div className='d-flex flex-column col-6'>
        <div className='d-flex justify-content-between my-5 py-5 h5'>
          <span>{t('total')}</span>
          <span>
            {outletContext.total.toFixed(2)}
            <sup>EUR</sup>
          </span>
        </div>
        <div className='d-flex justify-content-between h5'>
          <div className='p-3 px-5 bg-blue rounded-pill'>
            {t('back')}
          </div>
          <div className='p-3 px-5 bg-teal rounded-pill'>
            {t('next')}
          </div>
        </div>
      </div>
      <div className='col-3'></div>
    </div>
  </div>
}