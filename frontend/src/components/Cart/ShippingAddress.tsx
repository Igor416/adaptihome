import Space from "./Space";
import Input from "./Input";
import { OrderProps } from "../_hooks/useOrder";
import { TranslationProps } from "../../i18n";

interface ShippingAddressProps extends OrderProps, TranslationProps {
  
}

export default function ShippingAddress({t, order, updateOrder}: ShippingAddressProps) {
  return <div className='d-flex my-5'>
    <Space />
    <div style={{gridTemplateColumns: 'auto '.repeat(2)}} className='col-9 d-grid'>
      <Input t={t} id='email' value={order.email} setter={updateOrder} side='left'/>
      <Input t={t} id='city' value={order.city} setter={updateOrder} side='right' />
      <Input t={t} id='phone' value={order.phone} setter={updateOrder} side='left' />
      <Input t={t} id='address' value={order.address} setter={updateOrder} side='right' />
    </div>
    <Space />
  </div>
}