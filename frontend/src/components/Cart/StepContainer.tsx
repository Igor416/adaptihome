import { ReactNode } from 'react';

interface StepContainerProps {
  children: ReactNode[]
}

export default function StepContainer({children}: StepContainerProps) {
  return <div id='steps' className='carousel slide col-12' data-bs-ride='carousel' data-bs-interval='false'>
    <div className='carousel-inner col-12'>
      {children.map((child, i) => 
        <div key={i} className={'carousel-item col-12' + (i === 0 ? ' active' : '')}>
          {child}
        </div>
      )}
    </div>
  </div>
}