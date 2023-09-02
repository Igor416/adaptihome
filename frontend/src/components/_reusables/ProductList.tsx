import { ReactNode } from 'react';
import { Product } from '../../JSONTypes';
import { t } from 'i18next';
import { Link } from 'react-router-dom';
import HoverableImage from './HoverableImage';
import OldPrice from './OldPrice';
import Price from './Price';
import { ResponsiveProps } from '../..';

interface ProductListProps extends ResponsiveProps {
  products?: Product[]
}

export default function ProductList({products, isMobile}: ProductListProps) {
  return <div style={{gridTemplateColumns: 'auto '.repeat(isMobile ? 1 : 2), padding: isMobile ? '0' : '12.5vh 12.5vw'}} className='d-grid'>
    {products && products.map((product, i) => 
      <Link key={i} to={'/product/' + product.category.name + '/' + product.name} className={'text-secondary' + (products?.length === 1 && !isMobile ? ' w-50' : '')}>
        <HoverableImage src={product.shortcut} styles={{opacity: 0.9}} className='m-3'>
          <span className='position-absolute mt-3 ms-4 start-0 h6'>{product.category.name_s}</span>
          <div className='position-absolute d-flex flex-column align-items-start bottom-0 start-0 mb-3 ms-4'>
            <span className='h4 text-black'>{product.name}</span>
            <div className='d-flex flex-nowrap h5'>
              <OldPrice discount={product.discount} size={product.sizes[0]} />
              <Price discount={product.discount} size={product.sizes[0]} from={t('from')} />
            </div>
          </div>
        </HoverableImage>
      </Link>
    )}
  </div>
}