import { Size } from "../../JSONTypes";
import useDiscount from "../_hooks/useDiscount";

interface PriceProps {
  discount: number,
  size?: Size,
  price?: number,
  from?: string
}

export default function Price({discount, size, price, from}: PriceProps) {
  const val = useDiscount(size, price, discount)

  return <div className='d-flex flex-nowrap'>
    {from && <span className='me-1'>{from}</span>}
    <span className={discount != 0 ? 'text-teal' : ''}>
      {val.toFixed(2)}
    </span>
    <sup>EUR</sup>
  </div>
}