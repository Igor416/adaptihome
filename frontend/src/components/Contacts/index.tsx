import Shop from './Shop';
import Centralizer from '../_reusables/Centralizer';
import MarginImage from '../_reusables/MarginImage';
import SideText from '../_reusables/SideText';
import { ResponsiveProps } from '../..';

export default function Contacts({isMobile}: ResponsiveProps) {
  return <Centralizer>
    <div className='d-flex flex-column align-items-center p-sm-5 p-4 h3 text-center'>
      <SideText text='contacts' right='18' isMobile={isMobile} />
      <div className='d-flex flex-wrap w-100 text-start'>
        <Shop
          name='Cyprus Showroom'
          email='adaptihomecy@gmail.com'
          phone='+3579691747'
          hours='Monday - Friday / 09:00 - 18:00'
          address='Gravias, 4, Pyrgos, 4529, Limassol, Cyprus'
        />
      </div>
      <MarginImage src='https://rabatabil.ro/img/theme/contacts.jpg' isMobile={isMobile} />
    </div>
  </Centralizer>
}