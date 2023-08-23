import { useState } from "react"
import HoverableImage from "../_reusables/HoverableImage"
import Circle from "./Circle"

interface SlideShowProps {
  images: string[]
}

export default function SlideShow({images}: SlideShowProps) {
  const [pickedImage, pickImage] = useState(0)

  return <div className='d-flex flex-nowrap col-6'>
    <div className='d-flex flex-column align-items-center p-5'>
      {images.map((image, i) => 
        <div key={i} className='mb-4'>
          <Circle size={2.5} color='dark' active={i === pickedImage} setActive={() => pickImage(i)} />
        </div>
      )}
    </div>
    <div className='position-relative flex-grow-1'>
      {images.map((image, i) => 
        <HoverableImage
          key={i}
          styles={{
            opacity: i === pickedImage ? 1 : 0
          }}
          className={'position-absolute w-100 h-100 ' + (i === pickedImage ? 'visible' : 'invisible')}
          src={image}
        ><></></HoverableImage>
      )}
    </div>
  </div>
}