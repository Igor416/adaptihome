import { Size } from "../../JSONTypes";

export default function useDiscount(size: Size, productDiscount: number) {
  return size.price * (100 - Math.max(size.discount, productDiscount)) / 100 * size.quantity
}