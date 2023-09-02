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
          email='office@rabatabil.ro'
          phone='0747202000 / 0790584741'
          hours='Monday - Friday / 09:00 - 18:00'
          address='500210, Brasov, Bulevardul Muncii 4, Brasov, România'
          url='https://www.google.com/maps/dir//rabatabil.ro,+Bulevardul+Muncii+4,+Bra%C8%99ov+500281,+Romania/@45.6427027,25.6161151,16z/data=!4m9!4m8!1m0!1m5!1m1!1s0x40b35da3e0728d8d:0x87598ad5a7ea650!2m2!1d25.6159415!2d45.6423555!3e0?hl=en'
        />
      </div>
      <MarginImage src='https://rabatabil.ro/img/theme/contacts.jpg' isMobile={isMobile} />
    </div>
  </Centralizer>
}