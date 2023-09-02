import { Link } from 'react-router-dom'
import Label from './Label'

interface ShopProps {
  name: string,
  email: string,
  phone: string,
  hours: string,
  address: string,
  url: string
}

export default function Shop({name, email, phone, hours, address, url}: ShopProps) {
  return <div className='d-flex flex-column col-sm-5 align-items-start m-sm-4'>
    <span className='h3'>{name}</span>
    <div className='d-flex'>
      <div className='d-flex col-6'>
        <Label label='Email' content={email} />
      </div>
      <div className='d-flex col-6'>
        <Label label='Phone' content={phone} />
      </div>
    </div>
    <Label label='Hours' content={hours} />
    <Label label='Address' content={address} />
    <Link to={url} className='p-3 rounded mt-5 bg-blue h3 no-hover no-link text-whitesmoke'>
      <span>Show on map</span>
    </Link>
  </div>
}