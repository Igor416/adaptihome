import { useNavigate, useSearchParams } from 'react-router-dom';
import { Filters } from '../../JSONTypes'
import { useState, useEffect } from 'react';
import { LinkFilters } from '../..';

export default function useFilters(filters: Filters, setFilters: (val: Filters) => void, validFilters: LinkFilters[]): (key: string, multiple: boolean, value: string) => void {
  const searchParams = useSearchParams()
  const navigate = useNavigate()
  const [fetched, fetch] = useState(false)
  
  useEffect(() => {
    const copy: Filters = {order: ['low']}
    searchParams[0].forEach((value, key) => {
      if (key === 'order') {
        copy[key] = [value]
        return
      }
      const valid = validFilters.filter(f => f.key === key)[0]
      if (!valid) {
        return;
      }
      if (valid.multiple) {
        copy[key] = value.split(',')
      } else {
        copy[key] = [value]
      }
    })
    setFilters(copy)
    fetch(true)
  }, [])

  useEffect(() => {
    if (fetched) {
      let query = '?'
      Object.keys(filters).map(key => {
        if (filters[key]?.length === 0) {
          return
        }
        query += key + '='
        filters[key].forEach(filter => query += filter + ',')
        query = query.slice(0, -1)
        query += '&'
      })
      query = query.slice(0, -1)
      navigate(location.pathname + query)
    }
  }, [filters])
  
  const updateFilters = (key: string, multiple: boolean, ...value: string[]) => {
    const copy = {...filters}
    if (copy[key]?.includes(value[0])) {
      copy[key].splice(copy[key].indexOf(value[0]), 1)
    }
    else if (!copy[key]?.length || !multiple) {
      copy[key] = value
    } else {
      copy[key]= copy[key].concat(value)
    }
    
    setFilters(copy)
  }

  return updateFilters
}