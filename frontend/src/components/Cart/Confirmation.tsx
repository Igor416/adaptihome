import { ResponsiveProps } from '../..';
import { TranslationProps } from '../../i18n';
import { OutletContextProps } from '../App';
import { OrderProps } from '../_hooks/useOrder';
import Checkable from '../_reusables/Checkable';
import Price from '../_reusables/Price';
import Input from './Input';
import Space from './Space';
import Summary from './Summary';

interface ConfirmationProps extends OrderProps, TranslationProps, ResponsiveProps {
  outletContext: OutletContextProps
}

export default function Confirmation({t, order, updateOrder, outletContext, isMobile}: ConfirmationProps) {
  return <div className='d-flex flex-column'>
    <Summary {...outletContext} showTotal={false} isMobile={isMobile} />
    <div className='d-flex my-5'>
      {!isMobile && <Space />}
      <div className='col-sm-9 col-12 d-flex flex-column bg-white py-sm-5 p-2 px-sm-0'>
        <span>{t('shipping_info')}</span>
        <div style={{gridTemplateColumns: 'auto '.repeat(isMobile ? 1 : 2)}} className='mt-2 d-grid'>
          <Input t={t} id='email' value={order.email} setter={updateOrder} side='left' disabled />
          <Input t={t} id='city' value={order.city} setter={updateOrder} side='right' disabled />
          <Input t={t} id='phone' value={order.phone} setter={updateOrder} side='left' disabled />
          <Input t={t} id='address' value={order.address} setter={updateOrder} side='right' disabled />
        </div>
      </div>
      {!isMobile && <Space />}
    </div>
    <div className='d-flex my-5'>
      {!isMobile && <Space />}
      <div className='col-sm-9 col-12 d-flex flex-column py-5 h5'>
        <div className='py-2 border-bottom'>
          <Checkable checked onChecked={() => {}} value='Accept Terms & Conditions' multiple />
        </div>
        <div className='py-4 border-bottom d-flex justify-content-between'>
          <span>{t('subtotal')}</span>
          <Price discount={0} price={outletContext.total} />
        </div>
        <div className='py-4 border-bottom d-flex justify-content-between'>
          <span>{t('shipping')}</span>
          <Price discount={0} price={order.shipping === 'showroom' ? 0 : 15} />
        </div>
        <div className='py-4 border-bottom d-flex justify-content-between'>
          <span>{t('total')}</span>
          <Price discount={0} price={outletContext.total + (order.shipping === 'showroom' ? 0 : 15)} />
        </div>
      </div>
      {!isMobile && <Space />}
    </div>
  </div>
}