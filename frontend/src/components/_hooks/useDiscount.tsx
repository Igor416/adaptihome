import { Size } from "../../JSONTypes";

export default function useDiscount(size?: Size, price?: number, productDiscount: number = 0) {
  if (size) {
    return size.price * (100 - Math.max(size.discount, productDiscount)) / 100 * size.quantity
  }
  else if (price) {
    return price * (100 - productDiscount) / 100
  }
  return 0
}