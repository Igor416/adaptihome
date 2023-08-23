import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { LinksProps } from '../..';
import { Filters, Product } from '../../JSONTypes';
import { getProducts } from '../../api';
import SideText from '../_reusables/SideText';
import PlusIcon from './PlusIcon';
import Submenu from './SubMenu';
import Checkable from './Checkable';
import useCategory from './useCategory';
import useFilters from './useFilters';
import ProductList from '../_reusables/ProductList';

export default function Shop({links}: LinksProps) {
  const [category, setCategory] = useState('folding_bed')
  const [filters, setFilters] = useState<Filters>({order: ['low']});
  const [categoryOpened, openCategory] = useState(false)
  const [filterOpened, openFilter] = useState(false)
  const [products, setProducts] = useState<Product[]>()
  const [t, i18n] = useTranslation(['shop', 'links'])

  const linkFilters = useCategory(category, setCategory, links)
  const updateFilters = useFilters(filters, setFilters, linkFilters)

  useEffect(() => {
    getProducts().then(setProducts)
  }, [category, filters])

  useEffect(() => {
    if (categoryOpened) {
      openFilter(false)
    }
  }, [categoryOpened])

  useEffect(() => {
    if (filterOpened) {
      openCategory(false)
    }
  }, [filterOpened])

  return <div className='d-flex flex-column align-items-center h4 text-center'>
    <SideText text='shop' right='7' />
    <div id='shop_menu' className='d-flex flex-nowrap border-top border-bottom w-100'>
      <div className='p-5 col-6 d-flex border-end'>
        <div className='col-6'></div>
        <div onClick={() => openCategory(!categoryOpened)} className='col-6 d-flex justify-content-between align-items-end'>
          <span>{t(category + '.name', {ns: 'links'})}</span>
          <PlusIcon size={2} active={categoryOpened} />
        </div>
      </div>
      <div className='p-5 col-6 d-flex border-start'>
        <div onClick={() => openFilter(!filterOpened)} className='col-6 d-flex justify-content-between align-items-end'>
          <span>{t('filter')}</span>
          <PlusIcon size={2} active={filterOpened} />
        </div>
        <div className='col-6'></div>
      </div>
    </div>
    <Submenu active={categoryOpened} side='left'>
      {links.map((link, i) => {
        return <div
          key={i}
          onClick={() => {setCategory(link.name);openCategory(false);setFilters({order: ['low']})}}
          className={'d-flex py-2' + (link.name === category ? ' text-teal' : '')}
        >
          <span>
            {t(link.name + '.name', {ns: 'links'})}
            <sup>{link.count}</sup>
          </span>
        </div>
      })}
    </Submenu>
    <Submenu active={filterOpened} side='right' t={t} clear={() => setFilters({order: ['low']})}>
      <div className='h6 text-secondary py-2'>{t('order_by')}</div>
      {['a', 'z', 'low', 'high'].map((ordering, i) => 
        <Checkable key={i} checked={filters.order.includes(ordering)} value={t(ordering)} onChecked={() => updateFilters('order', false, ordering)} />
      )}
      {links.filter(l => l.name === category)[0].filters.map((group, i) =>
        <div key={i} className='d-flex flex-column border-top my-2 py-2'>
          <div className='h6 text-secondary py-2'>{t(group.key)}</div>
          {group.values.map((filter, j) => 
            <Checkable
              key={j}
              checked={filters[group.key]?.includes(filter)}
              value={t(filter)}
              onChecked={() => updateFilters(group.key, group.multiple, filter)}
              multiple={group.multiple}
            />
          )}
        </div>
      )}
    </Submenu>
    <ProductList products={products} />
  </div>
}