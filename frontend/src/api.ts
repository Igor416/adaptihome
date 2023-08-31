import Cookies from 'js-cookie'
import { Product, DetailedProduct, MattressColectionPrice, Order, SearchResults } from './JSONTypes'


export function sendSearch(search: string): Promise<SearchResults> {
  const url = 'search/'
  
  return sendPostRequest<string, SearchResults>(url, search)
}

export function getMattressColectionsPrice(): Promise<MattressColectionPrice[]> {
  const url = 'mattress_category_prices/'

  return sendGetRequest<MattressColectionPrice[]>(url)
}

export function getProducts(): Promise<Product[]> {
  const url = location.pathname.replace('/shop/', 'products/') + location.search

  return sendGetRequest<Product[]>(url);
}

export function getProduct(category: string, name: string): Promise<DetailedProduct> {
  const url = `product/${category}/${name}/`

  return sendGetRequest<DetailedProduct>(url);
}

export function getOrder(id: string): Promise<Order> {
  const url = `order/${id}/` 

  return sendGetRequest<Order>(url)
}

export function sendOrder(products: Product[], total: number): Promise<Order> {
  const url = `order/-1/` 

  return sendPostRequest<{products: Product[], total: number}, Order>(url, {products: products, total: total})
}

export function updateOrderProducts(id: string, products: Product[], total: number): Promise<Order> {
  const url = `order/${id}/` 

  return sendPatchRequest<{products: Product[], total: number}, Order>(url, {products: products, total: total})
}

export function submitOrder(order: Order): Promise<Order> {
  const url = `order/${order.id}/` 

  return sendPatchRequest<Order, Order>(url, order)
}

async function sendGetRequest<T>(url: string): Promise<T> {
  return sendRequest<T, T>(url, 'GET')
}

async function sendPostRequest<T, R>(url: string, body: T): Promise<R> {
  return sendRequest<T, R>(url, 'POST', body)
}

async function sendPatchRequest<T, R>(url: string, body: T): Promise<R> {
  return sendRequest<T, R>(url, 'PATCH', body)
}

async function sendRequest<T, R>(url: string, method: string, body?: T): Promise<R> {
  const options = {
    method: method,
    headers: {
      'X-CSRFToken': Cookies.get('csrftoken') as string,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  }
  const response = await (method === 'GET' ? fetch('/api/' + url) : fetch('/api/' + url, options));
  const data = await response.json();
  return data;
}