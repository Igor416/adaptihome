interface TextBlockProps {
  section: string,
  heading: string,
  t1: string,
  t2: string
}

export default function TextBlock({section, heading, t1, t2}: TextBlockProps) {
  return <div className='d-flex flex-column mt-5 p-5 text-sm-start text-center'>
    <div className='d-flex flex-column flex-sm-row'>
      <div className='col-sm-6 h4 mb-5 mb-sm-0'>{section}</div>
      <div className='col-sm-6 h2'>{heading}</div>
    </div>
    <div style={{marginTop: '10vh'}} className='d-flex flex-column flex-sm-row h5'>
      <div className='col-sm-6 mb-5 mb-sm-0'>{t1}</div>
      <div className='col-sm-6'>{t2}</div>
    </div>
  </div>
}