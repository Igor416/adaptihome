import { faMinus, faPlus, faTimes } from "@fortawesome/free-solid-svg-icons"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { t } from "i18next"
import { Link } from "react-router-dom"
import Hoverable from "../_reusables/Hoverable"
import HoverableImage from "../_reusables/HoverableImage"
import Price from "../_reusables/Price"
import SizeDisplay from "../_reusables/SizeDisplay"
import Space from "./Space"
import { OutletContextProps } from "../App"

interface SummaryProps extends OutletContextProps {
  showTotal?: boolean
}

export default function Summary({products, total, updateQuantity, deleteSize, showTotal = true}: SummaryProps) {
  return <div className='d-flex flex-wrap'>
    <Space color='white' />
    <div className='col-9 d-flex flex-column bg-white'>
      {products.map((product, i) => {return product.sizes.map((size, j) => 
        <div key={i * 100 + j} className={'d-flex align-items-center py-5' + (products.length > 1 ? ' border-bottom' : '')}>
          <div className='col-2 p-2'>
            <HoverableImage src={product.shortcut} styles={{opacity: 0.9}}>

            </HoverableImage>
          </div>
          <div className='d-flex flex-column align-items-start col-2'>
            <Link to={`/product/${product.category.name}/${product.name}/`} className='h4 text-decoration-none text-dark'>
              <Hoverable color='dark'>{product.name}</Hoverable>
            </Link>
            <span>{product.category.name_s}</span>
          </div>
          <div className='d-flex col-2 d-flex justify-content-center align-items-center h6'>
           {showTotal && <FontAwesomeIcon
              onClick={() => updateQuantity(product, size, -1)}
              icon={faMinus}
              style={{height: '1vh', aspectRatio: 1}}
              className='bg-red rounded-circle p-2'
            />}
            <span className={'mx-3' + (!showTotal ? ' h5' : '')}>{showTotal ? '' : 'x'}{size.quantity}</span>
            {showTotal && <FontAwesomeIcon
              onClick={() => updateQuantity(product, size, 1)}
              icon={faPlus}
              style={{height: '1vh', aspectRatio: 1}}
              className='bg-teal rounded-circle p-2'
            />}
          </div>
          <div className='col-3 h5 d-flex justify-content-center'>
            <SizeDisplay size={size} t={t} />
          </div>
          <div className='col-2 h5 d-flex justify-content-center'>
            <Price discount={0} size={size} />
          </div>
          <div onClick={() => deleteSize(product)} className='col-1 h5 text-secondary text-end'>
            <FontAwesomeIcon icon={faTimes} />
          </div>
        </div>
      )})}
    </div>
    <Space color='white' />
    {showTotal && <Space />}
    {showTotal && <div className='col-9 d-flex justify-content-between my-5 py-5 h5'>
      <span>{t('total')}</span>
      <span>
        {total.toFixed(2)}
        <sup>EUR</sup>
      </span>
    </div>}
    {showTotal && <Space />}
  </div>
}