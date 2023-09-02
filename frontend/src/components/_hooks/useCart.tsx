import { useEffect, useState } from 'react';
import { Product, Size } from '../../JSONTypes';
import Cookies from 'js-cookie';
import useDiscount from './useDiscount';
import { getOrder, sendOrder, updateOrderProducts } from '../../api';

export default function useCart() {
  const [total, setTotal] = useState(0)
  const [count, setCount] = useState(0)
  const [products, setProducts] = useState<Product[]>([])
  const [fetched, fetch] = useState(false)

  useEffect(() => {
    const orderId = Cookies.get('orderId')
    if (orderId) {
      getOrder(orderId).then(resp => {
        fetch(true)
        setProducts(resp.products)  
      })
    } else {
      fetch(true)
      setProducts([])
    }
  }, [])

  useEffect(() => {
    if (fetched) {
      let total = 0;
      for (let product of products) {
        for (let size of product.sizes) {
          total += useDiscount(size, product.discount)
        }
      }
      setTotal(total);
      let count = 0;
      for (let product of products) {
        for (let size of product.sizes) {
          count += size.quantity
        }
      }
      setCount(count)

      const orderId = Cookies.get('orderId')
      if (orderId) {
        updateOrderProducts(orderId, products, total).then(_ => {})
      } else if (products.length > 0) {
        sendOrder(products, total).then(resp => Cookies.set('orderId', resp.id, { expires: 30 }))
      }
    }
  }, [products])

  const addSize = (product: Product) => {
    const copy = [...products]
    const duplicates = products.filter(pr => pr.name === product.name)
    if (duplicates.length) {
      const duplicate = duplicates[0]
      const sizesDuplicted = duplicate.sizes.filter(s => s.length === product.sizes[0].length && s.width === product.sizes[0].width)

      if (sizesDuplicted.length) {
        return updateQuantity(duplicate, sizesDuplicted[0], 1)
      } else {
        copy[products.indexOf(duplicate)].sizes.push(product.sizes[0])
      }
    } else {
      copy.push(product)
    }
    setProducts(copy)
  }

  const deleteSize = (product: Product) => {
    const copy = [...products]
    const target = products.filter(pr => pr.name === product.name)[0]
    target.sizes = target.sizes.filter(s => s.length !== product.sizes[0].length && s.width !== product.sizes[0].width)
    if (target.sizes.length) {
      copy[products.indexOf(product)] = target
    } else {
      copy.splice(products.indexOf(product), 1)
    }
    
    setProducts(copy)
  }

  const updateQuantity = (product: Product, size: Size, value: number) => {
    const copy = [...products]
    const prev = copy[products.indexOf(product)].sizes[product.sizes.indexOf(size)].quantity
    if (prev + value < 1 || prev + value > 99) {
      return
    }
    copy[products.indexOf(product)].sizes[product.sizes.indexOf(size)].quantity += value;
    setProducts(copy)
  }

  const clearProduct = (product: Product, size: Size) => {
    return {
      name: product.name,
      discount: product.discount,
      category: product.category,
      shortcut: product.shortcut,
      sizes: [size]
    }
  }

  return {
    products: products,
    total: total,
    count: count,
    addSize: addSize,
    deleteSize: deleteSize,
    updateQuantity: updateQuantity,
    clearProduct: clearProduct
  }
}