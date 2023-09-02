import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import { useOutletContext } from 'react-router-dom'
import { OutletContextProps } from '../App'
import Summary from './Summary'
import StepContainer from './StepContainer'
import ShippingAddress from './ShippingAddress'
import useOrder from '../_hooks/useOrder'
import ShippingMethod from './ShippingMethod'
import Confirmation from './Confirmation'
import { submitOrder } from '../../api'
import { ResponsiveProps } from '../..'

export default function Cart({isMobile}: ResponsiveProps) {
  const outletContext: OutletContextProps = useOutletContext()
  const [currentStep, pickStep] = useState(0)
  const {order, updateOrder, valid} = useOrder(outletContext.products, outletContext.total)
  const [t, i18n] = useTranslation('cart')

  return <div className='d-flex flex-column'>
    <div className='d-flex w-100 border-top border-bottom py-sm-5 px-sm-0 px-4'>
      <div className='col-sm-3'></div>
      <div className='col-sm-6 d-flex overflow-auto'>
        {['summary', 'shipping_address', 'shipping_method', 'confirmation'].map((step, i) => 
          <div
            key={i}
            data-bs-target='#steps'
            data-bs-slide-to={i}
            className={'d-flex text-nowrap me-4 my-sm-0 my-4 h6 text-' + (i === currentStep ? 'blue' : 'secondary')}
            onClick={() => pickStep(i)}
          >
            <span className='me-1'>0{i + 1}.</span>
            <span>{t(step)}</span>
          </div>
        )}
      </div>
    </div>
    {outletContext.products.length === 0
    ?
    <div style={{height: '45vh', paddingTop: '10vh'}} className='bg-whitesmoke text-center h4'>
      {t('no_products')}
    </div>
    :
    <div className='d-flex flex-wrap py-sm-5 bg-whitesmoke'>
      <div className='col-sm-2'></div>
      <div className='d-flex col-sm-8 col-12 p-sm-0 p-4'>
        <StepContainer>
          <Summary {...outletContext} isMobile={isMobile} />
          <ShippingAddress t={t} order={order} updateOrder={updateOrder} isMobile={isMobile} />
          <ShippingMethod t={t} order={order} updateOrder={updateOrder} isMobile={isMobile} />
          <Confirmation t={t} order={order} updateOrder={updateOrder} outletContext={outletContext} isMobile={isMobile} />
        </StepContainer>
      </div>
      <div className='col-sm-2'></div>
      <div className='col-sm-3'></div>
      <div className='d-flex flex-column col-sm-6 col-12 p-sm-0 p-4'>
        <div className={'d-flex justify-content-between h' + (isMobile ? '6' : '5')}>
          <div
            onClick={() => pickStep(currentStep === 0 ? 0 : currentStep - 1)}
            className='p-3 px-sm-5 bg-blue rounded-pill'
            data-bs-target='#steps'
            data-bs-slide='prev'
          >
            {t('back')}
          </div>
          {
            currentStep === 3
            ?
            <div
              onClick={() => valid ? submitOrder(order) : {}}
              style={{opacity: valid ? 1 : 0.5}}
              className='p-3 px-sm-5 bg-teal rounded-pill'
            >
              {t('submit')}
            </div>
            :
            <div
              onClick={() => pickStep(currentStep + 1)}
              className='p-3 px-sm-5 bg-teal rounded-pill'
              data-bs-target='#steps'
              data-bs-slide='next'
            >
              {t('next')}
            </div>}
        </div>
      </div>
      <div className='col-3'></div>
    </div>}
  </div>
}