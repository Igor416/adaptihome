interface CentralizerProps {
  children: React.ReactNode
}

export default function Centralizer({children}: CentralizerProps) {
  return <div className='d-flex'>
    <div className='col-2'></div>
    <div className='col-8'>
      {children}
    </div>
    <div className='col-2'></div>
  </div>
}