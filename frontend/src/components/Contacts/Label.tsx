interface LabelProps {
  label: string,
  content: string
}

export default function Label({label, content}: LabelProps) {
  return <div className='d-flex flex-column my-4'>
    <span className='text-teal h5'>{label}:</span>
    <span className='mt-2 text-nowrap h6'>{content}</span>
  </div>
}