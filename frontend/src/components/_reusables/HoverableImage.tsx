import { CSSProperties } from 'react'

interface HoverableImageProps {
  children: React.ReactNode,
  src: string,
  styles?: CSSProperties,
  className?: string,
  innerClassName?: string
}

export default function HoverableImage({children, src, styles = {}, className = '', innerClassName = ''}: HoverableImageProps) {
  return <div className={'hoverable-image position-relative overflow-hidden bg-dark ' + className}>
    <img style={styles} className='img-fluid position-relative' src={src} />
    <div className={'position-absolute w-100 h-100 start-0 top-0 ' + innerClassName}>
      {children}
    </div>
  </div>
}