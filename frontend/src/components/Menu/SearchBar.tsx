import { useState, useEffect } from "react"
import { SearchResults } from "../../JSONTypes"
import { sendSearch } from "../../api"
import { TranslationProps } from "../../i18n"
import { faSearch, faTimes } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import Hoverable from "../_reusables/Hoverable"
import { Link } from "react-router-dom"
import OldPrice from "../_reusables/OldPrice"
import Price from "../_reusables/Price"

export default function SearchBar({t}: TranslationProps) {
  const [search, setSearch] = useState('')
  const [show, setShow] = useState(false)
  const [res, setRes] = useState<SearchResults>({categories: [], products: []})

  useEffect(() => {
    if (search.length > 1) {
      setShow(true)
      sendSearch(search).then(data => {setRes(data)})
      return
    }
    setRes({categories: [], products: []})
    setShow(false)
  }, [search])

  return <div className='w-100'>
    <div className='input-group flex-nowrap'>
      <input
        className='p-3 rounded-end rounded-pill bg-whitesmoke border-0 no-hover w-100'
        type='text'
        id='search_query_input'
        value={search}
        onFocus={() => setShow(search.length > 1)}
        onChange={e => setSearch(e.target.value)}
      />
      <button className='p-3 rounded-start rounded-pill bg-whitesmoke border-0 no-hover'>
        <FontAwesomeIcon icon={faSearch} color='var(--blue)' />
      </button>
    </div>
    <div
      style={{
        zIndex: 1200,
        width: '40%',
        display: show ? 'block' : 'none',
      }}
      className='border bg-white position-absolute py-3 px-4 mt-4'
    >
      <span className='mb-4'>{t('help')}</span>
      <div className='w-100 d-flex flex-column border-bottom mt-3'>
        <span className='h5 pb-2'>{t('search_categories')}: </span>
        {res.categories.map((item, index) => 
          <div key={index} className='d-flex row-nowrap justify-content-between pb-2 text-end link'>
            <Link onClick={() => setShow(false)} className='no-link no-hover' to={item.link}>
              <Hoverable color='blue'>{item.text}</Hoverable>
            </Link>
            <span>({item.count})</span>
          </div>
        )}
      </div>
      <div className='w-100 d-flex flex-column border-bottom mt-3'>
        <span className='h5 pb-2'>{t('search_products')}: </span>
        {res.products.map((item, index) => 
          <div key={index} className='d-flex row-nowrap justify-content-between pb-2 text-end link'>
            <Link onClick={() => setShow(false)} className='no-link no-hover' to={item.link}>
              <Hoverable color='blue'>{item.text}</Hoverable>
            </Link>
            <OldPrice discount={item.discount} price={item.price} />
            <Price from={t('from')} discount={item.discount} price={item.price} />
          </div>
        )}
      </div>
      <FontAwesomeIcon
        icon={faTimes}
        onClick={() => {document.getElementById('search_query_input')?.blur();setShow(false)}}
        className='position-absolute end-0 top-0 mt-3 me-3'
      />
    </div>
  </div>
}