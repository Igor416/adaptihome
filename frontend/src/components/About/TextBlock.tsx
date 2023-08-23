interface TextBlockProps {
  section: string,
  heading: string,
  t1: string,
  t2: string
}

export default function TextBlock({section, heading, t1, t2}: TextBlockProps) {
  return <div className='d-flex flex-column mt-5 p-5 text-start'>
    <div className='d-flex'>
      <div className='d-flex col-6 h4'>{section}</div>
      <div className='d-flex col-6 h2'>{heading}</div>
    </div>
    <div style={{marginTop: '10vh'}} className='d-flex h5'>
      <div className='d-flex col-6'>{t1}</div>
      <div className='d-flex col-6'>{t2}</div>
    </div>
  </div>
}