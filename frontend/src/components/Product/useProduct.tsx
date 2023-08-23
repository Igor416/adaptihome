import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { DetailedProduct } from "../../JSONTypes";
import { getProduct } from "../../api";

export default function useProduct() {
  const params = useParams()
  const [product, setProduct] = useState<DetailedProduct>()

  useEffect(() => {
    const category = params.category as string
    const name = params.name as string
    getProduct(category, name).then(setProduct)
  }, [params.category, params.name])

  return product
}