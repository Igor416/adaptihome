import { Link } from "react-router-dom";
import Centralizer from "../_reusables/Centralizer";
import HoverableImage from "../_reusables/HoverableImage";
import SideText from "../_reusables/SideText";
import TextBlock from "./TextBlock";
import MarginImage from "../_reusables/MarginImage";
import LinkImage from "../_reusables/LinkImage";

export default function About() {
  return <Centralizer>
    <div className='d-flex flex-column align-items-center p-5 h3 text-center'>
      <SideText text='about' right='10' />
      <span className='h1'>Bringing your story and vision to life.</span>
      <MarginImage src='https://rabatabil.ro/img/cms/1295%D1%85633.jpg' />
      <TextBlock
        section='Our Studio.'
        heading='We work side by side with you to create exceptional spaces.'
        t1='Our furniture are very well designed and they meet the requirements of people who care both for design and quality. We are a producer of multifunctiomal furniture which can change your living space in moments.'
        t2='We make modules of transformable furniture and accessories which will help to equip your living space and increase the usable area of the room.'
      />
      <MarginImage src='https://flatstudio.md/img/cms/11f.jpg' />
      <TextBlock
        section='Our Mission.'
        heading='We manufacture goods that serve people.'
        t1=''
        t2='Flat curates a selection of objects focused on quality, minimalism, and functionality. Our mission is to provide a unique set of products that fascinate and inspire the user. We review each product, down to its packaging, to ensure that we continuously provide the best in both quality and design.'
      />
      <MarginImage src='https://flatstudio.md/img/cms/10a.jpg' />
      <TextBlock
        section='Our products.'
        heading='We create personalized design solutions.'
        t1=''
        t2='We create designs that are not only visually-stunning, but smart, enduring, and functional with big strategic thinking influencing every single decision.'
      />
      <div className='d-flex flex-column'>
        <div className='d-flex mb-5'>
          <img className='me-5' src='https://flatstudio.md/img/cms/14.jpg' />
          <img src='https://flatstudio.md/img/cms/4.jpg' />
        </div>
        <div className='d-flex'>
          <img className='me-5' src='https://flatstudio.md/img/cms/5a.jpg' />
          <img src='https://flatstudio.md/img/cms/6.jpg' />
        </div>
      </div>
      <TextBlock
        section='Our Achievments.'
        heading='Our expertise. Your needs. In perfect alignment.'
        t1=''
        t2='This isn’t about us. It’s about you. That’s why we check our tastes at the door and listen with intention. Together we can create something amazing. We’re quick to respond and known for our personal attention.'
      />
      <TextBlock
        section='Our products'
        heading='We create customized design solutions'
        t1=''
        t2='We create products that are not only innovative, but also smart, reliable and functional, with an excellent strategic idea for each solution.'
      />
      <LinkImage to='/contacts' image='https://rabatabil.ro/img/footeradvanced/type_contact.jpg'>Get in touch with us</LinkImage>
    </div>
  </Centralizer>
}