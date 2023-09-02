import { ReactNode } from 'react'
import { Link } from 'react-router-dom'
import HoverableImage from './HoverableImage'
import { ResponsiveProps } from '../..'

interface LinkImageProps extends ResponsiveProps {
  to: string,
  children: ReactNode,
  image: string
}

export default function LinkImage({to, children, image, isMobile}: LinkImageProps) {
  return <Link to={to} className='position-relative d-flex flex-column flex-sm-row justify-content-end ps-sm-5'>
    {
      isMobile
      ?
      <span className='mb-4 no-link h3'>{children}</span>
      :
      <span style={{zIndex: 1100}} className='position-absolute top-50 start-0 text-black h1'>{children}</span>
    }
    <HoverableImage className='ms-sm-5' src={image}>

    </HoverableImage>
  </Link>
}