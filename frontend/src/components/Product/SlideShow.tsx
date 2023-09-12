import { useState } from 'react'
import HoverableImage from '../_reusables/HoverableImage'
import Circle from './Circle'
import { ResponsiveProps } from '../..'

interface SlideShowProps extends ResponsiveProps {
  images: string[]
}

export default function SlideShow({images, isMobile}: SlideShowProps) {
  const [pickedImage, pickImage] = useState(0)

  return <div
    id='photos'
    className='carousel slide d-flex flex-column-reverse flex-sm-row flex-sm-nowrap col-sm-6'
    data-bs-ride='carousel'
    data-bs-interval='false'
  >
    <div className='d-flex flex-sm-column align-items-sm-center p-5'>
      {images.map((_, i) => 
        <div data-bs-target="#photos" data-bs-slide-to={i} key={i} className='mb-sm-4 mx-3 mx-sm-0'>
          <Circle size={isMobile ? 10 : 2.5} color='dark' active={i === pickedImage} setActive={() => pickImage(i)} />
        </div>
      )}
    </div>
    <div className='flex-grow-1 carousel-inner'>
      {images.map((image, i) => 
        <HoverableImage
          key={i}
          styles={{
            opacity: 1
          }}
          className={'bg-whitesmoke carousel-item' + (i === 0 ? ' active' : '')}
          src={image}
        >
          
        </HoverableImage>
      )}
    </div>
  </div>
}