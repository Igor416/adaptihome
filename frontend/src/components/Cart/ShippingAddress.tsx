import Space from './Space';
import Input from './Input';
import { OrderProps } from '../_hooks/useOrder';
import { TranslationProps } from '../../i18n';
import { ResponsiveProps } from '../..';

export default function ShippingAddress({t, order, updateOrder, isMobile}: OrderProps & TranslationProps & ResponsiveProps) {
  return <div className='d-flex my-sm-5'>
    {!isMobile && <Space />}
    <div style={{gridTemplateColumns: 'auto '.repeat(isMobile ? 1 : 2)}} className='col-sm-9 col-12 d-grid'>
      <Input t={t} id='email' value={order.email} setter={updateOrder} side='left'/>
      <Input t={t} id='city' value={order.city} setter={updateOrder} side='right' />
      <Input t={t} id='phone' value={order.phone} setter={updateOrder} side='left' />
      <Input t={t} id='address' value={order.address} setter={updateOrder} side='right' />
    </div>
    {!isMobile && <Space />}
  </div>
}