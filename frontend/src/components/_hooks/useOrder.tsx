import { useEffect, useState } from 'react';
import { Order, Product } from '../../JSONTypes';
import Cookies from 'js-cookie';
import { getOrder } from '../../api';

export interface OrderProps {
  order: Order,
  updateOrder: (key: string, value: string) => void,
  valid?: boolean
}

export default function useOrder(products: Product[], total: number): OrderProps {
  const [valid, setValid] = useState(false)
  const [order, setOrder] = useState<Order>({
    id: '',
    products: products,
    total: total,
    email: '',
    city: 'Lemasos',
    phone: '',
    address: '',
    shipping: 'showroom'
  })

  useEffect(() => {
    const orderId = Cookies.get('orderId')
    if (orderId) {
      getOrder(orderId).then(setOrder)
    }
  }, [])

  useEffect(() => {
    const copy = {...order}
    copy.products = products
    setOrder(copy)
  }, [products])

  useEffect(() => {
    const copy = {...order}
    copy.total = total
    setOrder(copy)
  }, [total])

  const updateOrder = (key: string, value: string) => {
    const copy = {...order}
    copy[key] = value
    setOrder(copy)
  }

  const validateOrder = () => {
    for (let key of Object.keys(order)) {
      if (!order[key]) {
        console.log(key, order[key])
        setValid(false)
        return
      }
    }
    setValid(true)
  }

  useEffect(validateOrder, [order])

  return {
    order: order,
    updateOrder: updateOrder,
    valid: valid
  }
}