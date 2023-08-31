import { TranslationProps } from "../../i18n";
import { OutletContextProps } from "../App";
import { OrderProps } from "../_hooks/useOrder";
import Checkable from "../_reusables/Checkable";
import Price from "../_reusables/Price";
import Input from "./Input";
import Space from "./Space";
import Summary from "./Summary";

interface ConfirmationProps extends OrderProps, TranslationProps {
  outletContext: OutletContextProps
}

export default function Confirmation({t, order, updateOrder, outletContext}: ConfirmationProps) {
  return <div className='d-flex flex-column'>
    <Summary {...outletContext} showTotal={false} />
    <div className='d-flex my-5'>
      <Space color='white' />
      <div className='col-9 d-flex flex-column bg-white py-5'>
        <span>{t('shipping_info')}</span>
        <div style={{gridTemplateColumns: 'auto '.repeat(2)}} className='mt-2 d-grid'>
          <Input t={t} id='email' value={order.email} setter={updateOrder} side='left' disabled />
          <Input t={t} id='city' value={order.city} setter={updateOrder} side='right' disabled />
          <Input t={t} id='phone' value={order.phone} setter={updateOrder} side='left' disabled />
          <Input t={t} id='address' value={order.address} setter={updateOrder} side='right' disabled />
        </div>
      </div>
      <Space color='white' />
    </div>
    <div className='d-flex my-5'>
      <Space />
      <div className='col-9 d-flex flex-column py-5 h5'>
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
      <Space />
    </div>
  </div>
}