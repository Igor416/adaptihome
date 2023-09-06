import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Link, LinkFilters } from '../..';

export default function useCategory(category: string, setCategory: (val: string) => void, links: Link[]): LinkFilters[] {
  const params = useParams()
  const navigate = useNavigate()
  const [fetched, fetch] = useState(false)

  useEffect(() => {
    if (!params.category || links.filter(l => l.name === params.category).length === 0) {
      navigate(`/shop/FoldingBed/` + location.search)
      fetch(true)
      return
    }
    fetch(true)
    setCategory(params.category)
  }, [])

  useEffect(() => {
    if (fetched) {
      if (params.category === category) {
        return
      }
      navigate(`/shop/${category}/` + location.search)
    }
  }, [category])
  
  return links.filter(l => l.name === params.category)[0]?.filters
}