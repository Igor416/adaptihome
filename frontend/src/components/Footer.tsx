import { faFacebookF, faInstagram } from '@fortawesome/free-brands-svg-icons';
import { faPhone } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

export default function Footer() {
  return <div className='d-flex py-5 mt-5'>
    <div className='col-3'></div>
    <div className='col-2 d-flex flex-column h5'>
      <span>Privacy Policy</span>
      <span>Terms and Conditions</span>
      <span>About Us</span>
    </div>
    <div className='col-2 d-flex justify-content-center align-items-center'>
      <div
        style={{width: '2vw', aspectRatio: 1, backgroundColor: '#4267B2'}}
        className='rounded-circle d-flex justify-content-center align-items-center text-white me-3'
      ><FontAwesomeIcon icon={faFacebookF} /></div>
      <div
        style={{width: '2vw', aspectRatio: 1, background: 'radial-gradient(circle at 30% 107%, #fdf497 0%, #fdf497 5%, #fd5949 45%,#d6249f 60%,#285AEB 90%)'}}
        className='rounded-circle d-flex justify-content-center align-items-center text-white mx-3'
      ><FontAwesomeIcon icon={faInstagram} /></div>
      <div
        style={{width: '2vw', aspectRatio: 1, background: 'linear-gradient(to top, #09ba26, #64fd80)'}}
        className='rounded-circle d-flex justify-content-center align-items-center text-white ms-3'
      ><FontAwesomeIcon icon={faPhone} /></div>
    </div>
    <div className='col-2 d-flex flex-column h5 text-end'>
      <span>Made by @Grosu Igor, 2023</span>
    </div>
    <div className='col-3'></div>
  </div>
}