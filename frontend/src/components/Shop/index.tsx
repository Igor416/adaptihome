import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { LinksProps, ResponsiveProps } from '../..';
import { Filters, MattressColectionPrice, Product } from '../../JSONTypes';
import { getMattressColectionsPrice, getProducts } from '../../api';
import SideText from '../_reusables/SideText';
import PlusIcon from './PlusIcon';
import Submenu from './SubMenu';
import Checkable from '../_reusables/Checkable';
import useCategory from './useCategory';
import useFilters from './useFilters';
import ProductList from '../_reusables/ProductList';
import Price from '../_reusables/Price';
import Tab from './Tab';

export default function Shop({links, isMobile}: LinksProps & ResponsiveProps) {
  const [category, setCategory] = useState('folding_bed')
  const [filters, setFilters] = useState<Filters>({order: ['low']});
  const [categoryOpened, openCategory] = useState(false)
  const [filterOpened, openFilter] = useState(false)
  const [products, setProducts] = useState<Product[]>()
  const [mattressCollectionsPrice, setMattressCollectionsPrice] = useState<MattressColectionPrice>()
  const [t, i18n] = useTranslation(['shop', 'links'])

  const linkFilters = useCategory(category, setCategory, links)
  const updateFilters = useFilters(filters, setFilters, linkFilters)

  useEffect(() => {
    getMattressColectionsPrice().then((resp) => {
      const mattressCollectionsPrice: MattressColectionPrice = {}
      for (let pair of resp) {
        mattressCollectionsPrice[Object.keys(pair)[0]] = pair[Object.keys(pair)[0]]
      }
      setMattressCollectionsPrice(mattressCollectionsPrice)
    })
  }, [])

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
    <SideText text='shop' right='7' isMobile={isMobile} />
    <div id='shop_menu' className='d-flex flex-nowrap border-top border-bottom w-100'>
      <Tab setter={openCategory} active={categoryOpened} text={t(category + '.name', {ns: 'links'})} direction='' />
      <Tab setter={openFilter} active={filterOpened} text={t('filter')} direction='-reverse' />
    </div>
    <Submenu active={categoryOpened} side='left' isMobile={isMobile}>
      {links.map((link, i) => {
        return <div
          key={i}
          onClick={() => {setCategory(link.name);openCategory(false);setFilters({order: ['low']})}}
          className={'d-flex py-2' + (link.name === category ? ' text-teal' : '')}
        >
          <span className='w-100'>
            {t(link.name + '.name', {ns: 'links'})}
            <sup>{link.count}</sup>
          </span>
        </div>
      })}
    </Submenu>
    <Submenu active={filterOpened} side='right' t={t} clear={() => setFilters({order: ['low']})} isMobile={isMobile}>
      <div className='h6 text-secondary py-2'>{t('order_by')}</div>
      {['a', 'z', 'low', 'high'].map((ordering, i) => 
        <Checkable key={i} checked={filters.order.includes(ordering)} value={t(ordering)} onChecked={() => updateFilters('order', false, ordering)} />
      )}
      {mattressCollectionsPrice && links.filter(l => l.name === category)[0].filters.map((group, i) =>
        <div key={i} className='d-flex flex-column border-top my-2 py-2'>
          <div className='h6 text-secondary py-2'>{t(group.key)}</div>
          {group.values.map((filter, j) => 
            <Checkable
              key={j}
              checked={filters[group.key]?.includes(filter)}
              value={category === 'mattress' && group.key === 'collection' ? <div className='d-flex justify-content-between'>{t(filter)}
                <span className='ms-4'>
                  <Price 
                    from={t('from')}
                    discount={0}
                    price={mattressCollectionsPrice[filter]}
                  />
                </span>
              </div> : t(filter)}
              onChecked={() => updateFilters(group.key, group.multiple, filter)}
              multiple={group.multiple}
            />
          )}
        </div>
      )}
    </Submenu>
    <ProductList products={products} isMobile={isMobile} t={t} />
  </div>
}