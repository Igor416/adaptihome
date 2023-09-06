import Label from './Label'

interface ShopProps {
  name: string,
  email: string,
  phone: string,
  hours: string,
  address: string
}

export default function Shop({name, email, phone, hours, address}: ShopProps) {
  return <div className='d-flex flex-column col-sm-5 align-items-start m-sm-4'>
    <span className='h3'>{name}</span>
    <Label label='Email' content={email} />
    <Label label='Phone' content={phone} />
    <Label label='Hours' content={hours} />
    <Label label='Address' content={address} />
  </div>
}