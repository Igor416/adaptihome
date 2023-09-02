import { ResponsiveProps } from "../.."

interface ImageProps extends ResponsiveProps {
  src: string
}

export default function MarginImage({src, isMobile}: ImageProps) {
  return <img className='img-fluid' style={{margin: isMobile ? '10vh 0' : '25vh 0'}} src={src} />
}