import { Size } from "../../JSONTypes";

interface OldPriceProps {
  discount: number,
  size?: Size
  price?: number
}

export default function OldPrice({discount, size, price}: OldPriceProps) {
  if (discount > 0) {
    return <div className='mb-2 me-2 text-red h6'>
      <span style={{textDecoration: 'line-through'}}>{size ? size.price : price}</span>
      <sup>EUR</sup>
    </div>
  }
  return <></>
}