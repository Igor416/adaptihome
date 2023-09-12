export interface SearchResults {
  categories: Array<{
    link: string,
    category: string,
    count: string
  }>,
  products: Array<{
    link: string,
    category: string,
    name: string,
    price: number,
    discount: number
  }>
}

export interface Size {
  width: number,
  length: number,
  price: number,
  discount: number,
  quantity: number
}

export interface MattressColectionPrice {
  [key: string]: number
}

export interface Filters {
  order: string[],
  [key: string]: string[]
}

export interface Category {
  name: string,
  name_s: string,
  name_pl: string
}

export interface Product {
  name: string,
  discount: number,
  category: Category,
  shortcut: string,
  sizes: Size[]
}

export interface DetailedProduct extends Product {
  suggestions: Product[],
  desc: string,
  article: string,
  images: string[]
  structure: Array<{
    image: string,
    name: string,
    desc: string
  }>
  characteristic:  {
    [key: string]: string | string[] | number | boolean
  },
  dimensions: {
    [key: string]: number | number[]
  }
}

export interface Order {
  id: string,
  products: Product[],
  total: number,
  email: string,
  city: string,
  phone: string,
  address: string,
  shipping: string,
  [key: string]: string | number | Product[]
}