import Cookies from 'js-cookie'
import { Product, DetailedProduct, MattressColectionPrice, Order, SearchResults, Filters } from './JSONTypes'


export function sendSearch(search: string): Promise<SearchResults> {
  const url = '/api/search/'
  
  return sendPostRequest<string, SearchResults>(url, search)
}

export function getMattressColectionsPrice(): Promise<MattressColectionPrice[]> {
  const url = '/api/mattress_category_prices/'

  return sendGetRequest<MattressColectionPrice[]>(url)
}

export function getProducts(): Promise<Product[]> {
  const url = location.pathname.replace('shop/', 'api/products/')

  return sendGetRequest<Product[]>(url);
}

export function getProduct(category: string, name: string): Promise<DetailedProduct> {
  const url = `/api/product/${category}/${name}/`

  return sendGetRequest<DetailedProduct>(url);
}

export function sendOrder(data: Order): Promise<Order> | string {
  for (let key in data) {
    if (data[key as keyof Order] == '') {
      return 'error: empty'
    }
  }
  const url = '/telegram/order/'

  return sendPostRequest<Order, Order>(url, data)
}

async function sendPostRequest<T, R>(url: string, body: T): Promise<R> {
  const options = {
    method: 'POST',
    headers: {
      'X-CSRFToken': Cookies.get('csrftoken') as string,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  }
  const response = await fetch(url, options);
  const data = await response.json();
  return data;
}

async function sendGetRequest<T>(url: string): Promise<T> {
  const response = await fetch(url + location.search);
  const data = await response.json();
  return data;
}