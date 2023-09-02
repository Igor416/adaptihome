import { useState } from 'react'
import { useTranslation } from 'react-i18next'
import useProduct from './useProduct'
import SlideShow from './SlideShow'
import HoverableImage from '../_reusables/HoverableImage'
import OldPrice from '../_reusables/OldPrice'
import Price from '../_reusables/Price'
import Sizing from './Sizing'
import Centralizer from '../_reusables/Centralizer'
import LinkImage from '../_reusables/LinkImage'
import Section from './Section'
import SideText from './SideText'
import ProductList from '../_reusables/ProductList'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faShoppingCart } from '@fortawesome/free-solid-svg-icons'
import { Product } from '../../JSONTypes'
import { OutletContextProps } from '../App'
import { useOutletContext } from 'react-router-dom'
import { ResponsiveProps } from '../..'

export default function Product({isMobile}: ResponsiveProps) {
  const outletContext: OutletContextProps = useOutletContext()
  const product = useProduct()
  const [t, i18n] = useTranslation('product')
  const [pickedSize, pickSize] = useState(0)
  const [openedSection, openSection] = useState(-1)

  const renderOption = (key: string) => {
    const val = product?.characteristic[key]
    if (Array.isArray(val)) {
      return val.join(' / ')
    }

    if (typeof val == 'boolean') {
      return val ? t('yes') : t('no')
    }
  
    return val
  }

  if (product) {
    return <div className='d-flex mt-sm-5 flex-column'>
      <div className='d-flex flex-column flex-sm-row flex-sm-nowrap align-items-center'>
        <div className='d-flex justify-content-end col-sm-6'>
          <HoverableImage src={product.shortcut} styles={{opacity: 0.9}} >
            
          </HoverableImage>
        </div>
        <div className='d-flex flex-column align-items-start p-4 py-sm-0 text-center text-sm-start mx-sm-5 px-sm-5'>
          <span className='h3 mx-sm-5 w-100'>{product.name}</span>
          <span className='h6 m-sm-5'>{product.desc}</span>
          <div className='d-flex flex-column flex-sm-row justify-content-between w-100 mt-5 mt-sm-0 align-items-center'>
            <div className='d-flex flex-column mx-sm-5 h4'>
              <OldPrice discount={product.discount + product.sizes[pickedSize].discount} size={product.sizes[pickedSize]} />
              <Price discount={product.discount} size={product.sizes[pickedSize]} />
            </div>
            <div
              onClick={() => outletContext.addSize(outletContext.clearProduct(product, product.sizes[pickedSize]))}
              className='p-3 text-white bg-blue col-12 col-sm-auto mt-4 mt-sm-0 rounded-pill'
            >
              <span className='me-1'>{t('Add to Cart')}</span>
              <FontAwesomeIcon icon={faShoppingCart} />
            </div>
          </div>
        </div>
      </div>
      <SideText text={t('size') + '.'} />
      <div className='d-flex flex-column flex-sm-row flex-sm-nowrap align-items-center my-5'>
        <SlideShow images={product.images} isMobile={isMobile} />
        <Sizing sizes={product.sizes} pickedSize={pickedSize} pickSize={pickSize} t={t} isMobile={isMobile} />
      </div>
      <SideText text={t('description') + ':'} />
      <div style={{margin: isMobile ? 0 : '0 20vw'}} className='accordion d-flex flex-column p-4 p-sm-0' id='details'>
        <span className='h5'>{product.desc}</span>
        <Section id='information' title={t('information')} opened={openedSection === 1} open={() => openSection(openedSection === 1 ? -1 : 1)}>
          {Object.keys(product.characteristic).map((key, i) => 
            <div key={i} className='py-1'>
              <span>{key}:</span>
              <span className='ms-1 text-secondary'>{renderOption(key)}</span>
            </div>
          )}
        </Section>
        {product.structure && <Section id='structure' title={t('structure')} opened={openedSection === 2} open={() => openSection(openedSection === 2 ? -1 : 2)}>
          {product.structure.map((layer, i) => 
            <div key={i} className='d-flex py-2 align-items-center'>
              <div className='col-sm-3 h5'>
                <span>{layer.name}</span>
              </div>
              <div className='col-sm-2 d-flex align-items-center'>
                <img src={layer.image} />
              </div>
              <div className='col-sm-7'>
                <span>{layer.desc}</span>
              </div>
            </div>
          )}
        </Section>}
      </div>
      <SideText marginBottom={0} text={t('related') + '.'} />
      <ProductList products={[product]} isMobile={isMobile} />
      <Centralizer>
        <div className='p-5'>
          <LinkImage to='/shop/folding_bed/' image='https://flatstudio.md/img/footeradvanced/type_shop.jpg' isMobile={isMobile}>{t('shop_more')}<sup>130</sup></LinkImage>
        </div>
      </Centralizer>
    </div>
  }
  return <></>
}