interface ImageProps {
  src: string
}

export default function MarginImage({src}: ImageProps) {
  return <img style={{margin: '25vh 0'}} src={src} />
}