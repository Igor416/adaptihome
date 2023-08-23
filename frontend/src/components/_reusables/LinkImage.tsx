import { ReactNode } from "react"
import { Link } from "react-router-dom"
import HoverableImage from "./HoverableImage"

interface LinkImageProps {
  to: string,
  children: ReactNode,
  image: string
}

export default function LinkImage({to, children, image}: LinkImageProps) {
  return <Link to={to} className='position-relative d-flex justify-content-end ps-5'>
    <span style={{zIndex: 1100}} className='position-absolute top-50 start-0 text-black h1'>{children}</span>
    <HoverableImage className='ms-5' src={image}>

    </HoverableImage>
  </Link>
}