import Icons from './Icons';
import { ResponsiveProps } from '../..';

export default function Footer({isMobile}: ResponsiveProps) {
  return <div className='d-flex flex-sm-row flex-column py-sm-5 px-sm-0 p-4 mt-5 h6'>
    <div className='col-sm-3'></div>
    <div className='col-sm-2 d-flex text-center text-sm-start flex-column'>
      <span>Privacy Policy</span>
      <span>Terms and Conditions</span>
      <span>About Us</span>
    </div>
    <div className='col-sm-2 d-flex justify-content-center align-items-center py-5 py-sm-0'>
      <Icons isMobile={isMobile}/>
    </div>
    <div className='col-sm-2 d-flex flex-column text-center text-sm-end'>
      <span>Made by @Grosu Igor, 2023</span>
      <span>tel: +3579691747</span>
      <span>mail: +3579691747</span>
    </div>
    <div className='col-sm-3'></div>
  </div>
}