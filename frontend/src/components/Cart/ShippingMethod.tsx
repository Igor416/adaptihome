import { ResponsiveProps } from '../..';
import { TranslationProps } from '../../i18n';
import { OrderProps } from '../_hooks/useOrder';
import Price from '../_reusables/Price';
import Radio from './Radio';
import Space from './Space';

export default function ShippingMethod({t, order, updateOrder, isMobile}: OrderProps & TranslationProps & ResponsiveProps) {
  return <div className='d-flex my-sm-5'>
    {!isMobile && <Space />}
    <div className='col-sm-9 col-12 d-flex flex-column flex-sm-row'>
      <Radio
        t={t}
        name='showroom'
        checked={order.shipping === 'showroom'}
        check={updateOrder}
        label={<span>{t('free')}</span>}
        isMobile={isMobile}
      />
      <div className='mx-4'></div>
      <Radio
        t={t}
        name='courier'
        checked={order.shipping === 'courier'}
        check={updateOrder}
        label={<Price discount={0} price={15} />}
        isMobile={isMobile}
      />
    </div>
    {!isMobile && <Space />}
  </div>
}