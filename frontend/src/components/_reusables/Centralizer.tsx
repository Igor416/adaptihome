interface CentralizerProps {
  children: React.ReactNode
}

export default function Centralizer({children}: CentralizerProps) {
  return <div className='d-flex'>
    <div className='col-sm-2'></div>
    <div className='col-12 col-sm-8'>
      {children}
    </div>
    <div className='col-sm-2'></div>
  </div>
}