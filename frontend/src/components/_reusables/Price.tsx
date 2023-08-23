import { Size } from "../../JSONTypes";
import useDiscount from "../_hooks/useDiscount";

interface PriceProps {
  discount: number,
  size: Size,
  from?: string
}

export default function Price({discount, size, from}: PriceProps) {
  const price = useDiscount(size, discount)

  return <div className='d-flex flex-nowrap'>
    {from && <span className='me-1'>{from}</span>}
    <span className={discount != 0 ? 'text-teal' : ''}>
      {price.toFixed(2)}
    </span>
    <sup>EUR</sup>
  </div>
}