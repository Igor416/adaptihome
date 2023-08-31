import { TranslationProps } from "../../i18n";
import { OrderProps } from "../_hooks/useOrder";
import Price from "../_reusables/Price";
import Radio from "./Radio";
import Space from "./Space";

interface ShippingMethodProps extends OrderProps, TranslationProps {
  
}

export default function ShippingMethod({t, order, updateOrder}: ShippingMethodProps) {
  return <div className='d-flex my-5'>
    <Space />
    <div className='col-9 d-flex'>
      <Radio t={t} name='showroom' checked={order.shipping === 'showroom'} check={updateOrder} label={<span>{t('free')}</span>} />
      <div className='mx-4'></div>
      <Radio t={t} name='courier' checked={order.shipping === 'courier'} check={updateOrder} label={<Price discount={0} price={15} />} />
    </div>
    <Space />
  </div>
}