export interface SearchResults {
  categories: Array<{
    link: string,
    text: string,
    count: string
  }>,
  products: Array<{
    link: string,
    text: string,
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
  [key: string]: {
    price: number
  }
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
  desc: string,
  images: string[],
  structure: Array<{
      image: string,
      name: string,
      desc: string
  }>
  characteristic:  {
    [key: string]: string | string[] | number | boolean
  }
}

export interface Order {
  products: Product[],
  total: string,
  name: string,
  town: string,
  address: string,
  phone: string,
  payment: string,
  courier: string
}